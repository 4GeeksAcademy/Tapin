# ⚡ WEEK 9 QUICK START CHECKLIST

**For: @dev team**  
**Start Date: Monday, November 4, 2025**  
**Duration: 1 week**  
**Goal: Foundation complete + all tests passing**

---

## 📋 MONDAY MORNING (Nov 4) - Setup Day

### 9:00am - 9:30am: Kickoff Meeting

- [ ] Review DEV-SPRINT-PLAN-PHASE-2.md (this sprint plan)
- [ ] Review ARCHITECTURE-SYSTEM-DESIGN.md (5 min highlight: Sections 1-3)
- [ ] Questions? Ask here
- [ ] Confirm everyone understands the goal: 70%+ show-up by Week 20

### 9:30am - 10:00am: Environment Setup

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest pytest-cov  # Add for testing
python app.py  # Verify it starts
# Ctrl+C to stop
```

- [ ] Virtual environment created
- [ ] Packages installed
- [ ] Flask starts without errors

### 10:00am - 10:30am: Copy Code Files

**Source:** PHASE2-TECHNICAL-IMPLEMENTATION.md

1. [ ] Create `backend/models_phase2.py` - Copy code from PHASE2-TECHNICAL (Section 2.1)
2. [ ] Create `backend/matching_algorithm.py` - Copy from PHASE2-TECHNICAL (Section 2.2)
3. [ ] Create `backend/api_nonprofit.py` - Copy from PHASE2-TECHNICAL (Section 2.3)
4. [ ] Create `backend/api_volunteer.py` - Copy from PHASE2-TECHNICAL (Section 2.4)

**Each file should be copy-paste ready. No changes needed yet.**

### 10:30am - 11:00am: Wire Blueprints

**File:** `backend/app.py`

1. [ ] Add imports at top:

```python
from models_phase2 import (
    GeographicZone, Nonprofit, Volunteer, VolunteerNeed,
    VolunteerMatch, Assignment, Feedback
)
from api_nonprofit import nonprofit_api
from api_volunteer import volunteer_api
```

2. [ ] Add after existing blueprints (search for "register_blueprint" if any exist):

```python
app.register_blueprint(nonprofit_api)
app.register_blueprint(volunteer_api)
```

3. [ ] Test it:

```bash
python app.py
# Should start without errors
# Ctrl+C to stop
```

- [ ] Imports working
- [ ] Blueprints registered
- [ ] App starts clean

### 11:00am - 12:00pm: Database Setup

```bash
# Delete old database to start fresh
rm data.db

# Create new migration for Phase 2 tables
alembic revision --autogenerate -m "create_phase2_tables"

# Verify migration file created (check alembic/versions/)
ls -la alembic/versions/

# Run migration
python manage.py upgrade
# or: alembic upgrade head

# Verify tables created
sqlite3 data.db ".tables"
# Should see: geographic_zones, nonprofits, volunteers,
#            volunteer_needs, volunteer_matches, assignments, feedback
#            (plus old tables: listing, review, signup, user, item)
```

- [ ] Old database cleaned
- [ ] Migration created
- [ ] Migration runs cleanly
- [ ] All 7 new tables in database

### 12:00pm - 1:00pm: Verify Endpoints

```bash
# Start app in one terminal
python app.py

# In another terminal, test endpoints
curl http://127.0.0.1:5000/api/nonprofit/dashboard
# Should return 401 (unauthorized) or valid response (good - endpoint exists)

curl http://127.0.0.1:5000/api/volunteer/zone/1/needs
# Should return valid response (endpoint accessible)

# Test algorithm function directly in Python
python
>>> from matching_algorithm import calculate_match_score
>>> # Can import without errors?
>>> # Good! Algorithm loaded
```

- [ ] Nonprofit endpoints accessible
- [ ] Volunteer endpoints accessible
- [ ] Algorithm imports cleanly

---

## 📋 TUESDAY - THURSDAY (Nov 5-7) - Implementation & Testing

### Tuesday (Day 2): Matching Algorithm Testing

```bash
# Create test file
cat > tests/test_matching_algorithm.py << 'EOF'
import pytest
from matching_algorithm import (
    calculate_skill_overlap,
    check_availability_compatibility,
    calculate_match_score
)

