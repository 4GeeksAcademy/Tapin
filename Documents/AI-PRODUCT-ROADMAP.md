# Tapin AI-Powered Platform: Complete Product Roadmap & Architecture

**Date:** November 3, 2025  
**Agent:** @architect  
**Purpose:** Comprehensive user stories and technical architecture for AI-powered hyperlocal matching

---

## 🎯 Platform Vision

**Tapin connects locals with locals through invisible AI-powered matching across three ecosystems:**

1. **🤝 Volunteer Marketplace** - Match volunteers with meaningful community opportunities
2. **🏘️ Community Needs** - Connect people seeking help with those who can provide it
3. **💼 Service Provider Network** - Match last-minute/urgent needs with available local businesses

**Core Differentiator:** AI agents work 24/7 in the background to create perfect matches instantly while users experience a simple, magical interface.

---

## 🏗️ System Architecture (Current → AI-Enhanced)

### Phase 1: Foundation (COMPLETED ✅)

```
┌─────────────┐         ┌─────────────┐
│   React     │ ◄─────► │   Flask     │
│  Frontend   │  HTTP   │   Backend   │
│  + Leaflet  │         │  + SQLite   │
└─────────────┘         └─────────────┘
```

**Current Features:**

- User authentication (JWT)
- CRUD for listings
- Map integration (OpenStreetMap)
- Category filtering
- Reviews/ratings

### Phase 2: AI Core (NEXT - Months 1-3)

```
┌─────────────┐         ┌─────────────┐         ┌──────────────┐
│   React     │ ◄─────► │   Flask     │ ◄─────► │  Postgres    │
│  Frontend   │  HTTP   │   API       │         │   Database   │
│  + Leaflet  │         │             │         └──────────────┘
└─────────────┘         └──────┬──────┘
                               │
                               ▼
                        ┌──────────────┐         ┌──────────────┐
                        │    Redis     │ ◄─────► │ AI Workers   │
                        │ Message Queue│         │ (Celery)     │
                        └──────────────┘         └──────┬───────┘
                                                         │
                                                         ▼
                                                  ┌──────────────┐
                                                  │  Pinecone    │
                                                  │ Vector DB    │
                                                  └──────────────┘
```

**New Components:**

- **Redis**: Task queue for async AI processing
- **Celery Workers**: Run AI agents in background
- **Pinecone/Weaviate**: Vector database for semantic search
- **Postgres**: Production database with vector support

### Phase 3: Full AI Platform (Months 4-12)

```
┌─────────────┐         ┌───────────────────────────────┐
│   React     │         │     Load Balancer (nginx)      │
│  Frontend   │ ◄─────► │                                │
│  + PWA      │         └───────────────┬───────────────┘
└─────────────┘                         │
                                        ▼
                        ┌───────────────────────────────┐
                        │   Flask API Cluster (3+)       │
                        │   (Auto-scaling)               │
                        └───────────────┬───────────────┘
                                        │
                        ┌───────────────┴───────────────┐
                        │                               │
                 ┌──────▼──────┐              ┌────────▼────────┐
                 │   Postgres  │              │     Redis       │
                 │   Primary   │              │  Task Queue     │
                 │  + Replicas │              └────────┬────────┘
                 └─────────────┘                       │
                                              ┌────────┴────────┐
                                              │                 │
                                    ┌─────────▼───────┐  ┌──────▼──────┐
                                    │  AI Workers     │  │  Scheduler  │
                                    │  (6 agents)     │  │  (Airflow)  │
                                    │  Auto-scaling   │  └─────────────┘
                                    └─────────┬───────┘
                                              │
                        ┌─────────────────────┴──────────────────┐
                        │                                        │
                 ┌──────▼──────┐                        ┌────────▼────────┐
                 │  Pinecone   │                        │   ML Models     │
                 │  Vector DB  │                        │   (S3/Local)    │
                 └─────────────┘                        └─────────────────┘
```

---

## 📋 Complete User Story Matrix

### Epic 1: Foundation (COMPLETED ✅)

#### US1.1: User Authentication

**As a** user  
**I want to** register and log in securely  
**So that** I can access personalized features and my account data

