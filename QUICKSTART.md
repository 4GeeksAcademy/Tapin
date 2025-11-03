# Tapin Quick Start Guide

This guide will help you get both the backend and frontend running quickly.

## Prerequisites

- **Python 3.10+** (for backend)
- **Node.js 20+** (for frontend)
- **Git** (to clone the repository)

## Running the Backend (Flask API)

1. **Navigate to the backend directory:**

   ```bash
   cd backend
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**

   ```bash
   python manage.py upgrade
   ```

5. **Seed sample data (optional):**

   ```bash
   python seed_sample_data.py
   ```

6. **Start the Flask server:**
   ```bash
   python app.py
   ```

The backend API will be available at **http://127.0.0.1:5000**

### Test the Backend

Open in your browser:

- Health check: http://127.0.0.1:5000/api/health
- Listings: http://127.0.0.1:5000/api/listings

## Running the Frontend (React + Vite)

1. **Open a new terminal** and navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

The frontend will be available at **http://localhost:5173**

## Running Both Simultaneously

You can run both the backend and frontend at the same time by opening two separate terminal windows:

**Terminal 1 (Backend):**

```bash
cd backend
source .venv/bin/activate
python app.py
```

**Terminal 2 (Frontend):**

```bash
cd frontend
npm run dev
```

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