def test_skill_overlap_perfect_match():
    skills1 = '["mentoring", "tech"]'
    skills2 = '["mentoring", "tech"]'
    score = calculate_skill_overlap(skills1, skills2)
    assert score > 0.8  # Should be high

def test_skill_overlap_no_match():
    skills1 = '["mentoring"]'
    skills2 = '["construction"]'
    score = calculate_skill_overlap(skills1, skills2)
    assert score < 0.5  # Should be low

# Add 13+ more tests here
EOF

# Run tests
pytest tests/test_matching_algorithm.py -v --cov=matching_algorithm
```

- [ ] 15+ algorithm tests written
- [ ] All tests passing
- [ ] Coverage ≥70%

### Wednesday (Day 3): API Endpoint Testing

```bash
# Create test file for nonprofits API
cat > tests/test_api_nonprofit.py << 'EOF'
import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_dashboard_unauthorized(client):
    response = client.get('/api/nonprofit/dashboard')
    assert response.status_code in [401, 403]  # Should require auth

def test_create_need():
    # Test creating a nonprofit need
    pass

# Add tests for all nonprofit endpoints
EOF

# Run tests
pytest tests/test_api_nonprofit.py -v
```

- [ ] 10+ nonprofit API tests written
- [ ] Tests passing
- [ ] All CRUD operations covered

### Wednesday (Day 3): Volunteer API Testing

```bash
# Create test file for volunteer API
cat > tests/test_api_volunteer.py << 'EOF'
import pytest

def test_browse_zone_needs():
    # Test browsing needs in a zone
    pass

def test_create_assignment():
    # Test volunteer creating assignment
    pass

# Add tests for all volunteer endpoints
EOF

# Run tests
pytest tests/test_api_volunteer.py -v
```

- [ ] 10+ volunteer API tests written
- [ ] Tests passing
- [ ] All endpoints tested

### Thursday (Day 4): Integration Testing

```bash
# Create integration test file
cat > tests/test_integration_flow.py << 'EOF'
import pytest
from app import app, db

def test_full_flow():
    """
    Test complete flow:
    1. Create geographic zone
    2. Create nonprofit
    3. Create volunteer
    4. Nonprofit posts need
    5. Algorithm suggests volunteers
    6. Volunteer creates assignment
    7. Nonprofit confirms show-up
    """
    pass

EOF

# Run full test suite
pytest tests/ -v --cov=. --cov-report=html
```

- [ ] Integration test covers full flow
- [ ] All pieces work together
- [ ] Coverage report generated

---

## 📋 FRIDAY (Nov 8) - Go/No-Go Gate Assessment

### Morning: Code Review

- [ ] Review all code written (models, algorithm, API)
- [ ] Check for obvious bugs
- [ ] Verify PEP 8 style
- [ ] Remove debug code

### Afternoon: Final Testing

```bash
# Run full test suite
pytest tests/ -v --cov=. -x  # Stop on first failure

# Check coverage
pytest tests/ --cov-report=term-showing-missing