**Acceptance Criteria:**

- ✅ User can register with email/password
- ✅ Passwords are hashed with bcrypt
- ✅ JWT tokens issued on login
- ✅ Session maintained across page refreshes
- ✅ Secure logout functionality

**Status:** COMPLETE

#### US1.2: Password Recovery

**As a** user  
**I want to** reset my password via email  
**So that** I can recover access if I forget credentials

**Acceptance Criteria:**

- ✅ Password reset link sent to email
- ✅ Token expires after 1 hour
- ✅ New password must meet security requirements
- ✅ Old password immediately invalidated

**Status:** COMPLETE

---

### Epic 2: Basic Listing Management (COMPLETED ✅)

#### US2.1: Create Volunteer Opportunities

**As an** organization owner  
**I want to** post volunteer opportunities  
**So that** volunteers can discover and sign up for them

**Acceptance Criteria:**

- ✅ Create listing with title, description, category, location
- ✅ Upload images (optional)
- ✅ Set date/time requirements
- ✅ Specify skills needed
- ✅ Set volunteer capacity

**Status:** COMPLETE

#### US2.2: Create Service Listings

**As a** service provider  
**I want to** list my services  
**So that** locals can discover and contact me

**Acceptance Criteria:**

- ✅ Create service listing with business info
- ✅ Set service categories
- ✅ Add pricing information
- ✅ Upload portfolio images
- ✅ Set service area/radius

**Status:** COMPLETE

#### US2.3: Browse and Filter Listings

**As a** user  
**I want to** browse and filter all listings  
**So that** I can find relevant opportunities or services

**Acceptance Criteria:**

- ✅ View all listings in grid/list format
- ✅ Filter by type (Volunteer, Service, Community Need)
- ✅ Filter by category
- ✅ Filter by location radius
- ✅ Sort by date, rating, distance

**Status:** COMPLETE

#### US2.4: View Listing Details

**As a** user  
**I want to** view detailed information about a listing  
**So that** I can decide whether to engage

**Acceptance Criteria:**

- ✅ See all listing information
- ✅ View images in gallery
- ✅ Read reviews and ratings
- ✅ See location on mini-map
- ✅ Access contact information

**Status:** COMPLETE

---

### Epic 3: Map Integration (COMPLETED ✅)

#### US3.1: Interactive Map View

**As a** user  
**I want to** see listings on an interactive map  
**So that** I can find opportunities near me visually

**Acceptance Criteria:**

- ✅ Map displays all active listings
- ✅ Markers differentiated by type (color/icon)
- ✅ Click marker to see listing preview
- ✅ Link from map popup to detail page
- ✅ Map centers on user location (with permission)

**Status:** COMPLETE

#### US3.2: List/Map Toggle

**As a** user  
**I want to** switch between list and map views  
**So that** I can choose my preferred browsing method

**Acceptance Criteria:**

- ✅ Toggle button in header
- ✅ Filters persist across views
- ✅ Smooth transition between views
- ✅ State saved in URL/local storage

**Status:** COMPLETE

---

### Epic 4: AI Data Enrichment (NEW - Priority 1)

#### US4.1: Automatic Geocoding

**As a** listing creator  
**I want** addresses automatically converted to precise coordinates  
**So that** I don't have to manually set map locations

**Acceptance Criteria:**

- [ ] Address input triggers geocoding API
- [ ] Lat/lng automatically populated
- [ ] Map preview shows location
- [ ] User can adjust if needed
- [ ] Fallback for ambiguous addresses

**Technical:**

- Use Nominatim (OpenStreetMap) API - FREE
- Background Celery task for processing
- Cache results to avoid duplicate calls

**Priority:** HIGH  
**Effort:** 3 days  
**Dependencies:** Redis + Celery setup

#### US4.2: Intelligent Categorization

**As a** listing creator  
**I want** the system to suggest categories based on my description  
**So that** my listing is properly tagged without manual effort

**Acceptance Criteria:**

- [ ] AI analyzes description text
- [ ] Suggests 3-5 relevant categories
- [ ] User can accept/modify suggestions
- [ ] Categories improve over time (learning)
- [ ] Works for all listing types

**Technical:**

