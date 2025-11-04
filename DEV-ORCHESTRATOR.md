# Tapin Dev Orchestrator

Single command local development runner for Tapin. Starts the Flask backend and Vite frontend together, prints their URLs, and installs missing dependencies automatically.

## Quick Start

- From `Tapin/` (this folder):
  - `npm run dev`
- You’ll see URLs printed like:
  - Backend: `http://127.0.0.1:5000`
  - Frontend: `http://127.0.0.1:5173`
- Stop with `Ctrl+C`.

## What It Does

- Picks a Python executable (`PYTHON` env, then `py`/`python`/`python3`).
- Backend preflight: attempts `import flask`; if missing runs `pip install -r backend/requirements.txt`.
- Frontend preflight: checks for Vite in `node_modules`; if missing runs `npm install` in `frontend/`.
- Spawns both processes with prefixed logs: `[backend] ...` and `[frontend] ...`.

## Requirements

- Node.js v20+ and npm
- Python 3.x with `pip`
- Windows users: having the Python Launcher (`py`) helps; otherwise set `PYTHON` to your Python path.

## Configuration

- Ports and hosts
  - Backend: `BACKEND_HOST` (default `127.0.0.1`), `BACKEND_PORT` (default `5000`)
  - Frontend: `FRONTEND_HOST` (default `127.0.0.1`), `FRONTEND_PORT` (default `5173`)
- Backend environment (`Tapin/backend/.env`)
  - Supports `HOST`, `PORT`, `SECRET_KEY`, `JWT_SECRET_KEY`, `SECURITY_PASSWORD_SALT`, `SMTP_*`
  - Example: `Tapin/backend/.env.example`
- Frontend API base
  - `Tapin/frontend/.env` → `VITE_API_BASE` (defaults to `http://127.0.0.1:5000`)
  - Example: `Tapin/frontend/.env.example`

## Examples

- Custom backend port and host (PowerShell):
  - `$env:BACKEND_HOST='0.0.0.0'; $env:BACKEND_PORT='5050'; npm run dev`
- Explicit Python path (PowerShell):
  - `$env:PYTHON='C:\\Python311\\python.exe'; npm run dev`

## Troubleshooting

- `ModuleNotFoundError: No module named 'flask'`
  - The orchestrator tries to install dependencies; if it fails, run:
    - `python -m pip install -r Tapin/backend/requirements.txt` (or use `$env:PYTHON` if needed)
- `'vite' is not recognized`
  - The orchestrator runs `npm install` in `Tapin/frontend`. If it fails, run manually:
    - `cd Tapin/frontend && npm install`
- `spawn ENOENT` / `command not found`
  - Ensure `npm`, `python`/`py` are on PATH. Or set `$env:PYTHON` to the full path on Windows.
- `spawn EINVAL` on Windows
  - The orchestrator uses `shell: true` for the npm command; open a new terminal and retry if it persists.

## File References

- Orchestrator script: `Tapin/dev.js`
- Package script: `Tapin/package.json: "dev": "node dev.js"`
- Backend app: `Tapin/backend/app.py` (reads `HOST`/`PORT` env)
- Frontend entry: `Tapin/frontend/src/main.jsx`, app config in `Tapin/frontend/src/config.js`

## Notes

- For isolation, you can manually create a Python virtual environment in `Tapin/backend` and activate it before running `npm run dev`. The orchestrator will still work inside the venv.
- Logs are prefixed to help distinguish output. Use your terminal’s split panes if you prefer running backend and frontend separately.

