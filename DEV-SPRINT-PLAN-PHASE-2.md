# 🚀 PHASE 2 MVP DEVELOPMENT SPRINT PLAN

**Developer Assigned:** @dev  
**Sprint Period:** Weeks 9-20 (Months 3-5, November-January)  
**Current Date:** November 3, 2025  
**Status:** ✅ READY TO KICKOFF MONDAY

---

## 📋 CURRENT BACKEND STATE (AUDIT)

### What Exists ✅

```
✅ Flask 2.2+ configured (CORS, JWT, SQLAlchemy working)
✅ Basic User model (email, password_hash, role)
✅ Listing model (title, description, location, lat/lng)
✅ SignUp model (user signup tracking for listings)
✅ Review model (user reviews)
✅ Item model (simple MVP items)
✅ Authentication infrastructure (JWT, password hashing)
✅ Database migrations (alembic configured)
✅ 30+ tests in place (test_api.py, test_auth.py)
✅ Environment config (.env support)
```

### What Needs to be ADDED for Phase 2 ❌

```
❌ GeographicZone model (NEW - hyper-local boundaries)
❌ Nonprofit model (NEW - B2B customers)
❌ Volunteer model (NEW - B2C network)
❌ VolunteerNeed model (NEW - PRIMARY entity - opportunities)
❌ VolunteerMatch model (NEW - AI algorithm output)
❌ Assignment model (NEW - volunteer commitments)
❌ Feedback model (NEW - learning loop)
❌ Matching algorithm (CORE - 4-factor scoring)
❌ Nonprofit API endpoints (CRITICAL - dashboard)
❌ Volunteer API endpoints (CRITICAL - app)
```

### Architecture Decision: Keep or Migrate?

**Keep existing models:** User, Listing, SignUp, Review (these are Phase 1)  
**Add new models:** All 7 Phase 2 entities (above)  
**Database:** SQLite now (Phase 2), migrate to PostgreSQL in Phase 3+

---

## 📅 SPRINT BREAKDOWN (Week 9-20)

### WEEK 9-10: FOUNDATION PHASE ✅

#### Sprint Goal

Build database foundation + implement matching algorithm + basic API

#### Specific Tasks

**Task 1: Create models.py (Phase 2 entities)**

- [ ] Create `backend/models_phase2.py` (new file)
- [ ] Add 7 core models: GeographicZone, Nonprofit, Volunteer, VolunteerNeed, VolunteerMatch, Assignment, Feedback
- [ ] All relationships defined (foreign keys, backrefs)
- [ ] All fields as per ARCHITECTURE-SYSTEM-DESIGN.md section 2
- **Time:** 2-3 hours
- **Deliverable:** models_phase2.py (400+ lines, copy from PHASE2-TECHNICAL-IMPLEMENTATION.md)

**Task 2: Create database migration**

- [ ] Run `alembic revision --autogenerate -m "create_phase2_tables"`
- [ ] Verify SQL generated
- [ ] Run `alembic upgrade head`
- [ ] Verify data.db has all 7 new tables
- **Time:** 1 hour
- **Deliverable:** New alembic revision file + verified database

**Task 3: Implement matching algorithm**

- [ ] Create `backend/matching_algorithm.py` (new file)
- [ ] Implement 4 functions:
  - `calculate_skill_overlap(volunteer_skills, need_skills)`
  - `check_availability_compatibility(availability, date, time)`
  - `calculate_proximity_score(v_lat_lng, n_lat_lng, max_miles)`
  - `calculate_match_score(volunteer, need)` - main function
- [ ] Implement `generate_matches_for_need(need_id)`
- [ ] Implement `update_algorithm_from_feedback()`
- **Time:** 3-4 hours
- **Deliverable:** matching_algorithm.py (200+ lines, copy from PHASE2-TECHNICAL)
- **Testing:** 15+ unit tests (70%+ coverage)

**Task 4: Create API endpoints (nonprofit)**

- [ ] Create `backend/api_nonprofit.py` (new file)
- [ ] Implement Blueprint: `nonprofit_api`
- [ ] Endpoints:
  - `GET /api/nonprofit/dashboard` - Dashboard metrics
  - `POST /api/nonprofit/needs` - Create opportunity
  - `GET /api/nonprofit/needs/<id>` - View need + suggested matches
  - `GET /api/nonprofit/needs` - List all needs
  - `POST /api/nonprofit/assignments/<id>/confirm-show-up` - Record show-up
