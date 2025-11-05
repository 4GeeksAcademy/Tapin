# TAPIN SYSTEM ARCHITECTURE DESIGN

**Created by:** @architect  
**Purpose:** Translate BMAD Solution into executable technical design  
**Alignment:** BMAD phases, execution roadmap, and business model  
**Status:** Ready for Phase 1-2 Development

---

## 🏗️ ARCHITECTURE OVERVIEW

### Vision

**Build a hyper-local, AI-powered volunteer matching platform that achieves 70%+ show-up rates by deeply understanding nonprofit pain points and matching volunteers with precision.**

### Design Principles

1. **User-Centric:** Nonprofit pain = primary driver; volunteer experience = secondary optimizer
2. **Data-Driven:** Every decision backed by metrics (show-up %, matching accuracy, retention)
3. **Hyper-Local:** Neighborhood-first architecture; geographic boundaries = feature, not bug
4. **MVP-First:** Phase 2 MVP must prove matching algorithm works before scaling
5. **Scalability:** Design for 3-4 neighborhoods by Month 12; data structures support 10K+ volunteers

### Deployment Strategy

```
PHASE 1 (Mo 1-2): Single backend + discovery frontend (admin only)
PHASE 2 (Mo 3-5): Dual apps (nonprofit + volunteer) + matching algorithm MVP
PHASE 3 (Mo 6-8): Revenue features + improved algorithm + analytics
PHASE 4 (Mo 9-12): Multi-tenant support + geographic expansion + API layer
```

---

## 🗄️ DATA MODEL ARCHITECTURE

### Core Entities

```
NONPROFITS (B2B Customers)
├─ Attributes: name, location, mission, size, contact
├─ Relationships: admin_users, volunteer_needs, assignments
├─ Metrics: posting_frequency, avg_show_up_rate, repeat_volunteer_%
└─ Phase 2 Critical: Must track performance per nonprofit

VOLUNTEER_NEEDS (Opportunity Postings)
├─ Attributes: title, description, date, time, location, skills_required
├─ Relationships: nonprofit_id, volunteer_assignments, volunteer_feedback
├─ Metrics: posted_at, deadline, filled_at, total_matches_suggested
└─ Phase 2 Critical: This is the PRIMARY entity driving everything

VOLUNTEERS (B2C Network)
├─ Attributes: email, phone, name, skills, availability, location_preference
├─ Relationships: volunteer_matches, assignments, feedback_history
├─ Metrics: signup_date, total_assignments, show_up_rate, retention_cohort
└─ Phase 2 Critical: Track behavior patterns for matching algorithm

VOLUNTEER_MATCHES (AI Matching Output)
├─ Attributes: volunteer_id, need_id, match_score, suggested_at
├─ Relationships: assignment (one-to-one after conversion)
├─ Metrics: click_through_rate, conversion_to_assignment, feedback
└─ Phase 2 Critical: THE CORE of AI algorithm - measure and improve

ASSIGNMENTS (Volunteer Commitments)
├─ Attributes: volunteer_id, need_id, assignment_status, assigned_at
├─ Relationships: feedback, show_up_record, volunteer_notification
├─ Metrics: show_up (yes/no), feedback_score, time_spent
└─ Phase 2 Critical: End state - validate 70%+ show-up achievement

FEEDBACK (Loop Back Data)
├─ Attributes: from_volunteer, from_nonprofit, assignment_id, rating, text
├─ Relationships: volunteer, nonprofit, assignment
├─ Metrics: avg_rating, sentiment, mentioned_issues
└─ Phase 2 Critical: Feed algorithm improvements + nonprofit satisfaction

GEOGRAPHIC_ZONES (Hyper-Local Boundaries)
├─ Attributes: zone_name, neighborhood, city, postal_codes, bounds
├─ Relationships: nonprofits, volunteers, volunteer_needs
├─ Metrics: nonprofit_density, volunteer_density, network_health
└─ Phase 2 Critical: Boundary enforcement for hyper-local value prop
```

### Database Schema (Phase 2 MVP)