# Manual testing: Create test data
python
>>> from app import app, db
>>> from models_phase2 import *
>>> from matching_algorithm import *
>>>
>>> # Create zone
>>> zone = GeographicZone(zone_name="Park Slope", city="Brooklyn")
>>> db.session.add(zone)
>>> db.session.commit()
>>>
>>> # Create nonprofit
>>> nonprofit = Nonprofit(
...     name="Community Kitchen",
...     email="kitchen@example.com",
...     nonprofit_location_id=zone.id
... )
>>> db.session.add(nonprofit)
>>> db.session.commit()
>>>
>>> # Create volunteer
>>> volunteer = Volunteer(
...     email="john@example.com",
...     first_name="John",
...     last_name="Doe",
...     skills='["cooking"]',
...     home_zone_id=zone.id
... )
>>> db.session.add(volunteer)
>>> db.session.commit()
>>>
>>> # Create need
>>> need = VolunteerNeed(
...     nonprofit_id=nonprofit.id,
...     title="Food Prep",
...     description="Help prep meals",
...     location_id=zone.id
... )
>>> db.session.add(need)
>>> db.session.commit()
>>>
>>> # Generate matches
>>> from matching_algorithm import generate_matches_for_need
>>> matches = generate_matches_for_need(need.id)
>>> print(f"Generated {len(matches)} matches")
>>> # Should see: Generated 1+ matches
```

### End-of-Week Assessment: GO/NO-GO Gate

**PASS (GO to Week 11):**

- ✅ All 7 models created + relationships working
- ✅ Database migration clean + tables verified
- ✅ Matching algorithm: 15+ tests passing (70%+ coverage)
- ✅ API endpoints: All working (Postman/curl verified)
- ✅ End-to-end flow: Zone → Nonprofit → Volunteer → Need → Match → Assignment works
- ✅ Zero critical bugs
- ✅ Test coverage ≥70%

**HOLD (Extend Week 10):**

- ❌ Tests failing (fix before proceeding)
- ❌ Critical bugs found (prioritize fixes)
- ❌ Coverage <70% (add tests)
- ❌ Any blocker preventing integration

### Friday 5pm: Status Update

- [ ] Send Slack message to leadership
  - "✅ Foundation phase PASS - proceeding to Week 11 integration"
  - "❌ Foundation phase HOLD - extending Week 10 (details: ...)"

---

## 🎯 WEEK 9 SUCCESS CRITERIA

### By End of Friday

```
✅ 4 new files created (models_phase2.py, algorithm, 2x API)
✅ Database migrations created + all 7 tables in DB
✅ 35+ unit tests written + passing
✅ Code coverage ≥70%
✅ All endpoints testable via curl/Postman
✅ Full flow works: need → matches → assignment → show-up
✅ Zero critical bugs blocking integration

= GO to Week 11 ✅
```

---

## 📊 Time Budget (Week 9)

```
Monday:    3 hours (setup + copy code + wire blueprints)
Tuesday:   4 hours (algorithm tests)
Wednesday: 4 hours (API tests)
Thursday:  4 hours (integration + manual testing)
Friday:    2 hours (review + go/no-go assessment)

Total: 17 hours / 40-hour week = Reasonable + buffer for issues
```

---

## ❌ Common Pitfalls (Avoid These)

1. **Don't skip environment setup**
   → Spend time Monday morning getting venv + packages right
   → Saves 5 hours debugging later

2. **Don't write tests AFTER code**
   → Write tests as you code
   → Catches bugs early

3. **Don't skip database verification**
   → Verify tables exist before testing
   → SQL mistakes catch errors fast

4. **Don't ignore coverage reports**
   → Check coverage % every day
   → Aim for ≥70% (not lower)

5. **Don't skip manual end-to-end testing**
   → Just running unit tests isn't enough
   → Manually create zone → nonprofit → need → match

---

## 🚀 Commands You'll Use All Week

```bash
# Activate environment (every session)
source .venv/bin/activate

# Run tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ --cov=. --cov-report=html

# Start app
python app.py

# Test endpoints
curl http://127.0.0.1:5000/api/nonprofit/dashboard

# Database
sqlite3 data.db ".tables"
python manage.py upgrade

# View test results
open htmlcov/index.html  # Open coverage report
```

---

## 📞 SUPPORT

**Questions about:**

- **Architecture?** → Check ARCHITECTURE-SYSTEM-DESIGN.md
- **Code structure?** → Check PHASE2-TECHNICAL-IMPLEMENTATION.md (Section 2)
- **Why something exists?** → Check BMAD-SOLUTION.md or EXECUTION-ROADMAP-12-MONTH.md
- **Stuck?** → Ask @architect or @pm for clarification

---

**Status: ✅ READY FOR MONDAY MORNING KICKOFF**

_Week 9 Checklist: November 3, 2025_  
_Execution starts: Monday, November 4_  
_Go/No-Go gate: Friday, November 8 (5pm)_