- **Time:** 2-3 hours
- **Deliverable:** api_nonprofit.py (150+ lines, copy from PHASE2-TECHNICAL)

**Task 5: Create API endpoints (volunteer)**

- [ ] Create `backend/api_volunteer.py` (new file)
- [ ] Implement Blueprint: `volunteer_api`
- [ ] Endpoints:
  - `GET /api/volunteer/zone/<zone_id>/needs` - Browse opportunities
  - `GET /api/volunteer/needs/<id>` - View opportunity detail
  - `POST /api/volunteer/assignments` - Express interest (create assignment)
  - `GET /api/volunteer/assignments` - View my commitments
  - `POST /api/volunteer/assignments/<id>/feedback` - Submit feedback
- **Time:** 2-3 hours
- **Deliverable:** api_volunteer.py (120+ lines, copy from PHASE2-TECHNICAL)

**Task 6: Wire blueprints to app**

- [ ] Import blueprints in app.py
- [ ] Register both blueprints: `app.register_blueprint(nonprofit_api)`, etc.
- [ ] Test all endpoints with Postman
- **Time:** 1 hour
- **Deliverable:** Working endpoints, accessible via API

**Task 7: Write unit tests**

- [ ] Test matching algorithm (15+ test cases)
- [ ] Test API endpoints (20+ test cases)
- [ ] Test database relationships
- [ ] Aim for 70%+ code coverage
- **Time:** 3-4 hours
- **Deliverable:** test_phase2.py (200+ lines of tests)

#### Week 9-10 Success Criteria (GO/NO-GO GATE)

```
✅ All 7 Phase 2 models created + relationships working
✅ Database migration runs cleanly (no errors)
✅ Matching algorithm unit tests pass (70%+ coverage)
✅ API endpoints functional (Postman tests pass)
✅ Can create a need → get suggested volunteers end-to-end
✅ Zero critical bugs blocking integration

Decision: GO to Week 11 (Frontend Integration)
         or HOLD (fix issues, extend Week 10)
```

#### Deliverables

- ✅ models_phase2.py (6 new models)
- ✅ matching_algorithm.py (complete implementation)
- ✅ api_nonprofit.py (nonprofit endpoints)
- ✅ api_volunteer.py (volunteer endpoints)
- ✅ Alembic migration (database schema)
- ✅ test_phase2.py (unit + integration tests)
- ✅ All tests passing locally

---

### WEEK 11-12: INTEGRATION PHASE ✅

#### Frontend Team Parallel Track

(Backend on-call for API issues)

#### Sprint Goal

Full stack integration - frontend calls backend, end-to-end flow works

#### Specific Tasks (Backend Support)

**Task 1: API testing + optimization**

- [ ] Load test: Simulate 200 volunteers browsing opportunities
- [ ] Performance test: Database queries optimized
- [ ] Add database indexes on frequently queried columns
  - `idx_needs_nonprofit` on volunteer_needs(nonprofit_id)
  - `idx_needs_zone` on volunteer_needs(location_id)
  - `idx_volunteers_zone` on volunteers(home_zone_id)
  - `idx_matches_volunteer` on volunteer_matches(volunteer_id)
- **Time:** 2-3 hours

**Task 2: Error handling + logging**

- [ ] Add comprehensive error handling to all endpoints
- [ ] Add logging for all API calls
- [ ] Return consistent error format (400/500 errors)
- **Time:** 1-2 hours

**Task 3: Data validation**

