# Sprint 3 Architecture & Infrastructure Design

**Date:** November 3, 2025  
**Agent:** @architect  
**Sprint:** 3 - Map Integration & Deployment  
**Updated:** November 3, 2025 (Changed to free deployment options)

---

## Executive Summary

This document provides architectural recommendations for Sprint 3, covering map integration and deployment options. All recommendations prioritize **zero cost** for school projects, simplicity, and alignment with the current tech stack (Flask + React/Vite + SQLite dev).

**Key Changes:**

- ✅ Map integration: Leaflet + OpenStreetMap (FREE)
- ✅ Deployment option 1: Render free tier (recommended for live demos)
- ✅ Deployment option 2: Local demo with screen recording (recommended for submissions)
- ❌ Removed: Railway ($15/month) - overkill for school projects

---

## Current System Review

### Tech Stack (Sprints 1 & 2)

**Backend:**

- Flask 2.2+ with SQLAlchemy 3.0
- JWT authentication (Flask-JWT-Extended 4.4)
- SQLite (development)
- pytest for testing

**Frontend:**

- React 18.2 + Vite 5.0
- No router (single page app with modals)
- Vitest + React Testing Library

**Deployment Status:**

- ✅ Development: localhost:5173 (frontend) + localhost:5000 (backend)
- ❌ Production: Not deployed
- ❌ CI/CD: Not configured

### Features Implemented

- User authentication (register, login, password reset)
- Listing CRUD with ownership verification
- Sign-up/volunteer connection system
- Reviews and ratings (1-5 stars)
- Comprehensive test suites (32 backend tests, 10+ frontend tests)

---

## Story 3.1: Map Provider Recommendation

### Requirements Analysis

- Display listings on interactive map
- Click pins to show listing previews
- Toggle between list and map view
- Filter by map bounds (optional geofencing)
- Need geocoding for addresses (future)

### Option Comparison

#### ✅ **RECOMMENDED: Leaflet + OpenStreetMap**

**Pros:**

- 100% free, no API keys or usage limits
- Open source with MIT license
- Lightweight (38kb gzipped)
- Easy React integration (`react-leaflet`)
- Great mobile support
- No vendor lock-in
- Community-driven, stable, mature

**Cons:**

- Need separate geocoding service (Nominatim is free but rate-limited)
- Less polished UI than Google Maps
- Fewer built-in features

**Cost:** $0/month forever

**Integration Complexity:** Low

- Install: `npm install leaflet react-leaflet`
- Component: `<MapContainer>` with `<Marker>` components
- Styling: Include Leaflet CSS
- Time estimate: 4-6 hours

**Example Implementation:**

```jsx
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';

<MapContainer center={[51.505, -0.09]} zoom={13}>
  <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
  {listings.map((listing) => (
    <Marker key={listing.id} position={[listing.lat, listing.lng]}>
      <Popup>{listing.title}</Popup>
    </Marker>
  ))}
</MapContainer>;
```

#### ❌ Google Maps

**Pros:**

- Best-in-class UI/UX
- Comprehensive features
- Excellent geocoding

**Cons:**

- Requires billing account (even for free tier)
- $200/month free credit, then $7 per 1000 map loads
- Complex setup and API key management
- Vendor lock-in

**Cost:** $0-$100+/month depending on usage

**Recommendation:** Overkill for MVP, save for later if needed

#### ❌ Mapbox

**Pros:**

- Beautiful styling options
- Good React integration
- Better than Google for customization

**Cons:**

- Requires API key
- 50,000 free loads/month, then $5 per 1000
- More complex than Leaflet

**Cost:** $0-$50+/month

**Recommendation:** Good middle ground, but Leaflet is simpler for MVP

### 🎯 Final Recommendation: **Leaflet + OpenStreetMap**

**Rationale:**

1. **Zero cost** - Critical for early-stage MVP
2. **Simple integration** - Well-documented React library
3. **No API key hassles** - No registration, rate limits, billing setup
4. **Sufficient features** - Covers all Story 3.1 requirements
5. **Future-proof** - Can migrate to paid solution later if needed

**Geocoding Strategy:**

- **Now:** Users manually enter lat/lng or use location field text search
- **Later:** Integrate Nominatim (free, rate-limited) or paid service (Google Geocoding, Mapbox)

---

## Story 3.2: Production Infrastructure Design

### Hosting Platform Evaluation