- NLP model: spaCy or HuggingFace transformers
- Keywords extraction + category mapping
- Store training data for future improvement

**Priority:** MEDIUM  
**Effort:** 5 days  
**Dependencies:** ML model setup

#### US4.3: Quality Scoring

**As the** platform  
**I want to** automatically score listing quality  
**So that** better listings rank higher in search

**Acceptance Criteria:**

- [ ] Score based on completeness (0-100)
- [ ] Factors: description length, images, contact info
- [ ] Bonus for verified accounts
- [ ] Penalty for flagged content
- [ ] Score visible to listing owner only

**Technical:**

- Background worker calculates on create/update
- Stored in listings table
- Used for ranking algorithm

**Priority:** MEDIUM  
**Effort:** 2 days  
**Dependencies:** None

#### US4.4: Duplicate Detection

**As the** platform  
**I want to** detect and merge duplicate listings  
**So that** users don't see redundant content

**Acceptance Criteria:**

- [ ] Detect duplicates based on similarity
- [ ] Alert admin to potential duplicates
- [ ] Suggest merge to listing owners
- [ ] Auto-hide exact duplicates
- [ ] Learn from user feedback

**Technical:**

- Vector embeddings for semantic similarity
- Cosine similarity threshold (>0.85)
- Admin dashboard for review

**Priority:** LOW  
**Effort:** 4 days  
**Dependencies:** Vector database

---

### Epic 5: AI Matching Engine (NEW - Priority 1)

#### US5.1: Semantic Search

**As a** user  
**I want to** search using natural language  
**So that** I can find what I need without exact keywords

**Acceptance Criteria:**

- [ ] Free-form text search box
- [ ] Understands intent (e.g., "help kids read" → education/literacy)
- [ ] Returns relevant results even with different wording
- [ ] Faster than keyword search (<500ms)
- [ ] Learns from click patterns

**Technical:**

- Sentence embeddings (sentence-transformers)
- Pinecone/Weaviate vector search
- Cache popular queries
- Track click-through rate

**Priority:** HIGH  
**Effort:** 7 days  
**Dependencies:** Vector database, embeddings model

#### US5.2: Personalized Match Recommendations

**As a** user  
**I want to** see opportunities/services matched to my interests  
**So that** I discover relevant options without searching

**Acceptance Criteria:**

- [ ] Homepage shows "Recommended for You" section
- [ ] Recommendations based on profile, past activity
- [ ] Updates in real-time as preferences change
- [ ] Includes new listings matching interests
- [ ] Explains why each is recommended (transparency)

**Technical:**

- User preference vector from profile + behavior
- Similarity search against all listings
- Re-compute on login and every 4 hours
- Store in Redis cache

**Priority:** HIGH  
**Effort:** 8 days  
**Dependencies:** US5.1

#### US5.3: Smart Filters

**As a** user  
**I want** filters to adapt to my search patterns  
**So that** I find what I want faster

**Acceptance Criteria:**

- [ ] Filter options ranked by relevance
- [ ] "Suggested filters" based on search
- [ ] Remember frequently used filters
- [ ] One-click to saved filter sets
- [ ] Clear all filters easily

**Technical:**

- Track filter usage per user
- Store common combinations
- UI suggests based on current results

**Priority:** MEDIUM  
**Effort:** 3 days  
**Dependencies:** User analytics

---

### Epic 6: Urgent Matching (NEW - Priority 1)

#### US6.1: Post Urgent Needs

**As a** community member  
**I want to** post urgent/last-minute needs  
**So that** I can get help quickly

**Acceptance Criteria:**

- [ ] "Urgent" flag on listing creation
- [ ] Required: timeframe (e.g., "needed by 6pm today")
- [ ] Optional: budget/compensation
- [ ] Visible urgency indicator on listing
- [ ] Auto-expires after deadline

**Technical:**

- Urgency score calculated from timeframe
- Triggers urgent matching workflow
- Background job auto-archives expired

**Priority:** HIGH  
**Effort:** 4 days  
**Dependencies:** Celery workers

#### US6.2: Real-Time Alerts for Service Providers

**As a** service provider  
**I want to** receive instant notifications for urgent matches  
**So that** I can respond quickly and get the job

