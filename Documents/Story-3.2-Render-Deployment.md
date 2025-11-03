# Render Deployment Guide (FREE Tier)

**Perfect for school projects, portfolios, and demos**

---

## 🆓 Why Render for School Projects?

- **100% Free** - No credit card required
- **Auto-deploy** from GitHub (push to deploy)
- **Free PostgreSQL** database (90 days, renewable)
- **Free SSL** certificates (HTTPS automatic)
- **No cold starts** for web services (with caveats)

**Trade-off:** Free tier spins down after 15 minutes of inactivity (30-60 second cold start on next request)

---

## 📋 Prerequisites

- ✅ GitHub account with Tapin repository
- ✅ Render account (sign up free at [render.com](https://render.com))
- ✅ Story 3.1 completed (map integration)

---

## Part 1: Deploy Backend (Flask API)

### Step 1.1: Create Render Account

1. Go to [render.com](https://render.com)
2. Click "Get Started for Free"
3. Sign up with GitHub (recommended for auto-deploy)
4. Authorize Render to access your repositories

### Step 1.2: Create PostgreSQL Database

1. From Render dashboard, click **"New +"** → **"PostgreSQL"**
2. Configure database:
   - **Name:** `tapin-db`
   - **Database:** `tapin` (auto-filled)
   - **User:** `tapin` (auto-filled)
   - **Region:** Choose closest to you
   - **Plan:** **Free** (select this!)
3. Click **"Create Database"**
4. ⚠️ **Important:** Save the **Internal Database URL** (starts with `postgresql://`)
   - Copy from "Connections" section
   - You'll need this for backend service

**Note:** Free PostgreSQL expires after 90 days. After expiration, create a new one and re-deploy.

### Step 1.3: Create Backend Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository: `4GeeksAcademy/Tapin`
3. Configure service:
   - **Name:** `tapin-backend`
   - **Region:** Same as database
   - **Branch:** `main`
   - **Root Directory:** `backend`
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`
4. Click **"Advanced"** to set environment variables

### Step 1.4: Configure Backend Environment Variables

Add these in the "Environment Variables" section:

```env
# Database (paste the Internal Database URL from Step 1.2)
DATABASE_URL=<your-postgresql-internal-url>

# Flask Configuration
FLASK_ENV=production
FLASK_APP=app.py

# Security - GENERATE NEW VALUES!
SECRET_KEY=<generate-with-command-below>
JWT_SECRET_KEY=<generate-with-command-below>
SECURITY_PASSWORD_SALT=<generate-with-command-below>

# CORS - Update after frontend deployed
CORS_ORIGINS=https://tapin-frontend.onrender.com

# Port (Render provides this automatically)
PORT=10000
```

**Generate Secure Keys Locally:**

```bash
# Run these commands on your machine:
python3 -c "import secrets; print(secrets.token_hex(32))"  # SECRET_KEY
python3 -c "import secrets; print(secrets.token_hex(32))"  # JWT_SECRET_KEY
python3 -c "import secrets; print(secrets.token_hex(16))"  # SECURITY_PASSWORD_SALT
```

5. Click **"Create Web Service"**
6. Wait for build to complete (~3-5 minutes)
7. ✅ Backend will be live at: `https://tapin-backend.onrender.com`

### Step 1.5: Initialize Database

After first deploy, run migration:

1. Go to backend service → **"Shell"** tab
2. Run:
   ```bash
   python -c "from app import app, db; app.app_context().push(); db.create_all(); print('✅ Database initialized')"
   ```
3. Verify tables created successfully

---

## Part 2: Deploy Frontend (React/Vite)

### Step 2.1: Create Frontend Static Site

1. Click **"New +"** → **"Static Site"**
2. Select your repository: `4GeeksAcademy/Tapin`
3. Configure service:
   - **Name:** `tapin-frontend`
   - **Branch:** `main`
   - **Root Directory:** `frontend`
   - **Build Command:** `npm install && npm run build`
   - **Publish Directory:** `dist`

### Step 2.2: Configure Frontend Environment Variables

Add in "Environment Variables":

```env
# API URL - Use your backend URL from Step 1.3
VITE_API_URL=https://tapin-backend.onrender.com

# Build
NODE_ENV=production
```

4. Click **"Create Static Site"**
5. Wait for build (~2-3 minutes)
6. ✅ Frontend will be live at: `https://tapin-frontend.onrender.com`

### Step 2.3: Update CORS Settings

Now that frontend is deployed:

1. Go back to **backend service** → **"Environment"** tab
2. Update `CORS_ORIGINS` to include your frontend URL:
   ```env
   CORS_ORIGINS=https://tapin-frontend.onrender.com
   ```
3. Save changes (backend will auto-redeploy)

---

## Part 3: Verify Deployment

### Test Backend Health

```bash
curl https://tapin-backend.onrender.com/api/health
# Expected: {"status":"ok"}
```

### Test Full Application

1. Open `https://tapin-frontend.onrender.com` in browser
2. ✅ Register new user
3. ✅ Login
4. ✅ Create listing with coordinates
5. ✅ Toggle to map view
6. ✅ Verify markers display correctly
7. ✅ Test all CRUD operations

---

## Part 4: Auto-Deploy Setup

### Enable Auto-Deploy from GitHub

Both services are already configured for auto-deploy:

1. Push code to `main` branch
2. Render automatically detects changes
3. Rebuilds and deploys (3-5 minutes)

**Test Auto-Deploy:**

```bash
# Make a small change
echo "# Updated $(date)" >> README.md
git add README.md
git commit -m "Test auto-deploy"
git push origin main

# Watch deployment in Render dashboard
```

---

## 🚨 Free Tier Limitations

### What to Expect

1. **Services spin down** after 15 min inactivity
   - First request after inactivity: 30-60 second delay
   - Subsequent requests: Normal speed
2. **PostgreSQL expires** after 90 days
   - Export data before expiration
   - Create new database and update `DATABASE_URL`
3. **Build minutes** limited to 500/month
   - More than enough for school projects
4. **No custom domains** on free tier
   - URLs: `*.onrender.com`
   - Upgrade to paid if needed later

### Keeping Services "Warm" (Optional)

For demos, keep backend awake:

```bash
# Use a cron job service like cron-job.org
# Ping every 10 minutes:
curl https://tapin-backend.onrender.com/api/health
```

Or use [UptimeRobot](https://uptimerobot.com) (free tier):

- Add your backend URL
- Check interval: 5 minutes
- Prevents cold starts during demos

---

## 📊 Troubleshooting

### Build Fails

**Backend build error:**

```bash
# Check requirements.txt syntax
# Ensure all dependencies listed
# Verify Python 3.9+ compatible
```

**Frontend build error:**

```bash
# Verify package.json scripts
# Check for environment variable issues
# Ensure VITE_API_URL is set
```

### Database Connection Error

```bash
# Verify DATABASE_URL is correct (Internal URL, not External)
# Check database is running (green dot in dashboard)
# Ensure psycopg2-binary in requirements.txt
```

### CORS Errors

```bash
# Update backend CORS_ORIGINS with exact frontend URL
# Include protocol: https://
# No trailing slash
# Save and wait for backend to redeploy
```

### Cold Start Issues

```bash
# Expected behavior on free tier
# First request after 15 min: slow
# Set up UptimeRobot to keep warm
# Or mention in demo: "cold start expected"
```

---

## 💡 Best Practices for School Projects

### 1. Database Backups

```bash
# Export data before 90-day expiration
pg_dump <your-database-url> > backup.sql

# Or use Render dashboard: Database → Backups
```

### 2. Environment Variables

- ✅ Never commit secrets to Git
- ✅ Use strong random values
- ✅ Document required vars in README

### 3. Demo Preparation

- ✅ Test app day before demo
- ✅ Wake up services 5 minutes before presenting
- ✅ Have backup local demo ready
- ✅ Prepare screen recording as fallback

### 4. Documentation

- ✅ Add deployment URLs to README
- ✅ Document API endpoints
- ✅ Include screenshots in portfolio

---

## 📁 Project Structure Summary

```
Tapin/
├── backend/
│   ├── app.py              # Flask app
│   ├── requirements.txt    # Dependencies (psycopg2, gunicorn)
│   └── ...
├── frontend/
│   ├── src/
│   ├── package.json        # Build scripts
│   ├── vite.config.js
│   └── ...
├── Documents/
│   ├── Story-3.2-Render-Deployment.md  # This file
│   └── ...
└── README.md
```

---

## 🔗 Quick Reference URLs

| Service          | URL Pattern                           |
| ---------------- | ------------------------------------- |
| Backend          | `https://tapin-backend.onrender.com`  |
| Frontend         | `https://tapin-frontend.onrender.com` |
| Database         | `postgresql://...` (internal)         |
| Render Dashboard | `https://dashboard.render.com`        |

---

## ✅ Deployment Checklist

### Pre-Deployment

- [x] Code tested locally
- [x] All dependencies in requirements.txt
- [x] Frontend env var support added

### Render Setup

- [ ] Create Render account
- [ ] Create PostgreSQL database
- [ ] Deploy backend service
- [ ] Deploy frontend static site
- [ ] Update CORS settings
- [ ] Initialize database

### Verification

- [ ] Backend health check passes
- [ ] Frontend loads in browser
- [ ] User registration works
- [ ] Login works
- [ ] Create/edit listings
- [ ] Map view displays
- [ ] All CRUD operations functional

---

## 🎯 Next Steps After Deployment

1. **Add deployment URLs to README**
2. **Test all features end-to-end**
3. **Set up UptimeRobot** (optional, keeps services warm)
4. **Take screenshots for portfolio**
5. **Prepare demo script for presentation**

---

## 🆘 Need Help?

- **Render Docs:** https://render.com/docs
- **Render Community:** https://community.render.com
- **Flask Deployment:** https://flask.palletsprojects.com/deploying/
- **Vite Production:** https://vitejs.dev/guide/build.html

---

**Total Setup Time:** ~20 minutes  
**Cost:** $0/month (FREE!)  
**Perfect for:** School projects, portfolios, demos

---

**Last Updated:** November 3, 2025  
**Prepared by:** @qa