#### ✅ **RECOMMENDED: Railway**

**Why Railway:**

- **Simplicity:** Deploy from GitHub in 5 minutes
- **Pricing:** $5/month per service (predictable)
- **PostgreSQL:** Built-in managed database ($5/month)
- **Environment management:** Easy staging/production splits
- **Zero config:** Detects Flask/Node.js automatically
- **SSL/HTTPS:** Automatic
- **Monitoring:** Built-in logs and metrics
- **Developer experience:** Excellent CLI and dashboard

**Cost Estimate:**

- Backend service: $5/month
- Frontend service: $5/month
- PostgreSQL database: $5/month
- **Total: $15/month**

**Pros:**

- No credit card required for trial
- Free $5 credit for new users
- Simple pricing, no surprises
- Great for Python + React
- Built-in CI/CD

**Cons:**

- Newer platform (less mature than Heroku)
- Smaller community
- Limited free tier (500 hours/month)

## Story 3.2: Deployment Strategy (FREE Options)

### Requirements

- ✅ Zero or minimal cost (school project budget)
- ✅ Easy deployment and updates
- ✅ Support for Flask backend + React frontend
- ✅ PostgreSQL or SQLite database
- ✅ HTTPS/SSL (for security)
- ✅ Suitable for demos and portfolio

---

### 🆓 Option 1: Render (FREE Tier) - **RECOMMENDED FOR LIVE DEMOS**

#### Overview

Render provides a generous free tier perfect for school projects and portfolios.

**Pros:**

- 100% free (no credit card required)
- Auto-deploy from GitHub (push to deploy)
- Free PostgreSQL database (90 days, renewable)
- Free SSL certificates (HTTPS automatic)
- Static site hosting (frontend)
- Web service hosting (backend)

**Cons:**

- Services spin down after 15 min inactivity (30-60s cold start)
- PostgreSQL expires after 90 days (must renew)
- 750 hours/month execution time limit
- Slower than paid services

**Cost:** $0/month

**Setup Time:** ~20 minutes

**Best For:**

- Live demos with shareable URL
- Portfolio projects
- School project presentations
- Testing deployment workflows

#### Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Render Platform (FREE)              │
│                                                      │
│  ┌────────────────┐         ┌──────────────────┐   │
│  │ Static Site    │         │ Web Service      │   │
│  │ (React/Vite)   │◄───────►│ (Flask/Python)   │   │
│  │ Frontend       │         │ Backend          │   │
│  └────────────────┘         └──────────────────┘   │
│                                      │              │
│                                      ▼              │
│                             ┌──────────────────┐   │
│                             │ PostgreSQL       │   │
│                             │ (Free 90 days)   │   │
│                             └──────────────────┘   │
└─────────────────────────────────────────────────────┘
           │
           ▼
    ┌─────────────┐
    │   GitHub    │
    │ Auto-deploy │
    └─────────────┘
```

**Deployment Guide:** See `/Documents/Story-3.2-Render-Deployment.md`

---

### 🖥️ Option 2: Local Demo + Screen Recording - **RECOMMENDED FOR SUBMISSIONS**

#### Overview

Run the application locally and create a professional screen recording for submission.

**Pros:**

- Zero cost (completely free)
- Full control (no cold starts or downtime)
- Easy debugging (see all logs)
- Instant setup (2 minutes)
- Perfect quality (no network issues)
- No deployment complexity

**Cons:**

- Not publicly accessible
- Requires video editing skills
- Need to run servers for live demos

**Cost:** $0

**Setup Time:** 2 minutes (after dependencies installed)

**Best For:**

- Video submissions
- Assignment demonstrations
- Quick testing
- Development workflow
- Offline presentations

#### Setup

```bash
# Terminal 1: Backend
cd backend
source .venv/bin/activate
python app.py

# Terminal 2: Frontend
cd frontend
npm run dev

