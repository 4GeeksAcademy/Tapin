# Tapin Quick Start Guide

Get the Tapin volunteer platform running in minutes!

## 🚀 Quick Start (Choose Your Platform)

### Windows (One Command)

Simply double-click `start.bat` or run:
```cmd
start.bat
```

This automatically:
- Checks dependencies
- Installs packages
- Starts both servers
- Opens your browser

### macOS/Linux

Run the startup script:
```bash
chmod +x start.sh
./start.sh
```

### GitHub Codespaces

Click the green "Code" button → "Codespaces" → "Create codespace on main"

The environment will auto-configure and forward ports. Click the "Ports" tab and open the Frontend port (5173).

---

## 📋 Prerequisites

Install these before starting:

### Windows
```powershell
# Install Python
winget install Python.Python.3.11

# Install Node.js
winget install OpenJS.NodeJS.LTS
```

### macOS
```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python and Node.js
brew install python@3.11 node
```

### Linux (Ubuntu/Debian)
```bash
# Install Python and Node.js
sudo apt update
sudo apt install python3.11 python3-pip nodejs npm
```

---

## 🛠️ Manual Setup

If automated scripts don't work, follow these platform-specific instructions:

### Windows

**Terminal 1 - Backend:**
```powershell
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r backend\requirements.txt

# Run migrations
python backend\manage.py upgrade

# Start server
python backend\app.py
```

**Terminal 2 - Frontend:**
```powershell
# Install dependencies
cd frontend
npm install

# Start dev server
npm run dev
```

### macOS/Linux

**Terminal 1 - Backend:**
```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt

# Run migrations
python backend/manage.py upgrade

# Start server
python backend/app.py
```

**Terminal 2 - Frontend:**
```bash
# Install dependencies
cd frontend
npm install

# Start dev server
npm run dev
```

### GitHub Codespaces

Codespaces auto-installs everything. Just run:
```bash
# Terminal 1
python backend/app.py

# Terminal 2
cd frontend && npm run dev
```

---

## 🌐 Access the Application

Once running:
- **Frontend**: http://localhost:5173
- **Backend API**: http://127.0.0.1:5000
- **Health Check**: http://127.0.0.1:5000/api/health

## Environment Variables (Optional)

For local development, you can create a `.env` file in the repository root:

```env
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
SECURITY_PASSWORD_SALT=your-salt
SQLALCHEMY_DATABASE_URI=sqlite:///backend/data.db
```

See `backend/CONFIG.md` for more details on configuration options.

## Running Tests

### Backend Tests

```bash
cd backend
source .venv/bin/activate
pytest tests/
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Troubleshooting

### Backend Issues

- **Database errors**: Run `python manage.py upgrade` to ensure migrations are applied
- **Module not found**: Ensure virtual environment is activated and dependencies are installed
- **Port already in use**: Change the port in `app.py` or stop the conflicting process

### Frontend Issues

- **Module not found**: Delete `node_modules` and run `npm install` again
- **Port already in use**: Vite will automatically try the next available port

## Next Steps

- Review the [Backend README](backend/README.md) for API documentation
- Review the [Frontend README](frontend/README.md) for frontend architecture
- Check [API_DOCS.md](backend/API_DOCS.md) for endpoint details
- Explore the BMad agent framework in `.bmad-core/`
