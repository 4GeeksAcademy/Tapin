# PHASE 2 MVP: TECHNICAL IMPLEMENTATION GUIDE

**Created by:** @architect  
**Purpose:** Bridge system architecture to current codebase + development tasks  
**Timeline:** Weeks 9-20 (Months 3-5)  
**Status:** Ready to hand off to @dev team

---

## 🔗 CURRENT STATE vs. PHASE 2 REQUIREMENTS

### What We Have (Current Backend)

```python
# /backend/app.py - Flask app with:
✅ Flask framework (configured)
✅ SQLAlchemy ORM (configured)
✅ JWT authentication (configured)
✅ CORS enabled
✅ Database models (basic schema exists)
✅ Some API endpoints (30+ tests show existing functionality)
✅ Email sending infrastructure (SMTP)

# Current Models (likely):
✅ User/Auth models
✅ Volunteer models (possibly)
✅ Nonprofit models (possibly)
❓ Need to verify exact schema
```

### What We Need to ADD (Phase 2 MVP)

```
❌ Matching algorithm (CRITICAL - core of business model)
❌ Geographic zone system (CRITICAL - hyper-local feature)
❌ Volunteer_needs table (NEW - primary entity)
❌ Volunteer_matches table (NEW - algorithm output)
❌ Assignment tracking (ENHANCED - show-up tracking)
❌ Feedback loop system (NEW - for algorithm learning)
❌ Nonprofit dashboard endpoints (MISSING)
❌ Volunteer app endpoints (MISSING)
❌ Real-time metrics/analytics (MISSING)
❌ Notification system (email/SMS)
```

### Migration Path

```
Week 9-10: SETUP & FOUNDATION
├─ Audit current schema (what exists? what's missing?)
├─ Design new tables (volunteer_needs, volunteer_matches, geographic_zones)
├─ Create database migrations (alembic/)
├─ Implement matching algorithm core
└─ Write unit tests for algorithm

Week 11-12: API LAYER
├─ Implement nonprofit dashboard endpoints
├─ Implement volunteer app endpoints
├─ Wire up matching algorithm to endpoints
├─ Add feedback collection endpoints
└─ Integration tests for all new endpoints

Week 13-14: FRONTEND
├─ Build nonprofit dashboard UI
├─ Build volunteer app UI
├─ Connect to backend API
├─ Local testing of full flow
└─ Ready for pilot deployment

Week 15-20: PILOT LAUNCH & ITERATION
├─ Deploy to staging
├─ Onboard nonprofit pilots
├─ Track metrics (show-up rate, satisfaction)
├─ Weekly algorithm iteration
└─ Prepare for Phase 3
```

---

## 🗄️ DATABASE MIGRATION TASKS

### Step 1: Audit Current Schema

**Action Items (Week 9 - First Task):**

```bash
# 1. Check what tables already exist
sqlite3 backend/data.db ".schema"

# 2. Review current models in app.py
# Look for: db.Model classes

# 3. Check alembic migrations
ls -la backend/alembic/versions/

# 4. Document current state in CURRENT-SCHEMA.md
```

**Questions to Answer:**

- Do we have `User` model? What fields?
- Do we have `Volunteer` model? What fields?
- Do we have `Nonprofit` model? What fields?
- What's the relationship structure?
- Any existing assignments/opportunities tracking?

### Step 2: Create New Models (Phase 2 Needed)

**File:** `backend/models.py` (Create new file)

