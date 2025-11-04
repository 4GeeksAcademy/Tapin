# Backend (Flask)

This folder contains a small Flask API used for prototyping the Tapin backend.

Prerequisites

- Python 3.10+ recommended
- (Optional) virtualenv or venv

Quick start (zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/app.py
```

Environment variables

- `SECRET_KEY` — Flask secret (defaults to a dev value)
- `JWT_SECRET_KEY` — JWT secret (defaults to SECRET_KEY)
- `SECURITY_PASSWORD_SALT` — salt used for password reset tokens
- `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `SMTP_USE_TLS` — if you want the app to send real reset emails

Database

- By default the app uses SQLite at `backend/data.db` (created automatically).

Smoke tests

- Register: POST /register {email, password}
- Login: POST /login {email, password}
- Get listings: GET /listings
- Create listing (requires JWT): POST /listings with Authorization: Bearer <token>

Notes

- This is a development prototype. For production, switch to a proper RDBMS, secure secrets, and use stronger password hashing (bcrypt/passlib).

# Tapin Backend

This directory will contain the Flask backend for the Tapin project.

## Setup

1. Initialize a Python virtual environment.
2. Install Flask and other dependencies.
3. Implement API endpoints as described in the project documentation.

## .env support

This app loads environment variables from a `.env` file in `backend/` using python-dotenv.

Example `.env`:

```
SECRET_KEY=change-me
JWT_SECRET_KEY=change-me-too
SECURITY_PASSWORD_SALT=some-salt
SMTP_HOST=
SMTP_PORT=587
SMTP_USER=
SMTP_PASS=
SMTP_USE_TLS=true
```