**Acceptance Criteria:**

- [ ] Push notifications to mobile/desktop
- [ ] Shows: need, location, timeframe, compensation
- [ ] One-tap "I'm available" response
- [ ] See ETA to location
- [ ] Decline without penalty

**Technical:**

- WebSocket connection for real-time alerts
- Push notification service (Firebase Cloud Messaging)
- Geolocation for ETA calculation
- Response tracking

**Priority:** HIGH  
**Effort:** 10 days  
**Dependencies:** US6.1, mobile setup

#### US6.3: Availability Toggle

**As a** service provider  
**I want to** mark myself "Available Now"  
**So that** I only get alerts when I'm actually free

**Acceptance Criteria:**

- [ ] Toggle button in profile/dashboard
- [ ] Status shown on listings
- [ ] Calendar integration (Google/Apple)
- [ ] Auto-sets "busy" during booked times
- [ ] Schedule future availability

**Technical:**

- Real-time status in Redis
- Calendar API integration (OAuth)
- Cron job syncs calendar every 15 minutes

**Priority:** HIGH  
**Effort:** 6 days  
**Dependencies:** US6.2

#### US6.4: Fast Response Leaderboard

**As a** service provider  
**I want to** see my response time stats  
**So that** I can compete to be the fastest responder

**Acceptance Criteria:**

- [ ] Shows avg response time
- [ ] Leaderboard by category/location
- [ ] Badge for top 10%
- [ ] Response rate percentage
- [ ] Public profile display

**Technical:**

- Track timestamp: alert sent → first response
- Aggregate stats per provider
- Public leaderboard view

**Priority:** LOW  
**Effort:** 3 days  
**Dependencies:** US6.2

---

### Epic 7: Resource Discovery (NEW - Priority 2)

#### US7.1: Automated Organization Discovery

**As the** platform  
**I want to** automatically discover local nonprofits  
**So that** the database stays current without manual entry

**Acceptance Criteria:**

- [ ] Daily scrape of public nonprofit databases
- [ ] Extract: name, address, contact, mission
- [ ] Verify 501(c)(3) status
- [ ] Create draft listings (pending approval)
- [ ] Notify organizations of their listing

**Technical:**

- Scrapers for IRS database, GuideStar, city websites
- NLP to extract relevant info
- Admin review queue
- Email verification before publishing

**Priority:** MEDIUM  
**Effort:** 10 days  
**Dependencies:** Email service

#### US7.2: Social Media Monitoring

**As the** platform  
**I want to** monitor local social media for community needs  
**So that** opportunities are automatically added

**Acceptance Criteria:**

- [ ] Monitor local Facebook groups, Nextdoor
- [ ] Detect volunteer/help requests
- [ ] Create suggested listings
- [ ] Contact poster for verification
- [ ] Post back to social when filled

**Technical:**

- Social media APIs (Facebook Graph, etc.)
- NLP for intent classification
- Deduplicate before adding
- Rate limiting to avoid bans

**Priority:** LOW  
**Effort:** 12 days  
**Dependencies:** Social API keys, legal review

---

### Epic 8: Predictive Intelligence (NEW - Priority 2)

#### US8.1: Predict Volunteer Availability

**As the** platform  
**I want to** predict when users are likely to volunteer  
**So that** notifications are sent at optimal times

**Acceptance Criteria:**

- [ ] Analyze past volunteer activity patterns
- [ ] Identify day-of-week and time-of-day patterns
- [ ] Factor in holidays, weather, events
- [ ] Send notifications at predicted optimal times
- [ ] A/B test timing effectiveness

**Technical:**

- ML model: Random Forest or XGBoost
- Features: day, time, weather, past behavior
- Train on historical click/signup data
- Scheduled predictions daily

**Priority:** LOW  
**Effort:** 8 days  
**Dependencies:** Analytics data (3+ months)

#### US8.2: Demand Forecasting

**As an** organization  
**I want to** see predicted volunteer interest  
**So that** I can plan capacity and outreach

**Acceptance Criteria:**