```python
# models.py - New data models for Phase 2

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from enum import Enum

db = SQLAlchemy()

# ============== ENUMS ==============

class UserRole(Enum):
    NONPROFIT = "nonprofit"
    VOLUNTEER = "volunteer"
    ADMIN = "admin"

class NonprofitTier(Enum):
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"

class VolunteerTier(Enum):
    FREE = "free"
    PREMIUM = "premium"
    PRO = "pro"

class NeedStatus(Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    FILLED = "filled"
    CANCELLED = "cancelled"

class AssignmentStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    NO_SHOW = "no_show"

class MatchStatus(Enum):
    SUGGESTED = "suggested"
    CLICKED = "clicked"
    ASSIGNED = "assigned"
    REJECTED = "rejected"

# ============== MODELS ==============

class GeographicZone(db.Model):
    __tablename__ = 'geographic_zones'

    id = db.Column(db.Integer, primary_key=True)
    zone_name = db.Column(db.String(255), nullable=False)
    neighborhood = db.Column(db.String(255))
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(2))
    postal_codes = db.Column(db.String(500))  # JSON array as string
    center_lat = db.Column(db.Float)
    center_lng = db.Column(db.Float)
    radius_miles = db.Column(db.Integer, default=3)
    nonprofit_count = db.Column(db.Integer, default=0)
    volunteer_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    nonprofits = db.relationship('Nonprofit', backref='location', lazy=True)
    volunteers = db.relationship('Volunteer', backref='home_zone', lazy=True)
    needs = db.relationship('VolunteerNeed', backref='location', lazy=True)


class Nonprofit(db.Model):
    __tablename__ = 'nonprofits'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    mission = db.Column(db.Text)
    size = db.Column(db.String(50))  # small, medium, large
    annual_budget = db.Column(db.Float)
    primary_contact_name = db.Column(db.String(255))
    primary_contact_phone = db.Column(db.String(20))
    nonprofit_location_id = db.Column(db.Integer, db.ForeignKey('geographic_zones.id'))
    tier = db.Column(db.String(50), default='free')
    subscription_start = db.Column(db.Date)
    subscription_end = db.Column(db.Date)
    monthly_rate = db.Column(db.Float)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Password for login (if nonprofit user)
    password_hash = db.Column(db.String(255))

    # Relationships
    volunteer_needs = db.relationship('VolunteerNeed', backref='nonprofit', lazy=True, cascade='all, delete-orphan')
    assignments = db.relationship('Assignment', backref='nonprofit', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Nonprofit {self.name}>'


class Volunteer(db.Model):
    __tablename__ = 'volunteers'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    skills = db.Column(db.Text)  # JSON array as string: '["mentoring", "tech"]'
    availability = db.Column(db.Text)  # JSON object as string
    home_zone_id = db.Column(db.Integer, db.ForeignKey('geographic_zones.id'))
    willingness_to_travel_miles = db.Column(db.Integer, default=3)
    motivation = db.Column(db.String(50))  # social_impact, skill_building, etc
    is_active = db.Column(db.Boolean, default=True)
    tier = db.Column(db.String(50), default='free')
    show_up_count = db.Column(db.Integer, default=0)
    no_show_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Password for login
    password_hash = db.Column(db.String(255))

    # Relationships
    matches = db.relationship('VolunteerMatch', backref='volunteer', lazy=True, cascade='all, delete-orphan')
    assignments = db.relationship('Assignment', backref='volunteer', lazy=True, cascade='all, delete-orphan')

    @property
    def show_up_rate(self):
        """Calculate this volunteer's show-up rate (0.0-1.0)"""
        total = self.show_up_count + self.no_show_count
        if total == 0:
            return 0.85  # Default for new volunteers (conservative)
        return self.show_up_count / total

    def __repr__(self):
        return f'<Volunteer {self.first_name} {self.last_name}>'


class VolunteerNeed(db.Model):
    """PRIMARY ENTITY: Each opportunity posted by nonprofit"""
    __tablename__ = 'volunteer_needs'

    id = db.Column(db.Integer, primary_key=True)
    nonprofit_id = db.Column(db.Integer, db.ForeignKey('nonprofits.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    required_skills = db.Column(db.Text)  # JSON array as string
    location_id = db.Column(db.Integer, db.ForeignKey('geographic_zones.id'))
    preferred_date = db.Column(db.Date)
    preferred_time = db.Column(db.Time)
    estimated_hours = db.Column(db.Float)
    status = db.Column(db.String(50), default='draft')  # draft, active, filled, cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posted_at = db.Column(db.DateTime)
    deadline = db.Column(db.DateTime)
    filled_at = db.Column(db.DateTime)

    # Relationships
    matches = db.relationship('VolunteerMatch', backref='need', lazy=True, cascade='all, delete-orphan')
    assignments = db.relationship('Assignment', backref='need', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<VolunteerNeed {self.title}>'


class VolunteerMatch(db.Model):
    """ALGORITHM OUTPUT: Suggested matches from AI"""
    __tablename__ = 'volunteer_matches'

    id = db.Column(db.Integer, primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.id'), nullable=False)
    need_id = db.Column(db.Integer, db.ForeignKey('volunteer_needs.id'), nullable=False)
    match_score = db.Column(db.Float)  # 0.0-1.0
    match_reasoning = db.Column(db.Text)  # JSON: scores for each factor
    suggested_at = db.Column(db.DateTime, default=datetime.utcnow)
    volunteer_viewed_at = db.Column(db.DateTime)
    volunteer_clicked_at = db.Column(db.DateTime)
    status = db.Column(db.String(50), default='suggested')  # suggested, clicked, assigned, rejected

    # Prevent duplicate suggestions
    __table_args__ = (db.UniqueConstraint('volunteer_id', 'need_id', name='unique_volunteer_need'),)

    def __repr__(self):
        return f'<VolunteerMatch V{self.volunteer_id} N{self.need_id} Score:{self.match_score:.2f}>'


class Assignment(db.Model):
    """COMMITMENT: Volunteer assigned to opportunity"""
    __tablename__ = 'assignments'

    id = db.Column(db.Integer, primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.id'), nullable=False)
    need_id = db.Column(db.Integer, db.ForeignKey('volunteer_needs.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('volunteer_matches.id'))
    assignment_status = db.Column(db.String(50), default='pending')  # pending, confirmed, completed, no_show
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)
    confirmed_at = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)
    actual_hours = db.Column(db.Float)
    show_up = db.Column(db.Boolean)  # NULL = unknown, True = yes, False = no_show
    nonprofit_confirmed = db.Column(db.Boolean, default=False)

    # Relationships
    feedbacks = db.relationship('Feedback', backref='assignment', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Assignment V{self.volunteer_id} N{self.need_id} Status:{self.assignment_status}>'


class Feedback(db.Model):
    """POST-ASSIGNMENT FEEDBACK: Learning for algorithm"""
    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'))
    from_role = db.Column(db.String(50))  # volunteer or nonprofit
    rating = db.Column(db.Integer)  # 1-5
    text = db.Column(db.Text)
    feedback_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Feedback A{self.assignment_id} {self.rating}/5>'
```