# Open browser: http://localhost:5173
```

**Demo Guide:** See `/Documents/Local-Demo-Guide.md`

---

### 📊 Deployment Options Comparison

| Feature            | Render (Free)    | Local Demo  | Railway ❌       |
| ------------------ | ---------------- | ----------- | ---------------- |
| **Cost**           | $0/month         | $0          | $15/month        |
| **Setup Time**     | 20 min           | 2 min       | 15 min           |
| **Public URL**     | ✅ Yes           | ❌ No       | ✅ Yes           |
| **SSL/HTTPS**      | ✅ Auto          | N/A         | ✅ Auto          |
| **Database**       | PostgreSQL (90d) | SQLite      | PostgreSQL       |
| **Cold Starts**    | 30-60s           | None        | None             |
| **Auto-Deploy**    | ✅ GitHub        | N/A         | ✅ GitHub        |
| **Best For**       | Live demos       | Submissions | Production       |
| **Recommendation** | ⭐ Yes           | ⭐⭐ Yes    | ❌ Too expensive |

---

### 🎯 Final Recommendation

**For School Projects:**

1. **Primary:** Local demo + screen recording
   - Zero cost
   - Perfect quality
   - Easy to set up
   - Submit video to instructor

2. **Secondary:** Render free tier
   - If you need a live URL
   - For portfolio/resume
   - For peer testing
   - Keep in mind: cold starts

**Avoid for school:**

- Railway ($15/month) - unnecessary expense
- Heroku ($23/month) - too expensive
- AWS/GCP - too complex for MVP

---

### Alternative: Fly.io (If You Want to Explore Later)

**Note:** User mentioned Fly.io as potential alternative to Railway.

**Pros:**

- More generous free tier than Render
- Better performance
- Global edge network

**Cons:**

- Credit card required (even for free tier)
- More complex setup
- Less beginner-friendly

**Cost:** $0-$5/month

**Recommendation:** Good option if Render doesn't meet needs, but adds complexity.

---

### Production Architecture (Render Free Tier)

````
┌─────────────────────────────────────────────────────┐

```env
# Backend (Railway)
FLASK_ENV=production
SECRET_KEY=<strong-random-key>
JWT_SECRET_KEY=<strong-random-jwt-key>
SECURITY_PASSWORD_SALT=<strong-random-salt>
DATABASE_URL=<railway-postgresql-url>  # Auto-provided by Railway
CORS_ORIGINS=https://tapin.app
PORT=5000

# Email (Optional - for password reset)
SMTP_HOST=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USER=apikey
SMTP_PASS=<sendgrid-api-key>

# Monitoring (Optional)
SENTRY_DSN=<sentry-project-dsn>
````

**Frontend (Railway):**

```env
VITE_API_URL=https://tapin-backend.up.railway.app
NODE_ENV=production
```

### Database Migration Strategy

**From SQLite (dev) to PostgreSQL (prod):**

1. **Install PostgreSQL adapter:**

   ```bash
   pip install psycopg2-binary
   ```

2. **Update connection string in production:**
   - Railway auto-provides `DATABASE_URL`
   - SQLAlchemy handles PostgreSQL automatically
   - No code changes needed!

3. **Run migrations on first deploy:**

   ```bash
   alembic upgrade head
   ```

4. **Seed initial data (optional):**
   ```bash
   python seed_sample_data.py
   ```

**Migration Checklist:**

- [ ] Install `psycopg2-binary` in requirements.txt
- [ ] Test migrations locally with PostgreSQL
- [ ] Backup current SQLite data (if needed)
- [ ] Run `alembic upgrade head` in production
- [ ] Verify all tables created
- [ ] Test CRUD operations

---

## Story 3.3: CI/CD Pipeline Design

### GitHub Actions Workflow Strategy

**Goals:**

1. Run tests on every push
2. Block merge if tests fail
3. Auto-deploy to Railway on merge to main
4. Support staging environment

### Proposed Workflows

#### 1. **Test Workflow** (runs on every PR and push)

**File:** `.github/workflows/test.yml`

```yaml
name: Test Suite

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  backend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: |
          cd backend
          pip install -r requirements.txt

      - name: Run pytest
        run: |
          cd backend
          pytest tests/ -v --cov=. --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          file: backend/coverage.xml
          flags: backend

  frontend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
          cache-dependency-path: frontend/package-lock.json

      - name: Install dependencies
        run: |
          cd frontend
          npm ci

      - name: Run Vitest
        run: |
          cd frontend
          npm test -- --run --coverage

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          file: frontend/coverage/coverage-final.json
          flags: frontend

  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Run ESLint
        run: npm run lint
```

#### 2. **Deploy Workflow** (runs on merge to main)

**File:** `.github/workflows/deploy.yml`