```sql
-- NONPROFITS
CREATE TABLE nonprofits (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    mission TEXT,
    size ENUM('small', 'medium', 'large'),  -- <50, 50-250, 250+
    annual_budget DECIMAL(12,2),
    primary_contact_name VARCHAR(255),
    primary_contact_phone VARCHAR(20),
    nonprofit_location_id BIGINT REFERENCES geographic_zones(id),
    tier ENUM('free', 'pro', 'enterprise') DEFAULT 'free',
    subscription_start DATE,
    subscription_end DATE,
    monthly_rate DECIMAL(10,2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_nonprofits_zone ON nonprofits(nonprofit_location_id);
CREATE INDEX idx_nonprofits_tier ON nonprofits(tier);

-- VOLUNTEERS
CREATE TABLE volunteers (
    id BIGSERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    skills TEXT[],  -- JSON array: ['mentoring', 'tech', 'construction']
    availability JSON,  -- { "weekdays": [1-5], "weekends": [6-7], "hours": "mornings" }
    home_zone_id BIGINT REFERENCES geographic_zones(id),
    willingness_to_travel_miles INT DEFAULT 3,
    motivation ENUM('social_impact', 'skill_building', 'community', 'other'),
    is_active BOOLEAN DEFAULT TRUE,
    tier ENUM('free', 'premium', 'pro') DEFAULT 'free',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_volunteers_zone ON volunteers(home_zone_id);
CREATE INDEX idx_volunteers_skills ON volunteers USING GIN(skills);

-- VOLUNTEER_NEEDS (Core Opportunity Entity)
CREATE TABLE volunteer_needs (
    id BIGSERIAL PRIMARY KEY,
    nonprofit_id BIGINT NOT NULL REFERENCES nonprofits(id),
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    required_skills TEXT[],
    location_id BIGINT REFERENCES geographic_zones(id),
    preferred_date DATE,
    preferred_time TIME,
    estimated_hours FLOAT,
    status ENUM('draft', 'active', 'filled', 'cancelled') DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    posted_at TIMESTAMP,
    deadline TIMESTAMP,
    filled_at TIMESTAMP
);

CREATE INDEX idx_needs_nonprofit ON volunteer_needs(nonprofit_id);
CREATE INDEX idx_needs_zone ON volunteer_needs(location_id);
CREATE INDEX idx_needs_status ON volunteer_needs(status);

-- VOLUNTEER_MATCHES (AI Algorithm Output)
CREATE TABLE volunteer_matches (
    id BIGSERIAL PRIMARY KEY,
    volunteer_id BIGINT NOT NULL REFERENCES volunteers(id),
    need_id BIGINT NOT NULL REFERENCES volunteer_needs(id),
    match_score FLOAT,  -- 0.0 to 1.0
    match_reasoning JSON,  -- { "skills_match": 0.95, "availability": 0.85, "proximity": 0.8 }
    suggested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    volunteer_viewed_at TIMESTAMP,
    volunteer_clicked_at TIMESTAMP,
    status ENUM('suggested', 'clicked', 'assigned', 'rejected') DEFAULT 'suggested',
    UNIQUE(volunteer_id, need_id)
);

CREATE INDEX idx_matches_volunteer ON volunteer_matches(volunteer_id);
CREATE INDEX idx_matches_need ON volunteer_matches(need_id);
CREATE INDEX idx_matches_score ON volunteer_matches(match_score DESC);

-- ASSIGNMENTS (Final Commitment)
CREATE TABLE assignments (
    id BIGSERIAL PRIMARY KEY,
    volunteer_id BIGINT NOT NULL REFERENCES volunteers(id),
    need_id BIGINT NOT NULL REFERENCES volunteer_needs(id),
    match_id BIGINT REFERENCES volunteer_matches(id),
    assignment_status ENUM('pending', 'confirmed', 'completed', 'no_show') DEFAULT 'pending',
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    confirmed_at TIMESTAMP,
    completed_at TIMESTAMP,
    actual_hours FLOAT,
    show_up BOOLEAN,
    nonprofit_confirmed BOOLEAN DEFAULT FALSE
);

CREATE INDEX idx_assignments_volunteer ON assignments(volunteer_id);
CREATE INDEX idx_assignments_nonprofit ON assignments(need_id);
CREATE INDEX idx_assignments_status ON assignments(assignment_status);

-- FEEDBACK (Loop Data for Algorithm Improvement)
CREATE TABLE feedback (
    id BIGSERIAL PRIMARY KEY,
    assignment_id BIGINT REFERENCES assignments(id),
    from_role ENUM('volunteer', 'nonprofit'),
    rating INT CHECK (rating >= 1 AND rating <= 5),
    text TEXT,
    feedback_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_feedback_assignment ON feedback(assignment_id);

-- GEOGRAPHIC_ZONES (Hyper-Local Boundaries)
CREATE TABLE geographic_zones (
    id BIGSERIAL PRIMARY KEY,
    zone_name VARCHAR(255) NOT NULL,
    neighborhood VARCHAR(255),
    city VARCHAR(255) NOT NULL,
    state VARCHAR(2),
    postal_codes TEXT[],
    center_lat FLOAT,
    center_lng FLOAT,
    radius_miles INT DEFAULT 3,
    nonprofit_count INT DEFAULT 0,
    volunteer_count INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_zones_city ON geographic_zones(city);
```