### Step 3: Create Alembic Migrations

**File:** `backend/alembic/versions/001_create_phase2_tables.py`

```python
"""Create Phase 2 MVP tables

Revision ID: 001
Revises: (depends on existing)
Create Date: 2025-11-03

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001'
down_revision = None  # Set to existing revision if needed
branch_labels = None
depends_on = None


def upgrade():
    # Create tables (SQL from ARCHITECTURE document)
    op.create_table('geographic_zones', ...)  # (see architecture doc for full SQL)
    # ... create all new tables


def downgrade():
    op.drop_table('geographic_zones')
    # ... drop all tables
```

**Command to Run:**

```bash
cd backend
alembic revision --autogenerate -m "create_phase2_tables"
alembic upgrade head
```

---

## 🧠 MATCHING ALGORITHM IMPLEMENTATION

### File: `backend/matching_algorithm.py` (New File)

```python
# matching_algorithm.py - Core AI matching logic

from datetime import datetime, timedelta
import json
from models import (
    Volunteer, VolunteerNeed, VolunteerMatch,
    Assignment, Feedback
)
from db import db


def calculate_skill_overlap(volunteer_skills, need_skills):
    """
    Calculate % overlap between volunteer skills and required skills

    Args:
        volunteer_skills: string like '["mentoring", "tech", "cooking"]'
        need_skills: string like '["mentoring", "spanish"]'

    Returns:
        float 0.0-1.0 (1.0 = perfect match)
    """
    try:
        v_skills = set(json.loads(volunteer_skills or '[]'))
        n_skills = set(json.loads(need_skills or '[]'))
    except:
        return 0.5  # If parse fails, neutral score

    if not n_skills:
        return 0.8  # No specific skills required = all volunteers qualify

    overlap = len(v_skills & n_skills)
    coverage = overlap / len(n_skills)

    return min(1.0, coverage + 0.1)  # Slight boost for any match


def check_availability_compatibility(volunteer_availability, need_date, need_time):
    """
    Check if volunteer's availability matches opportunity date/time

    Args:
        volunteer_availability: JSON like {
            "weekdays": [1,2,3,4,5],
            "weekends": [6,7],
            "hours": "mornings"
        }
        need_date: datetime
        need_time: time

    Returns:
        float 0.0-1.0
    """
    try:
        avail = json.loads(volunteer_availability or '{}')
    except:
        return 0.5

    # Simple check: is it a weekend or weekday volunteer likes?
    day_of_week = need_date.weekday() + 1  # 1-7

    if day_of_week <= 5:
        if 'weekdays' in avail and day_of_week in avail.get('weekdays', []):
            return 0.85
    else:
        if 'weekends' in avail and day_of_week in avail.get('weekends', []):
            return 0.85

    return 0.3  # Poor match


def calculate_proximity_score(volunteer_lat_lng, need_lat_lng, max_miles):
    """
    Calculate distance between volunteer and opportunity

    Args:
        volunteer_lat_lng: (lat, lng)
        need_lat_lng: (lat, lng)
        max_miles: max distance volunteer will travel

    Returns:
        float 0.0-1.0 (1.0 = at location)
    """
    # Simplified: use Manhattan distance for now
    # TODO: Replace with Haversine formula for real distances

    if not volunteer_lat_lng or not need_lat_lng:
        return 0.5  # No location data = neutral

    lat_dist = abs(volunteer_lat_lng[0] - need_lat_lng[0]) * 69  # degrees to miles
    lng_dist = abs(volunteer_lat_lng[1] - need_lat_lng[1]) * 69
    distance = (lat_dist ** 2 + lng_dist ** 2) ** 0.5

    if distance > max_miles:
        return 0.0  # Too far

    # Score decreases with distance
    score = 1.0 - (distance / max_miles)
    return max(0.0, score)


def calculate_match_score(volunteer, need):
    """
    MAIN ALGORITHM: Calculate match score 0.0-1.0

    Factors (Phase 2 MVP):
    - Skills: 30% weight
    - Availability: 30% weight
    - Proximity: 20% weight
    - Reliability: 20% weight

    Args:
        volunteer: Volunteer object
        need: VolunteerNeed object

    Returns:
        float 0.0-1.0, score breakdown
    """

    # FACTOR 1: SKILLS (30%)
    skills_score = calculate_skill_overlap(
        volunteer.skills,
        need.required_skills
    )

    # FACTOR 2: AVAILABILITY (30%)
    availability_score = check_availability_compatibility(
        volunteer.availability,
        need.preferred_date,
        need.preferred_time
    )

    # FACTOR 3: PROXIMITY (20%)
    # TODO: Get lat/lng from zone centers
    proximity_score = 0.7  # Placeholder

    # FACTOR 4: RELIABILITY (20%)
    reliability_score = volunteer.show_up_rate

    # WEIGHTED TOTAL
    total_score = (
        (skills_score * 0.30) +
        (availability_score * 0.30) +
        (proximity_score * 0.20) +
        (reliability_score * 0.20)
    )

    return {
        'total': min(1.0, max(0.0, total_score)),
        'skills': skills_score,
        'availability': availability_score,
        'proximity': proximity_score,
        'reliability': reliability_score
    }


def generate_matches_for_need(need_id, min_score=0.7):
    """
    For a new/updated need, calculate matches for all volunteers in zone

    Args:
        need_id: integer
        min_score: minimum score to suggest (default 0.7)

    Returns:
        list of matches created, ranked by score
    """

    need = VolunteerNeed.query.get(need_id)
    if not need:
        return []

    # Get all active volunteers in same zone
    zone_volunteers = Volunteer.query.filter(
        Volunteer.home_zone_id == need.location_id,
        Volunteer.is_active == True
    ).all()

    matches = []

    for volunteer in zone_volunteers:
        # Skip if already matched for this need
        existing = VolunteerMatch.query.filter(
            VolunteerMatch.volunteer_id == volunteer.id,
            VolunteerMatch.need_id == need_id
        ).first()

        if existing:
            continue

        # Calculate match score
        score_breakdown = calculate_match_score(volunteer, need)
        total_score = score_breakdown['total']

        if total_score >= min_score:
            # Create match in database
            match = VolunteerMatch(
                volunteer_id=volunteer.id,
                need_id=need_id,
                match_score=total_score,
                match_reasoning=json.dumps(score_breakdown),
                status='suggested'
            )
            db.session.add(match)
            matches.append((match, total_score))

    db.session.commit()

    # Sort by score
    matches.sort(key=lambda x: x[1], reverse=True)

    return [m[0] for m in matches]


def update_algorithm_from_feedback():
    """
    Learn from feedback: adjust weights based on show-up outcomes

    Phase 2 MVP: Simple version - just gather data
    Phase 3+: Use this for ML model training
    """

    # Get recent assignments with feedback
    week_ago = datetime.utcnow() - timedelta(days=7)

    assignments = Assignment.query.filter(
        Assignment.completed_at >= week_ago,
        Assignment.show_up.isnot(None)
    ).all()

    # Analyze: did high-scoring matches -> high show-up?
    correlations = []

    for assignment in assignments:
        match = VolunteerMatch.query.get(assignment.match_id)
        if not match:
            continue

        correlation = {
            'match_score': match.match_score,
            'showed_up': assignment.show_up,
            'feedback_score': None
        }

        # Get feedback if available
        feedback = Feedback.query.filter(
            Feedback.assignment_id == assignment.id
        ).first()

        if feedback:
            correlation['feedback_score'] = feedback.rating

        correlations.append(correlation)

    # TODO: Log these correlations for analysis
    # In Phase 3, use for ML model training

    return correlations
```