- [ ] Show estimated signup rate
- [ ] Suggest best days/times to post
- [ ] Predict how quickly opportunity will fill
- [ ] Compare to similar past opportunities
- [ ] Alert if low predicted interest

**Technical:**

- Regression model for signup prediction
- Features: category, time, location, description
- Display confidence interval
- Update predictions as signups come in

**Priority:** LOW  
**Effort:** 6 days  
**Dependencies:** US8.1

---

### Epic 9: Trust & Safety (NEW - Priority 2)

#### US9.1: Automated Trust Scoring

**As a** user  
**I want to** see trust scores for listings and users  
**So that** I can make safe decisions

**Acceptance Criteria:**

- [ ] 0-100 trust score for all entities
- [ ] Based on: verifications, activity, reviews, reports
- [ ] Badge system (verified, trusted, new)
- [ ] Score visible on listings and profiles
- [ ] Explanation of score components

**Technical:**

- Background worker calculates on activity
- Weighted factors (see AI-ARCHITECTURE-STRATEGY.md)
- Cache in database for fast lookup
- Recalculate on major events

**Priority:** MEDIUM  
**Effort:** 5 days  
**Dependencies:** US1.1 (accounts)

#### US9.2: Fraud Detection

**As the** platform  
**I want to** detect fraudulent activity automatically  
**So that** users are protected

**Acceptance Criteria:**

- [ ] Detect multi-accounting (same device/IP)
- [ ] Identify bot-like behavior patterns
- [ ] Flag suspicious listings (scams, phishing)
- [ ] Auto-freeze high-risk accounts
- [ ] Admin review queue for flags

**Technical:**

- ML anomaly detection model
- Device fingerprinting
- Pattern analysis (posting frequency, text similarity)
- Rate limiting on account creation

**Priority:** HIGH  
**Effort:** 10 days  
**Dependencies:** Analytics tracking

#### US9.3: ID Verification

**As a** service provider  
**I want to** verify my identity  
**So that** I get more bookings due to trust

**Acceptance Criteria:**

- [ ] Upload government ID
- [ ] Verify business license (for businesses)
- [ ] Background check option (for sensitive services)
- [ ] "Verified" badge on profile
- [ ] Verification status visible on listings

**Technical:**

- Integration with ID verification service (Stripe Identity, Persona)
- Secure document storage
- Manual review for edge cases

**Priority:** MEDIUM  
**Effort:** 8 days  
**Dependencies:** Payment processing setup

---

### Epic 10: Payment & Commissions (NEW - Priority 2)

#### US10.1: In-Platform Booking

**As a** community member  
**I want to** book and pay for services in-app  
**So that** the transaction is secure and tracked

**Acceptance Criteria:**

- [ ] Service provider sets prices
- [ ] Customer books time slot
- [ ] Payment via Stripe
- [ ] Platform takes 8% commission automatically
- [ ] Receipt emailed to both parties

**Technical:**

- Stripe Connect for split payments
- Booking system with calendar
- Automated commission calculation
- Refund handling

**Priority:** HIGH  
**Effort:** 12 days  
**Dependencies:** Stripe account, legal review

#### US10.2: Voluntary Contribution

**As a** service provider  
**I want to** accept bookings off-platform but voluntarily contribute  
**So that** I support the platform without forced commissions

**Acceptance Criteria:**

- [ ] Mark booking as "Booked (external)"
- [ ] Option to pay 8% voluntary support fee
- [ ] One-time or recurring contribution
- [ ] Public "Supporter" badge for contributors
- [ ] Track contribution amount (private)

**Technical:**

- Stripe one-time payments
- Badge system
- Analytics on contribution rate

**Priority:** LOW  
**Effort:** 4 days  
**Dependencies:** US10.1

---

### Epic 11: Organization Premium Features (NEW - Priority 3)

#### US11.1: Advanced Analytics Dashboard

**As a** premium organization  
**I want to** see detailed analytics on my listings  
**So that** I can optimize volunteer recruitment

**Acceptance Criteria:**

- [ ] Views, clicks, signups over time
- [ ] Demographic data (with privacy)
- [ ] Conversion funnel visualization
- [ ] Comparison to similar organizations
- [ ] Export data to CSV

**Technical:**

