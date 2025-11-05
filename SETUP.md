# Tapin Development Setup

## Quick Start (Backend Only)

The backend is already running! Access it at:
- **API Root**: http://127.0.0.1:5000
- **Health Check**: http://127.0.0.1:5000/api/health
- **API Docs**: See backend/API_DOCS.md

## Frontend Setup Required

The frontend uses React + Vite and requires Node.js.

### Install Node.js

1. Download Node.js LTS from: https://nodejs.org/
   - Recommended: v20.x LTS or v18.x LTS
   - Run the installer and follow the prompts
   - ✅ Check "Add to PATH" option during installation

2. Verify installation (open new terminal):
   ```powershell
   node --version
   npm --version
   ```

3. Install frontend dependencies:
   ```powershell
   cd "c:\Users\User\Dropbox\My PC (DESKTOP-0CG7P59)\Documents\GitHub\Tapin\frontend"
   npm install
   ```

4. Start the frontend dev server:
   ```powershell
   npm run dev
   ```

5. Open http://localhost:5173 in your browser

## Running Both Servers

### Option 1: Two separate terminals

**Terminal 1 - Backend:**
```powershell
cd "c:\Users\User\Dropbox\My PC (DESKTOP-0CG7P59)\Documents\GitHub\Tapin"
.\.venv\Scripts\Activate.ps1
python backend/app.py
```

**Terminal 2 - Frontend:**
```powershell
cd "c:\Users\User\Dropbox\My PC (DESKTOP-0CG7P59)\Documents\GitHub\Tapin\frontend"
npm run dev
```

### Option 2: Using the start script (after Node.js is installed)

```powershell
cd "c:\Users\User\Dropbox\My PC (DESKTOP-0CG7P59)\Documents\GitHub\Tapin"
# Set execution policy if needed:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\start-dev.ps1
```

## What's Running Now

✅ **Backend**: http://127.0.0.1:5000 (Flask API)
❌ **Frontend**: Waiting for Node.js installation

## Testing the Backend Without Frontend

You can test the API endpoints using:
- Browser: http://127.0.0.1:5000/api/health
- PowerShell:
  ```powershell
  Invoke-WebRequest -Uri http://127.0.0.1:5000/api/health | Select-Object -ExpandProperty Content
  ```
- Postman, Insomnia, or curl

## Next Steps After Node.js Installation

1. Run `npm install` in the frontend directory
2. Run `npm run dev` to start the frontend
3. Open http://localhost:5173
4. The frontend will automatically connect to the backend at http://127.0.0.1:5000