---

## 🎯 MATCHING ALGORITHM (Phase 2 MVP Core)

### Design Goal

**Achieve 70%+ show-up rate by matching volunteers to opportunities based on (1) skill fit, (2) availability alignment, (3) geographic proximity, (4) volunteer behavior patterns**

### Algorithm v1 Logic (Weighted Scoring)

```python
def calculate_match_score(volunteer, need):
    """
    Phase 2 MVP: Simple weighted scoring
    Goal: 70%+ show-up prediction accuracy

    Factors:
    1. Skills match (30% weight): Do volunteer's skills fit need?
    2. Availability match (30% weight): Does volunteer's schedule fit?
    3. Geographic proximity (20% weight): Is volunteer near the opportunity?
    4. Volunteer reliability (20% weight): Historical show-up rate
    """

    # 1. SKILLS MATCH (30%)
    skills_match = calculate_skill_overlap(volunteer.skills, need.required_skills)
    # Output: 0.0-1.0 (1.0 = perfect match)

    # 2. AVAILABILITY MATCH (30%)
    availability_match = check_availability_compatibility(
        volunteer.availability,
        need.preferred_date,
        need.preferred_time
    )
    # Output: 0.0-1.0 (1.0 = perfect fit)

    # 3. GEOGRAPHIC PROXIMITY (20%)
    distance = calculate_distance(volunteer.location, need.location)
    proximity_score = max(0, 1.0 - (distance / volunteer.willingness_to_travel_miles))
    # Output: 0.0-1.0 (1.0 = at location, 0.0 = too far)

    # 4. VOLUNTEER RELIABILITY (20%)
    # Historical data: this volunteer's show-up rate
    reliability_score = volunteer.historical_show_up_rate / 100
    # Output: 0.0-1.0 (based on past behavior)

    # WEIGHTED SCORE
    total_score = (
        (skills_match * 0.30) +
        (availability_match * 0.30) +
        (proximity_score * 0.20) +
        (reliability_score * 0.20)
    )

    return total_score  # 0.0-1.0, where >0.7 = "good match"

def suggest_matches(need, min_score=0.7):
    """
    For each new need:
    1. Calculate match scores for ALL volunteers in zone
    2. Rank by score
    3. Suggest top N (typically 3-5) to nonprofit
    4. Track nonprofit interaction (click, assign, ignore)
    5. Use feedback loop to improve algorithm
    """

    zone_volunteers = get_volunteers_in_zone(need.location_id)

    matches = []
    for volunteer in zone_volunteers:
        score = calculate_match_score(volunteer, need)
        if score >= min_score:
            matches.append({
                'volunteer_id': volunteer.id,
                'need_id': need.id,
                'match_score': score,
                'reasoning': {
                    'skills': calculate_skill_overlap(...),
                    'availability': check_availability_compatibility(...),
                    'proximity': proximity_score,
                    'reliability': volunteer.historical_show_up_rate
                }
            })

    # Sort by score (highest first)
    matches.sort(key=lambda x: x['match_score'], reverse=True)

    # Suggest top 3-5 to nonprofit
    suggested = matches[:5]

    # Save suggestions to volunteer_matches table
    for match in suggested:
        save_volunteer_match(match)

    return suggested
```

### Algorithm Improvement Loop (Feedback → Iteration)