- Analytics tracking on all actions
- Dashboard with Chart.js/Recharts
- Aggregate queries with caching
- Data retention policy

**Priority:** MEDIUM  
**Effort:** 8 days  
**Dependencies:** Premium tier setup

#### US11.2: Automated Volunteer Outreach

**As a** premium organization  
**I want** the system to automatically notify matched volunteers  
**So that** I fill opportunities faster without manual work

**Acceptance Criteria:**

- [ ] Set target volunteer profile
- [ ] AI finds matching volunteers
- [ ] Sends personalized invitation emails
- [ ] Tracks open/click rates
- [ ] Unsubscribe option

**Technical:**

- Matching algorithm runs on listing creation
- Email campaign system (SendGrid)
- Personalization using volunteer profile data
- CAN-SPAM compliance

**Priority:** LOW  
**Effort:** 10 days  
**Dependencies:** US5.2, email service

---

## 🚀 Development Phases & Timeline

### Phase 1: Foundation (COMPLETE ✅)

**Duration:** 4 weeks  
**Status:** SHIPPED

- Basic CRUD operations
- User authentication
- Map integration
- Category filtering
- Reviews/ratings

### Phase 2: AI Infrastructure (CURRENT - Months 1-3)

**Duration:** 12 weeks  
**Goal:** Backend AI capability without changing frontend UX

**Month 1: Infrastructure Setup**

- [ ] Week 1-2: Migrate to Postgres + setup Celery/Redis
- [ ] Week 3: Vector database (Pinecone trial or Weaviate local)
- [ ] Week 4: First AI agent (Data Enrichment - US4.1, US4.3)

**Month 2: Core Matching**

- [ ] Week 5-6: Semantic search (US5.1)
- [ ] Week 7-8: Personalized recommendations (US5.2)

**Month 3: Urgent Matching**

- [ ] Week 9-10: Urgent needs + alerts (US6.1, US6.2)
- [ ] Week 11: Availability toggle (US6.3)
- [ ] Week 12: Testing, optimization, documentation

**Success Metrics:**

- Semantic search returns relevant results >80% of time
- Data enrichment runs automatically on all new listings
- Urgent alerts sent within 30 seconds of posting

### Phase 3: Intelligence Layer (Months 4-6)

**Duration:** 12 weeks  
**Goal:** Smart features that delight users

**Month 4: Discovery**

- [ ] Resource discovery agent (US7.1)
- [ ] Intelligent categorization (US4.2)
- [ ] Duplicate detection (US4.4)

**Month 5: Trust & Safety**

- [ ] Trust scoring (US9.1)
- [ ] Fraud detection (US9.2)
- [ ] ID verification (US9.3)

**Month 6: Optimization**

- [ ] Smart filters (US5.3)
- [ ] Response leaderboard (US6.4)
- [ ] Performance tuning

**Success Metrics:**

- Trust scores displayed on 100% of profiles
- Auto-discovered organizations: 50+ per city
- Fraud detection catches >90% of bad actors

### Phase 4: Monetization (Months 7-9)

**Duration:** 12 weeks  
**Goal:** Revenue generation without compromising mission

**Month 7: Payment Infrastructure**

- [ ] Stripe Connect integration (US10.1)
- [ ] Commission system (8% automated)
- [ ] Voluntary contributions (US10.2)

**Month 8: Premium Features**

- [ ] Organization premium tier ($49/month)
- [ ] Analytics dashboard (US11.1)
- [ ] Automated outreach (US11.2)

**Month 9: Conversion Optimization**

- [ ] A/B testing framework
- [ ] Upgrade prompts and messaging
- [ ] Self-service billing

**Success Metrics:**

- 5% of service providers opt for in-platform payment
- 10 organizations upgrade to premium
- $5,000+ monthly recurring revenue

### Phase 5: Scale & Intelligence (Months 10-12)

**Duration:** 12 weeks  
**Goal:** Predictive intelligence and multi-market expansion

**Month 10: Predictive Models**

- [ ] Volunteer availability prediction (US8.1)
- [ ] Demand forecasting (US8.2)
- [ ] Social monitoring (US7.2)

**Month 11: Enterprise Features**