---

## 🔌 API ENDPOINTS (Phase 2 MVP)

### File: `backend/api_nonprofit.py` (New File)

```python
# api_nonprofit.py - Nonprofit dashboard endpoints

from flask import Blueprint, request, jsonify
from flask_jwt_required import jwt_required, get_jwt_identity
from models import (
    Nonprofit, VolunteerNeed, VolunteerMatch,
    Assignment, Feedback, Volunteer
)
from matching_algorithm import generate_matches_for_need, update_algorithm_from_feedback
from db import db
import json

nonprofit_api = Blueprint('nonprofit_api', __name__, url_prefix='/api/nonprofit')


@nonprofit_api.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard():
    """GET nonprofit dashboard data"""
    nonprofit_id = get_jwt_identity()
    nonprofit = Nonprofit.query.get(nonprofit_id)

    if not nonprofit:
        return jsonify({'error': 'Nonprofit not found'}), 404

    # Calculate metrics
    all_needs = VolunteerNeed.query.filter_by(nonprofit_id=nonprofit_id).all()
    all_assignments = Assignment.query.filter(
        Assignment.need_id.in_([n.id for n in all_needs])
    ).all()

    show_up_count = len([a for a in all_assignments if a.show_up == True])
    total_assignments = len([a for a in all_assignments if a.show_up is not None])
    show_up_rate = (show_up_count / total_assignments * 100) if total_assignments > 0 else 0

    return jsonify({
        'status': 'success',
        'data': {
            'nonprofit_name': nonprofit.name,
            'total_needs_posted': len(all_needs),
            'total_assignments': len(all_assignments),
            'show_up_rate': f"{show_up_rate:.1f}%",
            'satisfaction_score': 4.2,  # TODO: calculate from feedback
        }
    }), 200


@nonprofit_api.route('/needs', methods=['POST'])
@jwt_required()
def create_need():
    """POST - Create new volunteer need"""
    nonprofit_id = get_jwt_identity()
    data = request.get_json()

    need = VolunteerNeed(
        nonprofit_id=nonprofit_id,
        title=data['title'],
        description=data['description'],
        required_skills=json.dumps(data.get('skills', [])),
        location_id=data.get('location_id'),
        preferred_date=data.get('preferred_date'),
        estimated_hours=data.get('hours'),
        status='draft'
    )

    db.session.add(need)
    db.session.commit()

    return jsonify({
        'status': 'success',
        'data': {'need_id': need.id}
    }), 201


@nonprofit_api.route('/needs/<int:need_id>', methods=['GET'])
@jwt_required()
def get_need_details(need_id):
    """GET - Retrieve need + suggested volunteers"""
    nonprofit_id = get_jwt_identity()
    need = VolunteerNeed.query.get(need_id)

    if not need or need.nonprofit_id != nonprofit_id:
        return jsonify({'error': 'Not found'}), 404

    # Get all suggested matches
    matches = VolunteerMatch.query.filter_by(need_id=need_id).order_by(
        VolunteerMatch.match_score.desc()
    ).all()

    suggested_volunteers = []
    for match in matches[:5]:  # Top 5
        volunteer = Volunteer.query.get(match.volunteer_id)
        suggested_volunteers.append({
            'volunteer_id': volunteer.id,
            'name': f"{volunteer.first_name} {volunteer.last_name}",
            'match_score': match.match_score,
            'match_explanation': json.loads(match.match_reasoning),
            'skills': json.loads(volunteer.skills or '[]'),
            'show_up_history': volunteer.show_up_rate
        })

    return jsonify({
        'status': 'success',
        'data': {
            'need': {
                'id': need.id,
                'title': need.title,
                'description': need.description,
                'status': need.status,
                'date': str(need.preferred_date)
            },
            'suggested_volunteers': suggested_volunteers
        }
    }), 200


@nonprofit_api.route('/assignments/<int:assignment_id>/confirm-show-up', methods=['POST'])
@jwt_required()
def confirm_show_up(assignment_id):
    """POST - Nonprofit confirms volunteer showed up"""
    nonprofit_id = get_jwt_identity()
    data = request.get_json()

    assignment = Assignment.query.get(assignment_id)
    if not assignment:
        return jsonify({'error': 'Assignment not found'}), 404

    # Verify nonprofit owns this assignment
    need = VolunteerNeed.query.get(assignment.need_id)
    if need.nonprofit_id != nonprofit_id:
        return jsonify({'error': 'Unauthorized'}), 403

    # Record show-up
    assignment.show_up = data.get('showed_up', False)
    assignment.nonprofit_confirmed = True
    assignment.completed_at = datetime.utcnow()

    # Update volunteer statistics
    volunteer = Volunteer.query.get(assignment.volunteer_id)
    if data.get('showed_up'):
        volunteer.show_up_count += 1
    else:
        volunteer.no_show_count += 1

    db.session.commit()

    return jsonify({
        'status': 'success',
        'message': 'Show-up recorded'
    }), 200
```