```
Week 1: Nonprofit posts need for "food prep volunteer, Saturdays 9am-1pm"
    ↓
Algorithm suggests: [Volunteer A (0.82), Volunteer B (0.75), Volunteer C (0.70)]
    ↓
Nonprofit selects Volunteer A → Assignment created
    ↓
Saturday comes → Volunteer A shows up ✅
    ↓
Feedback collected:
    - Volunteer A rating: 5/5 "Perfect fit, exactly what we needed"
    - Nonprofit rating: 5/5 "Volunteer was reliable and helpful"
    ↓
Learning: Volunteer A's profile features correlated with POSITIVE outcome
    → Increase weights for: weekend availability, food prep skills, reliability history
    ↓
Next time similar need posted:
    → Algorithm gives Volunteer A higher match_score (0.82 → 0.88)
    → More likely to be suggested first
```

### Phase 2 Success Metric

**Target: 70%+ of matched assignments result in volunteer showing up**

```
Baseline data needed Week 1-3:
├─ 50+ assignments made
├─ Track actual show-up (yes/no)
├─ Correlation: match_score vs. actual_show_up
└─ Iterate algorithm weekly based on data

Target Achievement by End of Phase 2 (Week 20):
├─ 70%+ show-up rate achieved
├─ Nonprofit satisfaction 4.5+/5
├─ Algorithm factors tuned based on real data
└─ Decision Gate: PASS → GO to Phase 3
```

---

## 🚀 API ARCHITECTURE

### Phase 2 MVP Endpoints (Minimal Set)

**Authentication**

```
POST /auth/register        - Signup (nonprofit or volunteer)
POST /auth/login           - Login + JWT token
POST /auth/logout          - Logout
POST /auth/refresh         - Refresh JWT token
```

**Nonprofit Dashboard**

```
GET  /nonprofits/{id}      - Nonprofit profile
POST /needs                - Create volunteer need
GET  /needs/{id}           - View specific need
PUT  /needs/{id}           - Update need (status, details)
GET  /needs                - List all needs for nonprofit
GET  /needs/{id}/matches   - Suggested volunteers for need
POST /assignments          - Create assignment (nonprofit selects volunteer)
GET  /assignments          - List assignments for nonprofit
POST /assignments/{id}/confirm - Nonprofit confirms volunteer showed up
GET  /analytics/dashboard  - Basic metrics (assignments, show-up rate)
```

**Volunteer App**

```
GET  /zones/{zone_id}/needs - List needs in volunteer's zone
GET  /needs/{id}            - View opportunity details
GET  /needs/{id}/match-score - Get MY match score for this need
POST /assignments/{id}/apply - Volunteer expresses interest/confirms
GET  /assignments           - Volunteer's commitments
POST /assignments/{id}/feedback - Leave feedback
GET  /profile              - Volunteer profile
PUT  /profile              - Update availability, skills, location
```

**Admin / Analytics** (Phase 3+)

```
GET  /admin/metrics        - System-wide metrics
GET  /admin/zones          - Geographic zone management
POST /admin/zones          - Create new zone
GET  /admin/nonprofits     - Manage nonprofits
```

### Response Format (Example)

```json
// GET /zones/{zone_id}/needs
{
  "status": "success",
  "data": {
    "zone_id": 1,
    "zone_name": "Park Slope, Brooklyn",
    "needs": [
      {
        "id": 101,
        "nonprofit_name": "Community Kitchen",
        "title": "Food Prep Volunteers",
        "description": "Help prepare meals for neighborhood residents",
        "skills_required": ["food_prep", "kitchen_safety"],
        "date": "2025-11-10",
        "time": "09:00-13:00",
        "location": "123 Main St, Brooklyn",
        "estimated_hours": 4,
        "my_match_score": 0.82,
        "match_explanation": {
          "skills": "You have food prep experience (95% match)",
          "availability": "Saturday mornings are your preferred time (perfect)",
          "proximity": "1.2 miles from your location",
          "reliability": "You show up 85% of the time (strong)"
        },
        "status": "active"
      }
      // ... more needs
    ],
    "total_count": 12
  }
}
```

---

## 🎨 FRONTEND ARCHITECTURE

### Phase 2 MVP App Structure

**Nonprofit Dashboard**