```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  test:
    uses: ./.github/workflows/test.yml # Reuse test workflow

  deploy-backend:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to Railway
        uses: bervProject/railway-deploy@main
        with:
          railway_token: ${{ secrets.RAILWAY_TOKEN }}
          service: backend

      - name: Run database migrations
        run: |
          railway run --service backend alembic upgrade head

  deploy-frontend:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to Railway
        uses: bervProject/railway-deploy@main
        with:
          railway_token: ${{ secrets.RAILWAY_TOKEN }}
          service: frontend

  smoke-tests:
    needs: [deploy-backend, deploy-frontend]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Health check - Backend
        run: |
          curl -f https://tapin-backend.up.railway.app/api/health || exit 1

      - name: Health check - Frontend
        run: |
          curl -f https://tapin.app || exit 1

      - name: Notify on Slack (optional)
        if: success()
        run: |
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -d '{"text":"✅ Tapin deployed successfully to production"}'
```

#### 3. **Staging Environment** (optional but recommended)

**Strategy:**

- Create `staging` branch
- Deploy to Railway staging environment
- Test before merging to `main`

**File:** `.github/workflows/deploy-staging.yml`

```yaml
name: Deploy to Staging

on:
  push:
    branches: [staging, develop]

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to Railway Staging
        uses: bervProject/railway-deploy@main
        with:
          railway_token: ${{ secrets.RAILWAY_TOKEN_STAGING }}
          service: backend
          environment: staging
```

### Branch Protection Rules

**Configure on GitHub:**

```
Branch: main
└── Require pull request reviews (1 approver)
└── Require status checks to pass
    ├── backend-tests
    ├── frontend-tests
    └── lint
└── Require branches to be up to date
└── Include administrators
```

### Secrets Configuration

**GitHub Repository Secrets:**

```
RAILWAY_TOKEN=<project-token-from-railway>
RAILWAY_TOKEN_STAGING=<staging-project-token>
SLACK_WEBHOOK=<optional-slack-webhook-url>
CODECOV_TOKEN=<optional-codecov-token>
```

### Rollback Strategy

**Manual Rollback:**

```bash
# Via Railway CLI
railway rollback

# Via Git
git revert <commit-sha>
git push origin main  # Triggers new deployment
```

**Automatic Rollback (Advanced):**

- Configure Railway to auto-rollback on health check failures
- Set up monitoring alerts (Sentry, UptimeRobot)
- Create rollback button in Railway dashboard

---

## Implementation Roadmap

### Phase 1: Map Integration (Story 3.1) - 0.5 days

**Tasks:**

1. Install Leaflet dependencies

   ```bash
   cd frontend
   npm install leaflet react-leaflet
   ```

2. Add lat/lng fields to Listing model

   ```python
   latitude = db.Column(db.Float, nullable=True)
   longitude = db.Column(db.Float, nullable=True)
   ```

3. Create `MapView.jsx` component

4. Update listing forms to include location coordinates

5. Toggle between `ListView` and `MapView`

**Assigned:** @dev

---

### Phase 2: Production Setup (Story 3.2) - 1 day

**Tasks:**

1. Create Railway account and project

2. Add `psycopg2-binary` to requirements.txt

3. Create Railway services:
   - Backend service (linked to backend/ folder)
   - Frontend service (linked to frontend/ folder)
   - PostgreSQL database

4. Configure environment variables

5. Connect GitHub repository

6. Test deployments manually

7. Document deployment URLs and access

**Assigned:** @dev with @architect support

---

### Phase 3: CI/CD Pipeline (Story 3.3) - 0.5 days

**Tasks:**

1. Create `.github/workflows/test.yml`

2. Create `.github/workflows/deploy.yml`

3. Configure GitHub secrets

4. Set up branch protection rules

5. Test pull request workflow

6. Test auto-deployment

7. Document CI/CD process

**Assigned:** @dev with @architect support

---

### Phase 4: Production Deployment (Story 3.4) - 0.5 days

**Tasks:**

1. Deploy backend to Railway production

2. Run database migrations

3. Deploy frontend to Railway production

4. Configure custom domain (optional)

5. Run smoke tests

6. Monitor for errors

7. Create production runbook

**Assigned:** @dev (deployment), @qa (verification)

---

## Cost Summary

### Monthly Recurring Costs