### File: `backend/api_volunteer.py` (New File)

```python
# api_volunteer.py - Volunteer app endpoints

from flask import Blueprint, request, jsonify
from flask_jwt_required import jwt_required, get_jwt_identity
from models import (
    Volunteer, VolunteerNeed, VolunteerMatch,
    Assignment, Feedback, GeographicZone
)
from db import db
import json

volunteer_api = Blueprint('volunteer_api', __name__, url_prefix='/api/volunteer')


@volunteer_api.route('/zone/<int:zone_id>/needs', methods=['GET'])
@jwt_required()
def get_zone_needs(zone_id):
    """GET - List all opportunities in volunteer's zone"""
    volunteer_id = get_jwt_identity()
    volunteer = Volunteer.query.get(volunteer_id)

    # Get all active needs in this zone
    needs = VolunteerNeed.query.filter(
        VolunteerNeed.location_id == zone_id,
        VolunteerNeed.status == 'active'
    ).all()

    needs_data = []

    for need in needs:
        # Get this volunteer's match score for this need (or calculate if new)
        match = VolunteerMatch.query.filter(
            VolunteerMatch.volunteer_id == volunteer_id,
            VolunteerMatch.need_id == need.id
        ).first()

        if match:
            match_score = match.match_score
            match_explanation = json.loads(match.match_reasoning)
        else:
            match_score = None
            match_explanation = None

        nonprofit = Nonprofit.query.get(need.nonprofit_id)

        needs_data.append({
            'id': need.id,
            'nonprofit_name': nonprofit.name,
            'nonprofit_mission': nonprofit.mission,
            'title': need.title,
            'description': need.description,
            'date': str(need.preferred_date),
            'time': str(need.preferred_time),
            'hours': need.estimated_hours,
            'location': f"Zone {zone_id}",  # TODO: better location display
            'my_match_score': match_score,
            'match_explanation': match_explanation,
            'status': need.status
        })

    return jsonify({
        'status': 'success',
        'data': {
            'zone_id': zone_id,
            'needs': needs_data,
            'total_count': len(needs_data)
        }
    }), 200


@volunteer_api.route('/assignments', methods=['POST'])
@jwt_required()
def create_assignment():
    """POST - Volunteer expresses interest (creates assignment)"""
    volunteer_id = get_jwt_identity()
    data = request.get_json()

    need_id = data.get('need_id')
    need = VolunteerNeed.query.get(need_id)

    if not need:
        return jsonify({'error': 'Need not found'}), 404

    # Check for existing assignment
    existing = Assignment.query.filter(
        Assignment.volunteer_id == volunteer_id,
        Assignment.need_id == need_id
    ).first()

    if existing:
        return jsonify({'error': 'Already assigned'}), 400

    # Get match (if exists)
    match = VolunteerMatch.query.filter(
        VolunteerMatch.volunteer_id == volunteer_id,
        VolunteerMatch.need_id == need_id
    ).first()

    # Create assignment
    assignment = Assignment(
        volunteer_id=volunteer_id,
        need_id=need_id,
        match_id=match.id if match else None,
        assignment_status='pending'
    )

    db.session.add(assignment)
    db.session.commit()

    # Send notification to nonprofit (TODO: implement)

    return jsonify({
        'status': 'success',
        'data': {'assignment_id': assignment.id}
    }), 201


@volunteer_api.route('/assignments/<int:assignment_id>/feedback', methods=['POST'])
@jwt_required()
def submit_feedback(assignment_id):
    """POST - Volunteer submits feedback after assignment"""
    volunteer_id = get_jwt_identity()
    data = request.get_json()

    assignment = Assignment.query.get(assignment_id)

    if not assignment or assignment.volunteer_id != volunteer_id:
        return jsonify({'error': 'Not authorized'}), 403

    feedback = Feedback(
        assignment_id=assignment_id,
        from_role='volunteer',
        rating=data.get('rating'),
        text=data.get('text')
    )

    db.session.add(feedback)
    db.session.commit()

    return jsonify({
        'status': 'success',
        'message': 'Feedback recorded'
    }), 201
```