```
/nonprofit/dashboard
├─ Header
│  ├─ Nonprofit name + logo
│  └─ Quick actions: New Post, View Needs, View Volunteers
├─ Main content
│  ├─ Metrics card: "X volunteers assigned, Y% show-up rate"
│  ├─ Active needs list (clickable for details)
│  │  └─ Each need shows:
│  │     - Title, date, time, location
│  │     - Suggested volunteers (AI-ranked)
│  │     - Assignment status
│  └─ Actions: Create Need, View Analytics
└─ Modals
   ├─ Create New Need (form)
   ├─ View Suggested Volunteers (list + rank)
   └─ Confirm Volunteer Showed Up (checkbox + feedback)
```

**Volunteer App**

```
/volunteer/browse
├─ Header
│  ├─ "Opportunities in your area"
│  └─ Filter: Skills, Date, Distance
├─ Opportunity cards (feed-style)
│  └─ Each card shows:
│     - Nonprofit name + mission
│     - Opportunity title + description
│     - Date, time, location, estimated hours
│     - MY MATCH SCORE (large, green if >0.7)
│     - "Why this might be perfect for you" (explanation)
│     - CTA: "I'm interested" or "Tell me more"
└─ Modals
   ├─ Opportunity detail (full info)
   ├─ Commitment confirmation
   └─ Feedback form (after volunteer shows up)
```

### Tech Stack (Phase 2)

```
Frontend:
├─ Framework: React 18.2 (already in place)
├─ Build: Vite 5.0 (already in place)
├─ Routing: React Router v6
├─ State: Zustand or Context API
├─ UI Components: Tailwind CSS + shadcn/ui
├─ HTTP Client: Axios or Fetch API
└─ Maps: Leaflet.js (for geographic visualization)

Backend:
├─ Framework: Flask 2.2 (already in place)
├─ ORM: SQLAlchemy 3.0 (already in place)
├─ Database: SQLite (Phase 2), PostgreSQL (Phase 3+)
├─ Auth: JWT via flask-jwt-extended (already in place)
├─ APIs: Flask-RESTful or Blueprint pattern
├─ Email: SMTP (for notifications)
└─ Async: Background jobs (Celery + Redis in Phase 3)

DevOps (Phase 3):
├─ Containerization: Docker
├─ Orchestration: Kubernetes or Docker Compose
├─ CI/CD: GitHub Actions
├─ Database: PostgreSQL 15+
├─ Cache: Redis
├─ Task Queue: Celery
└─ Search: Elasticsearch (optional, Phase 4+)
```

---

## 📊 METRICS & OBSERVABILITY

### Critical Phase 2 Metrics

```
NONPROFIT METRICS:
├─ Posted needs: How many nonprofits are using the platform?
├─ Suggested matches per need: Are we finding enough candidates?
├─ Match acceptance rate: % of suggestions that become assignments
├─ Assignment show-up rate: % of assignments that volunteers complete
├─ Nonprofit satisfaction: NPS + 5-star rating
└─ Repeat nonprofit rate: % posting multiple needs

VOLUNTEER METRICS:
├─ Monthly active volunteers: % growth week-over-week
├─ Assignment completion rate: % of commitments fulfilled
├─ Individual show-up rate: Personalized reliability score
├─ Volunteer satisfaction: NPS + 5-star rating
├─ Retention cohort: % returning to platform after 1st assignment
└─ Skills diversity: Distribution of skills in volunteer base

ALGORITHM METRICS (THE CORE):
├─ Match accuracy: For assignments made, % with 70%+ match_score
├─ Show-up correlation: Do high-scoring matches → high show-up?
├─ False positive rate: % of matches that volunteered but didn't show up
├─ Suggestion coverage: % of volunteers suggested for each need
└─ Algorithm improvement rate: Weekly A/B test results

BUSINESS METRICS:
├─ MRR (Monthly Recurring Revenue): Sum of paying nonprofit subscriptions
├─ ARR (Annual Recurring Revenue): MRR × 12
├─ Churn rate: % of nonprofits cancelling subscription
├─ Gross margin: Revenue - COGS / Revenue
└─ CAC (Customer Acquisition Cost): Marketing spend / New customers
```

### Dashboard (Real-Time Tracking)

