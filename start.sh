#!/bin/bash

echo "========================================"
echo "Starting Tapin Development Servers"
echo "========================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Node.js is available
if ! command -v npm &> /dev/null; then
    echo -e "${RED}ERROR: Node.js/npm not found!${NC}"
    echo "Please install Node.js from: https://nodejs.org/"
    echo "Or on macOS: brew install node"
    echo "Or on Ubuntu: sudo apt install nodejs npm"
    exit 1
fi

# Check if Python venv exists
if [ ! -f ".venv/bin/python" ]; then
    echo -e "${RED}ERROR: Python virtual environment not found!${NC}"
    echo "Please run: python3 -m venv .venv"
    exit 1
fi

# Check if frontend dependencies are installed
if [ ! -d "frontend/node_modules" ]; then
    echo -e "${YELLOW}Installing frontend dependencies...${NC}"
    cd frontend
    npm install
    cd ..
fi

echo ""
echo -e "${GREEN}Starting Backend Server (Flask)...${NC}"
# Start backend in background
.venv/bin/python backend/app.py &
BACKEND_PID=$!

# Wait for backend to start
sleep 3

echo -e "${GREEN}Starting Frontend Server (Vite)...${NC}"
# Start frontend in background
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

# Wait for frontend to start
sleep 5

echo ""
echo "========================================"
echo "Servers are running!"
echo "========================================"
echo -e "Backend:  ${GREEN}http://127.0.0.1:5000${NC}"
echo -e "Frontend: ${GREEN}http://localhost:5173${NC}"
echo "========================================"
echo ""
echo "Opening browser..."

# Open browser based on OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    open http://localhost:5173
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open http://localhost:5173 2>/dev/null || echo "Please open http://localhost:5173 in your browser"
fi

echo ""
echo -e "${YELLOW}Press Ctrl+C to stop all servers...${NC}"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "Stopping servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    # Kill any remaining node/python processes for our app
    pkill -f "vite.*5173" 2>/dev/null
    pkill -f "python.*backend/app.py" 2>/dev/null
    echo "Servers stopped."
    exit 0
}

# Trap Ctrl+C
trap cleanup INT TERM

# Wait forever (until Ctrl+C)
wait