---

## 📋 WEEK 9-10 DEVELOPMENT TASKS

### Priority 1: Foundation (Must Complete Before Week 11)

- [ ] **Audit current schema** - What exists? Document in CURRENT-SCHEMA.md
- [ ] **Create models.py** - Add Phase 2 models (copy code above)
- [ ] **Create database migration** - Run alembic upgrade
- [ ] **Implement matching_algorithm.py** - Copy code above, test locally
- [ ] **Write algorithm unit tests** - 10+ test cases for match scoring
- [ ] **Integration test** - Create a test need, verify matches generated

### Priority 2: API Foundation (Week 10)

- [ ] **Create api_nonprofit.py** - Nonprofit endpoints (copy above)
- [ ] **Create api_volunteer.py** - Volunteer endpoints (copy above)
- [ ] **Wire API to Flask app.py** - Register blueprints
- [ ] **Write API integration tests** - Test all endpoints
- [ ] **Swagger/OpenAPI docs** - Document API for frontend team

### Success Criteria for Week 10

```
✅ Database schema in place (migration runs cleanly)
✅ Models defined (all 6 core models working)
✅ Matching algorithm implemented (70%+ unit test coverage)
✅ API endpoints functioning (Postman tests pass)
✅ Team can run 'python app.py' and test endpoints locally
```

