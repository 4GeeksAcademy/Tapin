#!/usr/bin/env pwsh
# Start both backend and frontend dev servers

Write-Host "Starting Tapin development servers..." -ForegroundColor Green

# Start backend in background
Write-Host "`nStarting backend on http://localhost:5000..." -ForegroundColor Cyan
$backendJob = Start-Job -ScriptBlock {
    Set-Location "c:\Users\User\Dropbox\My PC (DESKTOP-0CG7P59)\Documents\GitHub\Tapin"
    & .\.venv\Scripts\Activate.ps1
    python backend/app.py
}

# Wait a moment for backend to start
Start-Sleep -Seconds 2

# Start frontend in foreground
Write-Host "Starting frontend on http://localhost:5173..." -ForegroundColor Cyan
Write-Host "`nPress Ctrl+C to stop both servers`n" -ForegroundColor Yellow

try {
    Set-Location "c:\Users\User\Dropbox\My PC (DESKTOP-0CG7P59)\Documents\GitHub\Tapin\frontend"
    npm run dev
} finally {
    # Clean up backend job when frontend exits
    Write-Host "`nStopping servers..." -ForegroundColor Yellow
    Stop-Job -Job $backendJob
    Remove-Job -Job $backendJob
    Write-Host "Servers stopped." -ForegroundColor Green
}