- [ ] Multi-location management
- [ ] API for third parties
- [ ] White-label option ($199/month)

**Month 12: Scale Preparation**

- [ ] Load testing (10,000+ concurrent users)
- [ ] Auto-scaling infrastructure
- [ ] Multi-city rollout plan

**Success Metrics:**

- Predictions accurate >75% of time
- Platform handles 5,000+ daily active users
- Expanded to 3+ cities

---

## 📊 Technical Architecture Details

### Database Schema Additions (Phase 2)

```sql
-- AI-related tables

CREATE TABLE embeddings (
    id SERIAL PRIMARY KEY,
    entity_type VARCHAR(50),  -- 'listing', 'user', 'organization'
    entity_id INTEGER,
    embedding VECTOR(384),    -- Postgres with pgvector extension
    model_version VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX ON embeddings USING ivfflat (embedding vector_cosine_ops);

CREATE TABLE match_cache (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    listing_id INTEGER REFERENCES listings(id),
    match_score FLOAT,
    reasoning JSONB,
    cached_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX ON match_cache (user_id, match_score DESC);

CREATE TABLE urgent_requests (
    id SERIAL PRIMARY KEY,
    listing_id INTEGER REFERENCES listings(id),
    urgency_score INTEGER,  -- 1-10
    needed_by TIMESTAMP,
    radius_miles INTEGER,
    status VARCHAR(20),  -- 'pending', 'matched', 'expired'
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE provider_availability (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    available_now BOOLEAN DEFAULT FALSE,
    calendar_synced BOOLEAN DEFAULT FALSE,
    last_seen TIMESTAMP,
    response_time_avg INTEGER,  -- seconds
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE trust_scores (
    id SERIAL PRIMARY KEY,
    entity_type VARCHAR(50),
    entity_id INTEGER,
    score INTEGER,  -- 0-100
    components JSONB,  -- breakdown of score factors
    calculated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE ai_agent_logs (
    id SERIAL PRIMARY KEY,
    agent_name VARCHAR(100),
    action VARCHAR(100),
    entity_type VARCHAR(50),
    entity_id INTEGER,
    result JSONB,
    execution_time_ms INTEGER,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### API Endpoints (New in Phase 2)

```python
# AI-Enhanced Search
GET /api/search
    ?q=free text search
    &semantic=true
    &user_id=123  # for personalization
Response: {
    "results": [...],
    "reasoning": "Matched based on...",
    "execution_time_ms": 245
}

# Personalized Recommendations
GET /api/recommendations/:user_id
Response: {
    "recommendations": [
        {
            "listing": {...},
            "match_score": 0.94,
            "reason": "Matches your interest in education"
        }
    ]
}

# Urgent Matching
POST /api/urgent-match
Body: {
    "listing_id": 456,
    "radius_miles": 30,
    "needed_by": "2025-11-03T18:00:00Z"
}
Response: {
    "matches_alerted": 12,
    "estimated_response_time": "4 minutes"
}

# Provider Availability
PATCH /api/providers/:id/availability
Body: {
    "available_now": true
}
Response: {
    "status": "available",
    "will_receive_alerts": true
}

# Trust Score
GET /api/trust-score/:entity_type/:entity_id
Response: {
    "score": 87,
    "breakdown": {
        "email_verified": 10,
        "phone_verified": 10,
        "account_age": 8,
        "reviews": 20,
        ...
    }
}
```

### Celery Tasks (Background AI Agents)

```python
# tasks/data_enrichment.py
@celery.task
def enrich_listing(listing_id):
    """Runs when new listing created"""
    listing = Listing.query.get(listing_id)

    # Geocode address
    coords = geocode_address(listing.address)
    listing.latitude = coords['lat']
    listing.longitude = coords['lng']

    # Generate embedding
    embedding = generate_embedding(listing.description)
    store_embedding('listing', listing_id, embedding)

    # Calculate quality score
    quality = calculate_quality_score(listing)
    listing.quality_score = quality

    db.session.commit()

@celery.task
def find_personalized_matches(user_id):
    """Runs on user login or every 4 hours"""
    user = User.query.get(user_id)
    user_embedding = get_user_embedding(user_id)

    # Vector search
    matches = vector_search(user_embedding, top_k=20)

    # Cache results
    MatchCache.bulk_insert(user_id, matches)