- [ ] Validate all input data (nonprofit creation, need creation, etc.)
- [ ] Return validation errors to frontend
- [ ] Prevent invalid state transitions (e.g., can't assign if no match)
- **Time:** 1-2 hours

**Task 4: Frontend integration support**

- [ ] Debug API calls from frontend team
- [ ] Help trace issues (CORS, JWT, data format)
- [ ] Add test data generator for frontend testing
- **Time:** 3-4 hours (on-call)

#### Week 11-12 Success Criteria

```
✅ All API endpoints working with frontend
✅ No CORS errors
✅ No JWT auth errors
✅ Full user flow testable: nonprofit → create need → volunteer sees → assigns → nonprofit confirms
✅ No data loss or corruption
✅ Performance acceptable (< 500ms response time)

Decision: GO to Week 13 (Deployment)
         or HOLD (debug integration issues)
```

#### Deliverables

- ✅ Optimized, tested API
- ✅ Database indexes added
- ✅ Error handling + logging
- ✅ Test data generators
- ✅ Integration test results

---

### WEEK 13-14: HARDENING + DEPLOYMENT PHASE ✅

#### Sprint Goal

Production-ready code, deploy to staging

#### Specific Tasks

**Task 1: Code review + cleanup**

- [ ] Review all code (models, algorithm, API)
- [ ] Refactor any technical debt
- [ ] Ensure code style consistent (PEP 8)
- [ ] Remove debug code
- **Time:** 2-3 hours

**Task 2: Database backup + recovery procedures**

- [ ] Test database backup
- [ ] Test database restore
- [ ] Document procedure for production
- **Time:** 1 hour

**Task 3: Environment configuration**

- [ ] Set up production-like staging environment
- [ ] PostgreSQL optional (can stay on SQLite for now)
- [ ] Configure secret management
- [ ] Test with production env vars
- **Time:** 1-2 hours

**Task 4: Docker containerization**

- [ ] Create `backend/Dockerfile`
- [ ] Create `docker-compose.yml` (optional but helpful)
- [ ] Test Docker build locally
- [ ] Verify app runs in container
- **Time:** 2-3 hours

**Task 5: CI/CD pipeline**

- [ ] Create GitHub Actions workflow (`.github/workflows/test-deploy.yml`)
- [ ] On push to main: run tests, build Docker image
- [ ] Deploy to staging environment
- **Time:** 2-3 hours

**Task 6: Security hardening**

- [ ] Review JWT configuration
- [ ] Verify passwords hashed (not plaintext)
- [ ] Add rate limiting (optional for Phase 2)
- [ ] Review CORS configuration (only allow frontend origin)
- **Time:** 1-2 hours

**Task 7: Monitoring + alerting setup**

- [ ] Add error tracking (Sentry optional)
- [ ] Add basic logging
- [ ] Set up health check endpoint
- [ ] Test monitoring works
- **Time:** 1-2 hours

#### Week 13-14 Success Criteria

```
✅ Code reviewed + cleaned
✅ Tests pass (unit + integration)
✅ Docker image builds successfully
✅ Staging environment deployed
✅ Health check endpoint working
✅ Can run 5 nonprofits + 200 volunteers on staging
✅ Performance acceptable under load

Decision: GO to Week 15 (Pilot Launch)
         or HOLD (performance tune/fix bugs)
```

#### Deliverables

- ✅ Production-ready code
- ✅ Docker image + docker-compose
- ✅ CI/CD pipeline configured
- ✅ Staging environment deployed
- ✅ Monitoring + alerting setup
- ✅ Security review completed

---

### WEEK 15-20: PILOT LAUNCH + ITERATION ✅

#### Sprint Goal

Launch with real users, track metrics, improve algorithm

#### Specific Tasks

**Task 1: Test data generation (Week 15)**

- [ ] Create seed script for pilot data
  - 1 geographic zone (Brooklyn, NY)
  - 5 nonprofit accounts
  - 200 volunteer accounts
  - 50 volunteer needs
- [ ] Script: `backend/seed_pilot_data.py`
- [ ] Time: 1-2 hours
- [ ] Run script to populate staging with test data

**Task 2: Metrics tracking + dashboards (Week 15-16)**

- [ ] Create new API endpoint: `GET /api/admin/metrics`
- [ ] Calculate real-time metrics:
  - Total volunteers
  - Total needs posted
  - Total assignments made
  - Show-up rate %
  - Avg match score
- [ ] Add endpoint: `GET /api/admin/algorithm-performance`
- [ ] Track algorithm accuracy (correlation between match_score and actual_show_up)
- **Time:** 2-3 hours

**Task 3: Weekly algorithm iteration (Week 16-20)**

- [ ] Day 1: Analyze show-up data from previous week
- [ ] Identify which match factors are most predictive
- [ ] Adjust weights if needed (slight tweaks, no major changes)
- [ ] Re-run tests to ensure no regressions
- [ ] Deploy updated algorithm
- **Time:** 2 hours/week × 5 weeks = 10 hours total

**Task 4: On-call support (Week 15-20)**

- [ ] Monitor platform during pilot
- [ ] Fix critical bugs immediately (production hotfixes)
- [ ] Respond to nonprofit support requests
- [ ] Track error logs + respond to errors
- **Time:** 5-10 hours/week (on-call status)

**Task 5: Performance optimization (Week 16-20)**

- [ ] Profile slow API endpoints
- [ ] Optimize database queries
- [ ] Add caching if needed (Redis optional)
- [ ] Improve matching algorithm speed if needed
- **Time:** 2-3 hours/week

**Task 6: Bug fixes (Week 16-20)**

- [ ] Fix any issues reported by nonprofits
- [ ] Handle edge cases discovered in real use
- [ ] Add tests to prevent regression
- **Time:** 2-5 hours/week (reactive)

#### Week 15-20 Success Criteria (FINAL GO/NO-GO GATE)

```
✅ 50+ volunteer assignments made successfully
✅ 70%+ show-up rate achieved (CRITICAL METRIC)
✅ 4.5+/5 nonprofit satisfaction (NPS survey)
✅ 40%+ volunteer repeat rate (retention)
✅ Algorithm accuracy validated (high-score matches show up)
✅ Zero critical bugs
✅ Platform stable (99%+ uptime)
✅ Ready to transition to Phase 3

Decision: GO to Phase 3 (Paid revenue, $200/mo)
         or REASSESS (iterate more, extend pilot, or pivot)
```

#### Deliverables

- ✅ Pilot data loaded
- ✅ Real-time metrics dashboard
- ✅ Weekly algorithm improvements
- ✅ Production hotfixes as needed
- ✅ 70%+ show-up rate proven
- ✅ Ready for Phase 3 decision

---

## 🛠️ TECHNICAL SETUP (DO THIS FIRST)

### Step 1: Environment Setup (Monday morning, 30 min)

```bash
# Navigate to backend
cd /Users/houseofobi/Documents/GitHub/Tapin/backend

# Verify Python 3.10+
python3 --version

# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Verify you're in venv (should see .venv prefix)
which python

# Install dependencies
pip install -r requirements.txt

# Add these packages for Phase 2 (if not already in requirements.txt)
pip install pytest pytest-cov  # For testing

# Verify Flask works
python app.py
# Should see: "Running on http://127.0.0.1:5000"
```

### Step 2: Database Verification (Monday, 15 min)

```bash
# Check current database
sqlite3 data.db ".tables"
# Should see: listing, review, signup, user, item

# Run existing migrations
python manage.py upgrade
# Should see: "Upgrade successful"

# Verify app runs
python app.py &
# In another terminal:
curl http://127.0.0.1:5000/api/health
# Should return: {"status": "ok"}
```

### Step 3: Copy Code from Architecture Doc (Monday, 30 min)

1. Open PHASE2-TECHNICAL-IMPLEMENTATION.md (section 2.1)
2. Copy models.py code → Create `backend/models_phase2.py`
3. Copy matching_algorithm.py code → Create `backend/matching_algorithm.py`
4. Copy api_nonprofit.py code → Create `backend/api_nonprofit.py`
5. Copy api_volunteer.py code → Create `backend/api_volunteer.py`

### Step 4: Import New Models in app.py (Monday, 15 min)

Add to top of app.py:

```python
from models_phase2 import (
    GeographicZone, Nonprofit, Volunteer, VolunteerNeed,
    VolunteerMatch, Assignment, Feedback
)
```

### Step 5: Wire Blueprints (Monday, 30 min)

Add to app.py (after existing imports):

```python
from api_nonprofit import nonprofit_api
from api_volunteer import volunteer_api

# Register blueprints
app.register_blueprint(nonprofit_api)
app.register_blueprint(volunteer_api)
```

---

## 📊 PROGRESS TRACKING

### Weekly Checkpoints

**Week 9 (Nov 4-8):**

- [ ] Day 1: Environment setup complete
- [ ] Day 2: models_phase2.py created + tested
- [ ] Day 3: Matching algorithm implemented
- [ ] Day 4: API endpoints created
- [ ] Day 5: All unit tests passing (70%+ coverage)

**Week 10 (Nov 11-15):**

- [ ] Day 1-2: Integration testing
- [ ] Day 3-4: Bug fixes
- [ ] Day 5: Go/No-Go gate assessment
- [ ] Status: Foundation phase COMPLETE or EXTEND

**Week 11-12 (Nov 18 - Dec 2):**

- [ ] Frontend team integrating backend
- [ ] Backend on-call for issues
- [ ] Status: Integration phase COMPLETE

**Week 13-14 (Dec 3-16):**

- [ ] Code hardening + deployment
- [ ] Docker + CI/CD setup
- [ ] Status: Staging deployment COMPLETE

**Week 15-20 (Dec 17 - Jan 20):**

- [ ] Pilot launch + iteration
- [ ] Algorithm improvements
- [ ] Show-up rate tracking
- [ ] Status: Phase 2 MVP COMPLETE or PIVOT

---

## 🎯 SUCCESS METRICS (QUANTIFIED)

### Week 10 Success Criteria

```
✅ Code coverage: ≥70% (unit tests)
✅ Response time: <500ms for all endpoints
✅ Database: All 7 tables created + relationships verified
✅ Algorithm: 15+ unit tests passing
✅ Integration: Need → matches → assignment end-to-end works
```

### Week 14 Success Criteria

```
✅ Staging deployment: 99%+ uptime
✅ Load test: Handles 5 nonprofits + 200 volunteers
✅ Performance: <2s response time under load
✅ Security: No critical vulnerabilities
✅ Monitoring: Alerting configured + tested
```

### Week 20 Success Criteria (CRITICAL)

```
✅ 70%+ show-up rate (THE KEY METRIC)
✅ 4.5+/5 nonprofit satisfaction
✅ 40%+ volunteer repeat rate
✅ Algorithm accuracy: High-score matches correlate with show-up
✅ Zero critical bugs
✅ Ready for Phase 3 (paid revenue)
```

---

## 🚨 POTENTIAL BLOCKERS (What Could Go Wrong)

### Technical Blockers

| Blocker                     | Risk      | Mitigation                              |
| --------------------------- | --------- | --------------------------------------- |
| Database migration fails    | 🟡 Medium | Test migrations on fresh DB first       |
| Algorithm too slow          | 🟡 Medium | Profile + optimize queries, add indexes |
| API endpoints timeout       | 🟡 Medium | Implement pagination, caching           |
| Matching accuracy poor      | 🔴 High   | Iterate weekly based on feedback data   |
| Frontend integration issues | 🟡 Medium | Daily sync with frontend team           |
| Show-up rate <60%           | 🔴 High   | Reassess algorithm + pivot decision     |

### Mitigation Strategies

**If show-up rate < 60%:**
→ Extend Week 20 pilot (gather more data)
→ Reassess algorithm weights (adjust factors)
→ Consider alternative pivot: Volunteer-first or freemium

**If API performance degrades under load:**
→ Add database indexes
→ Implement query pagination
→ Add Redis caching layer

**If frontend integration blocked:**
→ Pair programming with frontend
→ Create test harness for manual API testing
→ Mock frontend for backend development

---

## 📚 REFERENCE DOCUMENTS

### Documentation You'll Need

- **ARCHITECTURE-SYSTEM-DESIGN.md** - Complete system blueprint
- **PHASE2-TECHNICAL-IMPLEMENTATION.md** - Code ready to copy
- **EXECUTION-ROADMAP-12-MONTH.md** - Business timeline
- **chart_script.py** - Run this to see project Gantt roadmap

### Quick Links in Code

- `backend/app.py` - Main Flask app (update this to wire blueprints)
- `backend/requirements.txt` - Dependencies
- `backend/alembic/` - Database migrations
- `backend/tests/` - Test files (model after these)

---

## ✅ READY TO START

**Your Week 1 Checklist:**

- [ ] Monday 9am: Team kickoff meeting (15 min)
- [ ] Monday 9:30am: Environment setup (30 min)
- [ ] Monday 10am: Copy code from architecture docs (30 min)
- [ ] Monday 10:30am: Wire blueprints to app (15 min)
- [ ] Monday 11am: Start implementing models_phase2.py

**By Friday (Week 1):**

- ✅ Environment fully set up
- ✅ All 4 code files created (models, algorithm, 2x API)
- ✅ Unit tests written (15+ for algorithm)
- ✅ All tests passing

**Week 1 Success Criteria:**

- ✅ Can create a volunteer need
- ✅ Can get suggested volunteers back (algorithm works)
- ✅ Can create assignment (volunteer expresses interest)
- ✅ Can confirm show-up
- ✅ Full end-to-end flow testable locally

---

## 🎯 MY JOB AS @DEV

I will:

1. ✅ Build Phase 2 MVP exactly per architecture
2. ✅ Write 70%+ test coverage (no tech debt)
3. ✅ Track 70%+ show-up metric religiously
4. ✅ Iterate algorithm weekly based on data
5. ✅ Ship production-ready code
6. ✅ Support frontend team during integration
7. ✅ Make go/no-go decision at gates (with data)

---

**Status: ✅ READY FOR WEEK 9 KICKOFF**

_Development Sprint Plan: November 3, 2025_  
_Start Date: Monday, November 4, 2025_  
_MVP Launch Target: Week 15 (December 16)_  
_Success Metric: 70%+ show-up by Week 20 (January 20)_