---

## 📱 FRONTEND TASKS (Parallel Track)

### Nonprofit Dashboard (Frontend Team - Week 11-12)

**Files to Create:**

- `/frontend/src/pages/NonprofitDashboard.jsx` - Main dashboard
- `/frontend/src/components/NeedForm.jsx` - Create need form
- `/frontend/src/components/SuggestedVolunteersList.jsx` - Show matched volunteers
- `/frontend/src/components/ConfirmShowUp.jsx` - Record show-up

**Integration:**

- Fetch from `/api/nonprofit/dashboard`
- POST to `/api/nonprofit/needs`
- GET from `/api/nonprofit/needs/{id}` (with suggested volunteers)
- POST to `/api/nonprofit/assignments/{id}/confirm-show-up`

### Volunteer App (Frontend Team - Week 11-12)

**Files to Create:**

- `/frontend/src/pages/VolunteerBrowse.jsx` - Browse opportunities
- `/frontend/src/components/OpportunityCard.jsx` - Individual opportunity
- `/frontend/src/components/MatchScoreDisplay.jsx` - Show match score + explanation
- `/frontend/src/pages/MyAssignments.jsx` - Volunteer's commitments
- `/frontend/src/components/FeedbackForm.jsx` - Post-assignment feedback

**Integration:**

