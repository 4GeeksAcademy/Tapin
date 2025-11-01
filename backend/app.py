from flask import Flask
from flask import Flask, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from backend.auth import token_for
from flask_cors import CORS
from datetime import datetime
import os
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
import smtplib
from email.message import EmailMessage


app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
# Load .env from repository root in development if python-dotenv is installed
try:
    from dotenv import load_dotenv

    repo_root = os.path.abspath(os.path.join(base_dir, '..'))
    load_dotenv(os.path.join(repo_root, '.env'))
except Exception:
    # python-dotenv not installed or .env missing; proceed with environment variables
    pass

# Allow overriding the database URL via environment (useful for CI or production)
default_db = 'sqlite:///' + os.path.join(base_dir, 'data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', default_db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Secret key used for serializer tokens and other Flask features
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', app.config['SECRET_KEY'])
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get('SECURITY_PASSWORD_SALT', 'dev-salt')

CORS(app)

db = SQLAlchemy(app)
jwt = JWTManager(app)


def _warn_on_default_secrets():
    """Log a warning if important secret env vars are left at their dev defaults.

    This is only advisory and will not stop the app from running. It's helpful
    for local dev and in CI to call out missing secret configuration.
    """
    defaults = {
        'SECRET_KEY': 'dev-secret-key',
        'SECURITY_PASSWORD_SALT': 'dev-salt',
    }
    missing = []
    for key, default_val in defaults.items():
        val = os.environ.get(key, app.config.get(key))
        if not val or (isinstance(val, str) and val == default_val):
            missing.append(key)
    # JWT_SECRET_KEY may default to SECRET_KEY; still warn if it's the same as the dev key
    jwt_key = os.environ.get('JWT_SECRET_KEY', app.config.get('JWT_SECRET_KEY'))
    if not jwt_key or jwt_key == app.config.get('SECRET_KEY') == defaults['SECRET_KEY']:
        missing.append('JWT_SECRET_KEY')

    if missing:
        app.logger.warning(
            "Missing or default secrets detected: %s.\n"
            "For local dev copy `.env.sample` -> `.env` and set strong values."
            " See backend/CONFIG.md for details.",
            ', '.join(sorted(set(missing)))
        )


_warn_on_default_secrets()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    # simple role column for basic RBAC (default: "user")
    role = db.Column(db.String(50), default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {"id": self.id, "email": self.email}


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "owner_id": self.owner_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class Item(db.Model):
    """Simple persistent items for the MVP /api/items endpoints."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}


def get_serializer():
    return URLSafeTimedSerializer(app.config['SECRET_KEY'])


# Ensure database tables exist when the app starts. Using app.app_context()
# is more robust than the before_first_request decorator which may not be
# available in all runtime contexts.
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return jsonify({"message": "Tapin Backend API Root"})


@app.route('/api/health', methods=['GET'])
def api_health():
    return jsonify({"status": "ok"}), 200


@app.route('/api/items', methods=['GET'])
def api_list_items():
    # Return all items from the database
    items = Item.query.order_by(Item.id.asc()).all()
    return jsonify({"items": [i.to_dict() for i in items]}), 200


@app.route('/api/items', methods=['POST'])
@jwt_required()
def api_create_item():
    data = request.get_json() or {}
    name = data.get('name')
    if not name:
        return jsonify({"error": "name required"}), 400
    item = Item(name=name, description=data.get('description'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201


@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({"error": "email and password required"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "user already exists"}), 400
    pw_hash = generate_password_hash(password)
    user = User(email=email, password_hash=pw_hash)
    db.session.add(user)
    db.session.commit()
    # return both access and refresh tokens (identity stored as string)
    from backend.auth import token_pair

    tokens = token_pair(user)
    return jsonify({"message": "user created", "user": user.to_dict(), **tokens}), 201


@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "invalid credentials"}), 401
    # return both access and refresh tokens to the client
    from backend.auth import token_pair

    tokens = token_pair(user)
    return jsonify({"message": "login successful", "user": user.to_dict(), **tokens})


@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh_token():
    """Exchange a valid refresh token for a new access token."""
    uid = get_jwt_identity()
    try:
        uid_int = int(uid)
    except Exception:
        uid_int = uid
    user = db.session.get(User, uid_int)
    if not user:
        return jsonify({"error": "user not found"}), 404
    access_token = token_for(uid_int)
    return jsonify({"access_token": access_token})


@app.route('/me', methods=['GET'])
@jwt_required()
def me():
    uid = get_jwt_identity()
    # convert back to int because tokens store identity as string
    try:
        uid_int = int(uid)
    except Exception:
        uid_int = uid
    # Use Session.get() which is the modern SQLAlchemy API (avoids LegacyAPIWarning)
    user = db.session.get(User, uid_int)
    if not user:
        return jsonify({"error": "user not found"}), 404
    return jsonify({"user": user.to_dict()})


def send_reset_email(to_email, reset_url):
    smtp_host = os.environ.get('SMTP_HOST')
    if not smtp_host:
        return False, 'SMTP not configured'
    smtp_port = int(os.environ.get('SMTP_PORT', 587))
    smtp_user = os.environ.get('SMTP_USER')
    smtp_pass = os.environ.get('SMTP_PASS')
    use_tls = os.environ.get('SMTP_USE_TLS', 'true').lower() in ('1', 'true', 'yes')

    msg = EmailMessage()
    msg['Subject'] = 'Tapin Password Reset'
    msg['From'] = smtp_user or f'no-reply@{smtp_host}'
    msg['To'] = to_email
    msg.set_content(f'Use the link to reset your password: {reset_url}')

    try:
        server = smtplib.SMTP(smtp_host, smtp_port, timeout=10)
        server.ehlo()
        if use_tls:
            server.starttls()
            server.ehlo()
        if smtp_user and smtp_pass:
            server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        server.quit()
        return True, 'sent'
    except Exception as e:
        return False, str(e)


@app.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json() or {}
    email = data.get('email')
    if not email:
        return jsonify({"error": "email required"}), 400
    user = User.query.filter_by(email=email).first()
    if not user:
        # Do not reveal whether the email exists
        return jsonify({"message": "If an account exists for that email, a reset link has been sent."})

    serializer = get_serializer()
    token = serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])
    reset_url = url_for('confirm_reset', token=token, _external=True)

    sent, info = send_reset_email(email, reset_url)
    if sent:
        return jsonify({"message": "reset email sent"})
    else:
        # Fallback in dev: return the reset_url so developers can use it
        return jsonify({"message": "smtp not configured, returning reset link (dev)", "reset_url": reset_url, "error": info})


@app.route('/reset-password/confirm/<token>', methods=['POST'])
def confirm_reset(token):
    data = request.get_json() or {}
    new_password = data.get('password')
    if not new_password:
        return jsonify({"error": "password required"}), 400
    serializer = get_serializer()
    try:
        email = serializer.loads(token, salt=app.config['SECURITY_PASSWORD_SALT'], max_age=3600)
    except SignatureExpired:
        return jsonify({"error": "token expired"}), 400
    except BadSignature:
        return jsonify({"error": "invalid token"}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "no such user"}), 404
    user.password_hash = generate_password_hash(new_password)
    db.session.commit()
    return jsonify({"message": "password updated"})


@app.route('/listings', methods=['GET'])
def get_listings():
    # Support simple filtering via query params: q (text search on title/description), location
    q = request.args.get('q', type=str)
    location = request.args.get('location', type=str)

    query = Listing.query
    if q:
        like = f"%{q}%"
        query = query.filter((Listing.title.ilike(like)) | (Listing.description.ilike(like)))
    if location:
        query = query.filter(Listing.location.ilike(f"%{location}%"))

    listings = query.order_by(Listing.created_at.desc()).all()
    return jsonify([l.to_dict() for l in listings])


@app.route('/listings', methods=['POST'])
@jwt_required()
def create_listing():
    data = request.get_json() or {}
    title = data.get('title')
    if not title:
        return jsonify({"error": "title required"}), 400
    # JWT identity is stored as string; convert back to int for DB foreign key
    owner_id = int(get_jwt_identity())
    listing = Listing(title=title, description=data.get('description'), location=data.get('location'), owner_id=owner_id)
    db.session.add(listing)
    db.session.commit()
    return jsonify(listing.to_dict()), 201


@app.route('/listings/<int:id>', methods=['GET'])
def get_listing_detail(id):
    listing = Listing.query.get_or_404(id)
    return jsonify(listing.to_dict())


@app.route('/listings/<int:id>', methods=['PUT'])
@jwt_required()
def update_listing(id):
    listing = Listing.query.get_or_404(id)
    data = request.get_json() or {}
    listing.title = data.get('title', listing.title)
    listing.description = data.get('description', listing.description)
    listing.location = data.get('location', listing.location)
    db.session.commit()
    return jsonify(listing.to_dict())


@app.route('/listings/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_listing(id):
    listing = Listing.query.get_or_404(id)
    db.session.delete(listing)
    db.session.commit()
    return jsonify({"message": "deleted"})


if __name__ == '__main__':
    app.run(debug=True)