| Service               | Provider  | Cost             |
| --------------------- | --------- | ---------------- |
| Backend Hosting       | Railway   | $5               |
| Frontend Hosting      | Railway   | $5               |
| PostgreSQL Database   | Railway   | $5               |
| Domain (optional)     | Namecheap | $12/year ($1/mo) |
| Email (optional)      | SendGrid  | $0 (free tier)   |
| Monitoring (optional) | Sentry    | $0 (free tier)   |
| **Total**             |           | **$15-16/month** |

**Annual Cost:** ~$180-192/year

### One-Time Costs

- None (all platforms have free trials or credits)

### Alternative Budget Option

- Vercel (frontend) + Railway (backend): **$10/month**
- Free tier with limitations: **$0/month** (Render with spin-down)

---

## Risk Assessment

### Technical Risks

| Risk                                  | Likelihood | Impact | Mitigation                                    |
| ------------------------------------- | ---------- | ------ | --------------------------------------------- |
| SQLite → PostgreSQL migration issues  | Medium     | High   | Test locally first, backup data               |
| Railway platform downtime             | Low        | High   | Use Railway's status page, have rollback plan |
| Environment variable misconfiguration | Medium     | Medium | Use .env.example, document thoroughly         |
| Database migration failures           | Low        | High   | Test migrations in staging first              |
| Map performance with many markers     | Medium     | Medium | Implement marker clustering                   |

### Operational Risks

| Risk                         | Likelihood | Impact | Mitigation                                |
| ---------------------------- | ---------- | ------ | ----------------------------------------- |
| Exceeding free tier limits   | Low        | Low    | Monitor usage dashboard                   |
| Forgotten to renew domain    | Low        | Medium | Set calendar reminders                    |
| Lost access to accounts      | Low        | High   | Document credentials in 1Password/similar |
| No one knows how to rollback | Medium     | High   | Document rollback process, practice       |

---

## Success Criteria

### Story 3.1 (Map Integration)

- [ ] Listings displayed on interactive map
- [ ] Click marker shows listing preview
- [ ] Toggle between list and map view works
- [ ] Map loads within 2 seconds
- [ ] Mobile-responsive map interface

### Story 3.2 (Production Infrastructure)

- [ ] Backend deployed and accessible via HTTPS
- [ ] Frontend deployed and accessible via HTTPS
- [ ] PostgreSQL database connected and working
- [ ] Environment variables properly configured
- [ ] Health checks return 200 OK

### Story 3.3 (CI/CD Pipeline)

- [ ] Tests run automatically on every PR
- [ ] Failing tests block merge
- [ ] Auto-deployment on merge to main works
- [ ] Deployment takes < 10 minutes
- [ ] Rollback process documented and tested

### Story 3.4 (Production Deployment)

- [ ] Application live at production URLs
- [ ] All Sprint 1 features work in production
- [ ] Smoke tests pass
- [ ] No console errors
- [ ] Production runbook created

---

## Recommendations for @dev

### Immediate Actions

1. **Review this document** - Ask questions if anything is unclear
2. **Create Railway account** - Get familiar with the platform
3. **Install Leaflet locally** - Test basic map functionality
4. **Plan database migration** - Review Alembic migrations

### Best Practices

- **Test everything locally first** - Don't debug in production
- **Use staging environment** - Deploy to staging before production
- **Document as you go** - Update README with deployment steps
- **Monitor after deployment** - Watch logs for errors
- **Keep secrets secure** - Never commit API keys or tokens

### Questions to Resolve Before Starting

1. Do we want a custom domain? (adds $12/year)
2. Should we set up staging environment? (recommended)
3. Do we need email notifications working? (requires SMTP setup)
4. Who should have access to Railway/GitHub? (share credentials)

---

## Next Steps

**For Sprint 3 kickoff:**

1. **@dev** - Review this document, ask questions
2. **@architect** - Answer questions, provide support
3. **@dev** - Start with Story 3.1 (map integration) - lowest risk
4. **@dev** - Then Story 3.2 (Railway setup) - test deployments
5. **@dev** - Then Story 3.3 (CI/CD) - automate deployments
6. **@qa** - Verify Story 3.4 (production smoke tests)

**Estimated Timeline:**

- Story 3.1: 4-6 hours
- Story 3.2: 1 day
- Story 3.3: 4 hours
- Story 3.4: 4 hours
- **Total: 2-3 days**

---

**Document Status:** ✅ Ready for Implementation  
**Architect Approval:** @architect  
**Date:** November 3, 2025