```
/admin/metrics

Section 1: WEEKLY SNAPSHOT
├─ New volunteers: 45
├─ New needs posted: 23
├─ Assignments made: 67
├─ Show-up rate: 68% (tracking toward 70%)
└─ Nonprofit satisfaction: 4.3/5

Section 2: ALGORITHM PERFORMANCE
├─ Avg match score: 0.76
├─ Match-to-assignment rate: 42%
├─ Show-up correlation: 0.78 (high correlation = good!)
└─ Weekly improvement: +2.3%

Section 3: RETENTION
├─ Volunteer repeat rate: 38% (after first assignment)
├─ Nonprofit repeat post rate: 65%
└─ Churn alerts: X nonprofits at risk

Section 4: REVENUE (Phase 3+)
├─ Paying nonprofits: 8
├─ MRR: $1,600
├─ Expansion revenue: $150 (premium volunteers)
└─ Churn: $0 (no cancellations this week)
```

---

## 🔐 SECURITY & COMPLIANCE

### Phase 2 Security Requirements

```
AUTHENTICATION:
├─ JWT tokens (30-minute expiry, refresh tokens 7-day)
├─ Password hashing: bcrypt
├─ Email verification before nonprofit access
└─ Phone verification (optional for volunteers)

DATA PRIVACY:
├─ PII: Only store what's necessary (name, email, phone)
├─ Sensitive data: Password hashed, encrypted at rest
├─ GDPR compliance: User deletion endpoint
├─ Audit logs: Track all data access
└─ Rate limiting: Prevent abuse

PLATFORM SAFETY:
├─ Volunteer background check (optional, Phase 3)
├─ Nonprofit verification (confirmed nonprofit status)
├─ Report/block mechanism (flag inappropriate users)
├─ Feedback system for accountability
└─ Escalation path for issues
```

---

## 🚢 DEPLOYMENT STRATEGY

### Phase 2 Deployment

```
WEEK 9-10: Development Environment
├─ Backend: Running on localhost:5000
├─ Frontend: Running on localhost:5173 (Vite dev server)
├─ Database: SQLite data.db
└─ Testing: Local unit + integration tests

WEEK 11-12: Pilot Environment
├─ Backend: Deployed to simple host (Render, Railway, Heroku)
├─ Frontend: Deployed to Vercel or GitHub Pages
├─ Database: SQLite (upgrade to PostgreSQL Week 15+)
├─ Domain: tapin-pilot.local or similar
└─ Users: 3-5 nonprofits + 200 volunteers

WEEK 13+: Production-Ready
├─ Backend: Containerized (Docker)
├─ Frontend: CDN-delivered (Vercel)
├─ Database: PostgreSQL + backups
├─ Monitoring: Error tracking (Sentry) + logging (LogRocket)
└─ Scaling: Ready for multi-zone expansion (Phase 4)
```

### CI/CD Pipeline (Phase 2 Ready)

```
.github/workflows/test-and-deploy.yml

On: Push to main
  Step 1: Run tests (backend + frontend)
  Step 2: Lint checks
  Step 3: Build frontend
  Step 4: Deploy backend
  Step 5: Deploy frontend
  Step 6: Smoke tests on staging
  Step 7: Rollback if tests fail

Target: Automated deployment every commit
```

---

## 📋 PHASE 2 DEVELOPMENT CHECKLIST

### Week 9-10: Setup + Matching Algorithm

- [ ] Database schema finalized (use above SQL)
- [ ] Matching algorithm implemented (v1 with 4 factors)
- [ ] API endpoints stubbed (all routes defined)
- [ ] Authentication middleware working
- [ ] Unit tests for algorithm (70%+ coverage)
- [ ] Integration tests for API

### Week 11-12: Nonprofit Dashboard

- [ ] Dashboard layout (React components)
- [ ] Create need form (frontend + backend)
- [ ] View needs list (fetch + display)
- [ ] Suggested volunteers list (call matching algorithm)
- [ ] Confirm volunteer showed up (update assignment status)
- [ ] Basic analytics view (MRR, assignments, show-up %)

### Week 13-14: Volunteer App

- [ ] Browse opportunities feed
- [ ] Display match score + explanation
- [ ] "I'm interested" button (create assignment)
- [ ] My commitments page
- [ ] Feedback form (post-assignment)
- [ ] Notification system (email/SMS when matched)

### Week 15-20: Pilot Launch + Iteration