@celery.task
def urgent_matching_workflow(urgent_request_id):
    """Runs immediately on urgent need posted"""
    request = UrgentRequest.query.get(urgent_request_id)

    # Find available providers
    providers = find_available_providers(
        category=request.category,
        radius=request.radius_miles,
        available_now=True
    )

    # Score and rank
    scored = score_urgent_matches(request, providers)
    top_5 = scored[:5]

    # Send push notifications
    for provider in top_5:
        send_urgent_alert(provider.id, request.id)

    log_agent_action('urgent_matching', request.id, {
        'providers_alerted': len(top_5)
    })
```

---

## 🎯 Success Metrics by Phase

### Phase 2 Metrics (AI Infrastructure)

- **Technical:**
  - Vector search response time <500ms
  - 95% of listings auto-enriched within 5 minutes
  - Zero downtime during migration to Postgres
- **User Impact:**
  - Search relevance score >4/5 (user survey)
  - 30% increase in successful matches
  - 20% reduction in "no results found"

### Phase 3 Metrics (Intelligence)

- **Technical:**
  - Trust scores computed for 100% of users
  - Auto-discovery adds 50+ orgs per week
  - Fraud detection catches 90%+ bad actors
- **User Impact:**
  - 40% of users engage with recommendations
  - Trust badges increase conversion by 15%
  - User reports of spam/fraud decrease 80%

### Phase 4 Metrics (Monetization)

- **Business:**
  - $5,000+ MRR by end of Month 9
  - 5% take rate on service bookings
  - 10+ premium organization subscribers
- **User Impact:**
  - <2% churn on premium subscriptions
  - 4.5+ star rating for paid features
  - No increase in user complaints

### Phase 5 Metrics (Scale)

- **Technical:**
  - Handle 10,000 concurrent users
  - 99.9% uptime
  - <100ms API response time (p95)
- **Business:**
  - 3+ cities live
  - $50,000+ MRR
  - 1,000+ service provider bookings/month

---

## 🔧 Development Best Practices

### Testing Strategy

- **Unit Tests:** 80%+ coverage for business logic
- **Integration Tests:** All AI agent workflows
- **E2E Tests:** Critical user paths (signup, search, book)
- **Load Tests:** 10x expected peak traffic
- **A/B Tests:** All new UI features before rollout

### Monitoring & Observability

- **Application:** Sentry for error tracking
- **Performance:** New Relic or DataDog APM
- **AI Agents:** Custom dashboard for agent execution
- **Business:** Mixpanel for user analytics
- **Infrastructure:** Prometheus + Grafana

### Code Organization

```
backend/
├── agents/           # AI agent implementations
│   ├── data_enrichment.py
│   ├── matching.py
│   ├── urgent.py
│   └── discovery.py
├── ml_models/        # Trained models
│   ├── embeddings/
│   ├── classifiers/
│   └── predictions/
├── tasks/            # Celery background tasks
├── api/              # Flask API routes
└── utils/            # Shared utilities
```

### Deployment Pipeline

1. **Dev:** Auto-deploy on commit to `develop` branch
2. **Staging:** Manual deploy from `main` for testing
3. **Production:** Requires approval + automated rollback
4. **AI Models:** Separate deployment with versioning

---

## 📝 Next Actions

### Immediate (This Week)

1. [ ] Set up Postgres database (local + Render)
2. [ ] Install Celery + Redis
3. [ ] Create AI agent base classes
4. [ ] Implement US4.1 (Geocoding) as first agent

### Next Sprint (Weeks 2-3)

5. [ ] Set up vector database (Pinecone trial)
6. [ ] Implement embeddings generation
7. [ ] Build semantic search endpoint (US5.1)
8. [ ] Test semantic search with sample queries

### Month 1 Goal

- Complete AI infrastructure setup
- Ship first invisible AI feature (auto-geocoding)
- Demonstrate semantic search working
- Document architecture for team

---

**Questions? Contact @architect for technical details or @product-manager for priority/scope decisions.**
