# Backend MVP (minimal)

Prereqs: Python 3.10+ recommended.

Create venv, install deps, run app (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
python backend/mvp_app.py
```

Open http://127.0.0.1:5000/api/health
Open http://127.0.0.1:5000/api/items

Run tests:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
pytest backend/tests -q
```

Database migrations (Alembic)

Initialize and run migrations (from repository root):

```powershell
# install alembic into your venv first (if not already):
.\.venv\Scripts\python.exe -m pip install alembic

# create the alembic version table and run the included initial migration
alembic -c alembic.ini upgrade head

# To autogenerate future migrations:
alembic -c alembic.ini revision --autogenerate -m "add changes"
alembic -c alembic.ini upgrade head
```

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
 - Recommended: copy `.env.sample` to `.env` for local development. The `backend` app will pick up env vars from the process environment.
 - Added refresh token support: register/login now return both `access_token` and `refresh_token`. Use POST `/refresh` with a refresh token in the Authorization header to obtain a new access token.
 - The app will automatically load a `.env` file from the repository root if `python-dotenv` is installed. Copy `.env.sample` to `.env` and edit values for local development.

Manage migrations locally

To run migrations from your virtualenv without calling alembic directly, use the included wrapper:

```powershell
.\.venv\Scripts\Activate.ps1
python backend/manage.py upgrade
```

This executes `alembic -c alembic.ini upgrade head` using the active Python interpreter so it works reliably inside your venv.

Configuration & secrets

See `backend/CONFIG.md` for a list of environment variables used by the backend, recommended local defaults, and CI secret guidance. This document shows example GitHub Actions snippets for injecting secrets into workflows.

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