- [ ] Deploy to staging environment
- [ ] Onboard 3-5 nonprofit pilots
- [ ] Recruit 200+ volunteers
- [ ] Track show-up rate daily
- [ ] Weekly algorithm iteration based on feedback
- [ ] Iterate UI based on user feedback
- [ ] Nonprofit satisfaction surveys (target 4.5+/5)

### Success Criteria (End of Phase 2)

- ✅ 50+ volunteer assignments made
- ✅ 70%+ show-up rate achieved
- ✅ 4.5+/5 nonprofit satisfaction
- ✅ 40%+ repeat volunteer rate
- ✅ Algorithm accuracy validated
- ✅ Zero critical bugs
- ✅ Decision Gate: PASS → Proceed to Phase 3

---

## 🔮 FUTURE PHASES (3-4) ARCHITECTURE

### Phase 3: Revenue + Optimization

**Backend Enhancements:**

- PostgreSQL migration (SQLite → production-grade DB)
- Redis for caching + rate limiting
- Celery for async jobs (email, notifications, algorithm runs)
- Advanced analytics (cohort analysis, churn prediction)
- Webhook system for integrations

**Frontend Enhancements:**

- Payment processing (Stripe integration)
- Subscription management (upgrade/downgrade/cancel)
- Advanced filtering (skills, dates, distance)
- Impact dashboard (volunteer hours, nonprofits helped)
- Mobile app (Phase 4)

### Phase 4: Scale + Expansion

**Architecture Changes:**

- Multi-tenant support (one codebase, multiple zones)
- Elasticsearch for full-text search
- API marketplace (third-party integrations)
- Mobile apps (iOS + Android)
- Machine learning model improvements

**Data Infrastructure:**

- Data warehouse (Snowflake or BigQuery)
- Analytics pipeline (dbt + data models)
- Real-time dashboards (Tableau or Metabase)
- Predictive models (churn, matching, growth)

---

## ✅ ALIGNMENT WITH BUSINESS PLAN

### How Architecture Supports BMAD

| BMAD Goal                     | Architecture Component                         | Success Measure                              |
| ----------------------------- | ---------------------------------------------- | -------------------------------------------- |
| "70%+ show-up rate"           | Matching algorithm with 4 factors              | Show-up rate ≥ 70% by Week 20                |
| "Nonprofits primary revenue"  | Nonprofit dashboard + subscription tier system | 8+ paying nonprofits by Month 8              |
| "Volunteer engagement driver" | Volunteer app with match scores + feedback     | 200+ volunteers by Week 20                   |
| "Hyper-local network effects" | Geographic zone system + local filtering       | One neighborhood, 20%+ nonprofit penetration |
| "Data moat"                   | Feedback loop + algorithm learning             | Algorithm improves 2%+ weekly                |
| "$60K MRR by Month 12"        | Multi-zone deployment + replication            | 3-4 zones, proven playbook                   |

### How Phases Align

| Business Phase     | Architecture Phase             | Timeline | Output                       |
| ------------------ | ------------------------------ | -------- | ---------------------------- |
| Phase 1: Discovery | Architecture design (this doc) | Mo 1-2   | System design + requirements |
| Phase 2: MVP Pilot | MVP development + launch       | Mo 3-5   | Working app, 70%+ show-up    |
| Phase 3: Revenue   | Optimization + payment systems | Mo 6-8   | Paid tiers, $20K MRR         |
| Phase 4: Expansion | Multi-tenant + scale           | Mo 9-12  | 3-4 zones, $60K+ MRR         |

---

## 📚 REFERENCE DOCS

**Related Documentation:**

- BMAD-SOLUTION.md - Business model + strategy
- EXECUTION-ROADMAP-12-MONTH.md - Phase-by-phase timeline
- tapin-research-findings.md - Market validation
- API_DOCS.md - API specification (backend/)

---

## 🎯 NEXT STEPS (For Dev Team)

1. **Review this document** with product + engineering team (1 hour)
2. **Validate database schema** (any changes needed?)
3. **Set up development environment** (Docker + PostgreSQL for Phase 2)
4. **Create GitHub issues** for each Phase 2 task (Week 9-20)
5. **Assign ownership** (who builds what?)
6. **Begin Week 9 sprint** with matching algorithm implementation

**Status: ✅ READY FOR DEVELOPMENT**

_System Architecture Design: November 3, 2025_  
_Next milestone: Phase 2 MVP Launch (Week 15)_
