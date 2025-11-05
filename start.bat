@echo off
echo ========================================
echo Starting Tapin Development Servers
echo ========================================
echo.

REM Set Node.js path
set PATH=%PATH%;C:\Program Files\nodejs

REM Check if Node.js is available
where npm >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Node.js/npm not found!
    echo Please install Node.js from: https://nodejs.org/
    echo Or run: winget install OpenJS.NodeJS.LTS
    pause
    exit /b 1
)

REM Check if Python venv exists
if not exist ".venv\Scripts\python.exe" (
    echo ERROR: Python virtual environment not found!
    echo Please run: python -m venv .venv
    pause
    exit /b 1
)

REM Check if frontend dependencies are installed
if not exist "frontend\node_modules" (
    echo Installing frontend dependencies...
    cd frontend
    call npm install
    cd ..
)

echo.
echo Starting Backend Server (Flask)...
start "Tapin Backend" cmd /k ".venv\Scripts\python.exe backend/app.py"

REM Wait for backend to start
timeout /t 3 /nobreak >nul

echo Starting Frontend Server (Vite)...
start "Tapin Frontend" cmd /k "cd frontend && npm run dev"

REM Wait for frontend to start
timeout /t 5 /nobreak >nul

echo.
echo ========================================
echo Servers are starting!
echo ========================================
echo Backend:  http://127.0.0.1:5000
echo Frontend: http://localhost:5173
echo ========================================
echo.
echo Opening browser...
start http://localhost:5173

echo.
echo Press any key to stop all servers...
pause >nul

REM Kill the server windows
taskkill /FI "WindowTitle eq Tapin Backend*" /T /F >nul 2>&1
taskkill /FI "WindowTitle eq Tapin Frontend*" /T /F >nul 2>&1

echo Servers stopped.