- GET from `/api/volunteer/zone/{id}/needs`
- POST to `/api/volunteer/assignments`
- GET from `/api/volunteer/assignments`
- POST to `/api/volunteer/assignments/{id}/feedback`

---

## ✅ GO/NO-GO GATE: END OF WEEK 10

**Questions to Answer:**

- ✅ Can we POST a new need and get suggested volunteers back?
- ✅ Do suggested matches have 0.7+ scores?
- ✅ Can a volunteer see opportunities in their zone?
- ✅ Can we create + confirm an assignment?
- ✅ Does show-up tracking update volunteer stats?
- ✅ Any critical bugs found? (All must be fixed before Week 11)

**If YES to all:** Proceed to Week 11 (Frontend + Pilot Prep)  
**If NO to any:** Extend Week 10, fix issues, reassess Monday

---

## 📚 NEXT HANDOFF DOCUMENT

Once Phase 2 MVP launches (Week 15), @qa will create:

- TEST-PLAN-PHASE-2.md (40+ test cases for pilot)
- PILOT-LAUNCH-CHECKLIST.md (ready to onboard nonprofits)
- METRICS-TRACKING-SHEET.md (daily show-up rate monitoring)

---

## 📝 REFERENCE

**Related Docs:**

- ARCHITECTURE-SYSTEM-DESIGN.md - Full system design
- BMAD-SOLUTION.md - Business model + strategy
- EXECUTION-ROADMAP-12-MONTH.md - Timeline + gates

---

**Status: ✅ READY FOR DEVELOPMENT HANDOFF**

_Technical Implementation Guide: November 3, 2025_  
_Next milestone: Week 9 Sprint Kickoff - Database + Algorithm Implementation_
