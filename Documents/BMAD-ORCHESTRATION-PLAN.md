# Tapin AI Platform - BMad Orchestration Plan

**Date:** November 3, 2025  
**Orchestrator:** @bmad-orchestrator  
**Project Phase:** Phase 2 - AI Infrastructure (Months 1-3)  
**Status:** Planning & Role Assignment

---

## 🎯 Mission Brief

Transform Tapin from basic MVP into AI-powered hyperlocal matching platform by implementing 6 intelligent agents that work invisibly in the background to create perfect matches between volunteers, community needs, and service providers.

**Current State:** Phase 1 complete (auth, listings, map, reviews)  
**Target State:** AI infrastructure operational with semantic search and auto-enrichment  
**Approach:** Iterative development with continuous integration

---

## 👥 Agent Team Assignments

### @analyst - Business & Requirements Analysis

**Primary Responsibilities:**

- Validate AI strategy aligns with market needs
- Research vector database options (Pinecone vs Weaviate vs pgvector)
- Define success metrics for each AI feature
- Competitive analysis of AI-powered local platforms
- User research: How do people search for local opportunities?

**Deliverables:**

- [ ] Vector database recommendation report
- [ ] AI success metrics dashboard design
- [ ] User search behavior analysis
- [ ] Competitive landscape: AI features in similar platforms

**Dependencies:** None (can start immediately)

---

### @pm - Product Management & Prioritization

**Primary Responsibilities:**

- Maintain product roadmap and sprint planning
- Prioritize 47 user stories from AI-PRODUCT-ROADMAP.md
- Define MVP for Phase 2 (what ships in 12 weeks?)
- Stakeholder communication and expectation management
- Risk assessment and mitigation strategies

**Deliverables:**

- [ ] Phase 2 sprint breakdown (3 sprints × 4 iterations each)
- [ ] Feature prioritization matrix (MoSCoW method)
- [ ] Risk register with mitigation plans
- [ ] Progress reports to stakeholders (Ongoing)

**Dependencies:** @analyst's research, @architect's technical feasibility

---

### @po - Product Owner & Backlog Management

**Primary Responsibilities:**

- Own and refine user stories from AI-PRODUCT-ROADMAP.md
- Write detailed acceptance criteria for each story
- Manage sprint backlog and story dependencies
- Conduct story grooming sessions with @dev
- Accept/reject completed work

**Deliverables:**

- [ ] Refined user stories for Sprint 1 (US4.1, US4.3, US5.1)
- [ ] Acceptance test scenarios for each story (Ongoing)
- [ ] Sprint planning sessions (bi-weekly)
- [ ] Story sign-off and release notes (End of each sprint)

**Dependencies:** @pm's prioritization, @qa's test strategy

---

### @sm - Scrum Master & Process Facilitation

**Primary Responsibilities:**

- Facilitate daily standups and sprint ceremonies
- Remove blockers for development team
- Track sprint velocity and burndown
- Ensure BMad method practices are followed
- Coordinate between all agents

**Deliverables:**

- [ ] Sprint ceremony schedule
- [ ] Velocity tracking dashboard
- [ ] Blocker resolution log (Ongoing)
- [ ] Retrospective insights and improvements (End of each sprint)

**Dependencies:** All team members

---

### @architect - Technical Architecture & Design

**Primary Responsibilities:**

- Design AI infrastructure architecture
- Database migration strategy (SQLite → Postgres)
- Define API contracts for AI endpoints
- Select ML models and frameworks
- Infrastructure as code (Terraform/Docker)

**Deliverables:**

- [ ] Postgres migration plan with rollback strategy (Sprint 1 - Early)
- [ ] Redis + Celery architecture design (Sprint 1 - Early)
- [ ] API specification for AI endpoints (Sprint 1 - Mid)
- [ ] ML model selection rationale (sentence-transformers, etc.) (Sprint 1 - Mid)
- [ ] Docker compose setup for local development (Sprint 1 - Late)
- [ ] Production deployment architecture (Render/Railway) (Sprint 1 - Final)

**Dependencies:** @analyst's vector DB research

---

### @dev - Full Stack Development & Implementation

**Primary Responsibilities:**

- Implement all user stories from backlog
- Build 6 AI agents (data enrichment, matching, etc.)
- API development and database migrations
- ML model integration and testing
- Code reviews and documentation

**Deliverables - Sprint 1:**

- [ ] US4.1: Auto-geocoding agent implementation
- [ ] US4.3: Quality scoring algorithm
- [ ] Postgres migration (SQLite → Postgres + pgvector)
- [ ] Redis + Celery worker setup
- [ ] Background task queue implementation

**Deliverables - Sprint 2:**

- [ ] US5.1: Semantic search with embeddings
- [ ] US5.2: Personalized recommendation engine
- [ ] Vector database integration (Pinecone/Weaviate)
- [ ] Caching layer optimization

**Deliverables - Sprint 3:**

- [ ] US6.1, US6.2: Urgent matching + real-time alerts
- [ ] US6.3: Availability toggle for service providers
- [ ] WebSocket implementation for real-time features
- [ ] Performance optimization and load testing

**Dependencies:** @architect's designs, @po's refined stories

---

### @qa - Quality Assurance & Testing

**Primary Responsibilities:**

- Define test strategy for AI features
- Write automated tests (unit, integration, E2E)
- Test data generation for ML models
- Performance testing and benchmarking
- Security testing (AI-specific vulnerabilities)

**Deliverables:**

- [ ] AI test strategy document (Sprint 1 - Early)
- [ ] Test data generator for embeddings (Sprint 1 - Mid)
- [ ] Automated test suite for each AI agent (Ongoing)
- [ ] Performance benchmarks (semantic search <500ms) (Sprint 2 - Mid)
- [ ] Security audit: AI model input validation (Sprint 2 - Final)
- [ ] Load testing report (10K concurrent users) (Sprint 3 - Final)

**Test Coverage Targets:**

- Unit tests: 80%+ for business logic
- Integration tests: All AI agent workflows
- E2E tests: Critical user journeys (search, urgent match)

**Dependencies:** @dev's implementations

---

### @ux-expert - UX Design & User Experience

**Primary Responsibilities:**

- Ensure AI features are invisible but delightful
- Design "Recommended for You" UI components
- Real-time notification UX (urgent alerts)
- Loading states for AI processing
- Explain AI decisions without overwhelming users

**Deliverables:**

- [ ] "Invisible AI" design principles document (Sprint 1 - Early)
- [ ] Mockups: Personalized recommendations section (Sprint 1 - Late)
- [ ] Urgent alert notification designs (mobile + desktop) (Sprint 2 - Early)
- [ ] Loading/processing state animations (Sprint 2 - Mid)
- [ ] "Why this match?" explanation tooltips (Sprint 2 - Final)
- [ ] User testing sessions (3 rounds) (End of each sprint)

**Dependencies:** @pm's feature prioritization, @dev's API readiness

---

## 🎬 Workflow Orchestration

### Phase 2 Overview: AI Infrastructure (12 Weeks)

```yaml
# bmad-core/workflows/phase-2-ai-infrastructure.yaml

workflow_name: 'Phase 2: AI Infrastructure Setup'
approach: 'Iterative development with 3 sprints'
goal: 'Ship semantic search, auto-enrichment, and urgent matching'

sprints:
  - sprint_1:
      theme: 'Foundation - Infrastructure & First AI Agent'
      stories: ['US4.1', 'US4.3']

  - sprint_2:
      theme: 'Intelligence - Semantic Search & Recommendations'
      stories: ['US5.1', 'US5.2']

  - sprint_3:
      theme: 'Real-Time - Urgent Matching & Alerts'
      stories: ['US6.1', 'US6.2', 'US6.3']
```

---

## 📅 Sprint 1: Foundation (4 Iterations)

### Iteration 1: Planning & Setup

**Sprint Planning - Initial Setup**

- @sm: Facilitate sprint planning
- @po: Present refined user stories (US4.1, US4.3)
- @dev: Estimate story points
- @pm: Confirm sprint goals and deliverables

**Research & Design Phase**

- @analyst: Complete vector database research → Recommendation report
- @architect: Design Postgres migration strategy
- @architect: Design Redis + Celery architecture
- @ux-expert: Draft "Invisible AI" design principles

**Infrastructure Setup Phase**

- @dev: Set up Postgres locally + Render instance
- @dev: Install Redis and Celery
- @dev: Create base AI agent classes
- @qa: Write test strategy document

**Sprint 1, Iteration 1 Milestones:**

- ✅ Vector database selected
- ✅ Postgres + Redis running locally
- ✅ Base agent architecture in place
- ✅ Sprint 1 backlog ready

---

### Iteration 2: Database Migration

**@dev Tasks:**

- [ ] Migrate SQLAlchemy models to Postgres
- [ ] Install pgvector extension
- [ ] Create embeddings table schema
- [ ] Data migration script (SQLite → Postgres)
- [ ] Test rollback procedures

**@qa Tasks:**

- [ ] Test migration on staging environment
- [ ] Verify data integrity post-migration
- [ ] Performance benchmarks (before/after)
- [ ] Write migration test cases

**@architect Tasks:**

- [ ] Review migration code
- [ ] Document schema changes
- [ ] Update API_DOCS.md with new endpoints

**Sprint 1, Iteration 2 Milestones:**

- ✅ Database migrated to Postgres
- ✅ Zero data loss verified
- ✅ Rollback plan tested

---

### Iteration 3: First AI Agent - Auto-Geocoding (US4.1)

**@dev Tasks:**

- [ ] Implement data enrichment agent
- [ ] Integrate Nominatim geocoding API
- [ ] Create Celery task: `enrich_listing(listing_id)`
- [ ] Add task queue on listing creation
- [ ] Error handling and retry logic

**@qa Tasks:**

- [ ] Test geocoding with 100+ addresses
- [ ] Verify accuracy (lat/lng correct?)
- [ ] Test failure scenarios (invalid address)
- [ ] Load test: 1000 concurrent geocoding requests

**@ux-expert Tasks:**

- [ ] Design address input with auto-preview
- [ ] "Verifying location..." loading state
- [ ] Map preview during listing creation

**Sprint 1, Iteration 3 Milestones:**

- ✅ Auto-geocoding working on all new listings
- ✅ 95%+ accuracy on valid addresses
- ✅ Graceful degradation on failures

---

### Iteration 4: Quality Scoring (US4.3) & Sprint Review

**@dev Tasks:**

- [ ] Implement quality scoring algorithm
- [ ] Calculate on listing create/update
- [ ] Store quality_score in listings table
- [ ] Use score in ranking algorithm

**@qa Tasks:**

- [ ] Validate scoring logic
- [ ] Test edge cases (minimal listings)
- [ ] Performance impact assessment

**@po Tasks:**

- [ ] Review completed stories
- [ ] Accept or request changes
- [ ] Update release notes

**@sm Tasks:**

- [ ] Sprint review demo
- [ ] Sprint retrospective
- [ ] Calculate velocity for Sprint 2 planning

**Sprint 1 Complete - Milestones:**

- ✅ Sprint 1 complete (US4.1, US4.3)
- ✅ Auto-geocoding + quality scoring live
- ✅ Sprint 2 backlog ready

---

## 📅 Sprint 2: Intelligence (4 Iterations)

### Sprint 2, Iteration 1: Vector Database Setup

**@dev Tasks:**

- [ ] Sign up for Pinecone (trial) or deploy Weaviate
- [ ] Install sentence-transformers library
- [ ] Generate embeddings for all existing listings
- [ ] Implement embedding generation pipeline
- [ ] Create embeddings on new listing creation

**@architect Tasks:**

- [ ] Design vector search API
- [ ] Define embedding model (all-MiniLM-L6-v2)
- [ ] Caching strategy for embeddings

**@qa Tasks:**

- [ ] Test embedding generation performance
- [ ] Verify vector storage and retrieval
- [ ] Generate test queries for iteration 2

**Sprint 2, Iteration 1 Milestones:**

- ✅ Vector database operational
- ✅ All listings have embeddings
- ✅ Ready for semantic search implementation

---

### Sprint 2, Iteration 2: Semantic Search (US5.1)

**@dev Tasks:**

- [ ] Implement NLP agent for query parsing
- [ ] Build semantic search endpoint: GET /api/search?semantic=true
- [ ] Vector similarity search with Pinecone/Weaviate
- [ ] Re-ranking algorithm (location, recency, quality)
- [ ] Response time optimization (<500ms)

**@qa Tasks:**

- [ ] Test with 50+ natural language queries
- [ ] Measure relevance (user survey)
- [ ] Performance benchmarks
- [ ] A/B test: semantic vs keyword search

**@ux-expert Tasks:**

- [ ] Design search results page
- [ ] "Because you searched for..." explanations
- [ ] Highlight matching keywords

**Sprint 2, Iteration 2 Milestones:**

- ✅ Semantic search live and working
- ✅ >4/5 relevance score from testers
- ✅ <500ms response time (p95)

---

### Sprint 2, Iteration 3: Personalized Recommendations (US5.2)

**@dev Tasks:**

- [ ] Implement matching agent
- [ ] Build user embedding from profile + behavior
- [ ] GET /api/recommendations/:user_id endpoint
- [ ] Cache recommendations in Redis
- [ ] Background job: refresh every 4 hours

**@ux-expert Tasks:**

- [ ] Design "Recommended for You" section
- [ ] Homepage layout with personalization
- [ ] Empty state (new users)

**@qa Tasks:**

- [ ] Test recommendation quality
- [ ] Verify cache invalidation
- [ ] Cold start problem (new users)

**Sprint 2, Iteration 3 Milestones:**

- ✅ Personalized recommendations working
- ✅ 40%+ click-through rate
- ✅ Homepage updated with recommendations

---

### Sprint 2, Iteration 4: Sprint Review & Optimization

**@dev Tasks:**

- [ ] Performance optimization
- [ ] Code refactoring and cleanup
- [ ] Documentation updates

**@qa Tasks:**

- [ ] Regression testing
- [ ] User acceptance testing
- [ ] Bug fixes

**@pm Tasks:**

- [ ] Stakeholder demo
- [ ] Gather feedback
- [ ] Adjust Sprint 3 priorities if needed

**Sprint 2 Complete - Milestones:**

- ✅ Sprint 2 complete (US5.1, US5.2)
- ✅ AI search and recommendations live
- ✅ User feedback incorporated

---

## 📅 Sprint 3: Real-Time (4 Iterations)

### Sprint 3, Iteration 1: Urgent Matching System (US6.1)

**@dev Tasks:**

- [ ] Create urgent_requests table
- [ ] Implement urgent matching agent
- [ ] POST /api/urgent-match endpoint
- [ ] Find available providers algorithm
- [ ] Scoring and ranking logic

**@architect Tasks:**

- [ ] Design real-time notification architecture
- [ ] WebSocket or Server-Sent Events?
- [ ] Message queue for alerts

**@qa Tasks:**

- [ ] Test matching accuracy
- [ ] Verify urgency scoring
- [ ] Load test: 100 urgent requests/hour

**Sprint 3, Iteration 1 Milestones:**

- ✅ Urgent matching working
- ✅ Correct providers identified
- ✅ Ready for alert implementation

---

### Sprint 3, Iteration 2: Real-Time Alerts (US6.2)

**@dev Tasks:**

- [ ] Implement WebSocket server
- [ ] Push notification service integration
- [ ] Alert delivery to top 5 providers
- [ ] Response tracking system
- [ ] First-come-first-served logic

**@ux-expert Tasks:**

- [ ] Design urgent alert notification (mobile + desktop)
- [ ] One-tap accept/decline UI
- [ ] Alert sound and vibration
- [ ] Badge/counter for unread alerts

**@qa Tasks:**

- [ ] Test alert delivery (100% success rate)
- [ ] Measure delivery time (<30 seconds)
- [ ] Test concurrent alerts (multiple urgent needs)

**Sprint 3, Iteration 2 Milestones:**

- ✅ Real-time alerts working
- ✅ <30 second delivery time
- ✅ 100% delivery success rate

---

### Sprint 3, Iteration 3: Availability Toggle (US6.3)

**@dev Tasks:**

- [ ] Create provider_availability table
- [ ] PATCH /api/providers/:id/availability endpoint
- [ ] "Available Now" toggle in UI
- [ ] Calendar integration (Google/Apple)
- [ ] Auto-sync availability every 15 minutes

**@ux-expert Tasks:**

- [ ] Design availability toggle (prominent, easy)
- [ ] Status indicator on profile
- [ ] Calendar sync setup flow

**@qa Tasks:**

- [ ] Test toggle functionality
- [ ] Verify calendar sync
- [ ] Test auto-availability detection

**Sprint 3, Iteration 3 Milestones:**

- ✅ Availability toggle working
- ✅ Calendar integration functional
- ✅ Providers can control alert frequency

---

### Sprint 3, Iteration 4: Sprint Review, Testing & Launch

**@dev Tasks:**

- [ ] Code freeze
- [ ] Bug fixes only
- [ ] Performance tuning
- [ ] Documentation finalization

**@qa Tasks:**

- [ ] Full regression test suite
- [ ] Load testing (10K concurrent users)
- [ ] Security audit
- [ ] User acceptance testing

**@pm Tasks:**

- [ ] Launch planning
- [ ] Marketing materials
- [ ] Blog post: "How AI Powers Tapin"
- [ ] User onboarding guide

**@sm Tasks:**

- [ ] Sprint 3 retrospective
- [ ] Phase 2 completion report
- [ ] Phase 3 planning kickoff

**Sprint 3 Complete - Final Milestones:**

- ✅ Phase 2 complete and launched
- ✅ 3 AI features live (geocoding, search, urgent matching)
- ✅ Success metrics achieved
- ✅ Phase 3 planned

---

## 📊 Success Metrics (Phase 2)

### Technical Metrics

- [ ] Semantic search response time: <500ms (p95)
- [ ] Geocoding success rate: >95%
- [ ] Alert delivery time: <30 seconds
- [ ] Database migration: Zero data loss
- [ ] API uptime: >99.5%

### User Impact Metrics

- [ ] Search relevance: >4/5 stars (user survey)
- [ ] Recommendation CTR: >40%
- [ ] Urgent match success rate: >80%
- [ ] User retention: >60% at 30 days
- [ ] Net Promoter Score: >50

### Business Metrics

- [ ] 30% increase in successful matches
- [ ] 20% reduction in "no results found"
- [ ] 50+ new service providers signed up
- [ ] Zero increase in support tickets

---

## 🚨 Risk Management

### High Priority Risks

**Risk 1: Vector Database Performance**

- **Likelihood:** Medium
- **Impact:** High
- **Mitigation:** @analyst to benchmark all options in Sprint 1, Iteration 1
- **Owner:** @architect + @dev

**Risk 2: ML Model Accuracy**

- **Likelihood:** Medium
- **Impact:** High
- **Mitigation:** Test with diverse queries, fallback to keyword search
- **Owner:** @dev + @qa

**Risk 3: Database Migration Downtime**

- **Likelihood:** Low
- **Impact:** Critical
- **Mitigation:** Detailed rollback plan, staging test, backup before migration
- **Owner:** @architect + @dev

**Risk 4: Real-Time Alert Scale**

- **Likelihood:** Medium
- **Impact:** Medium
- **Mitigation:** Load testing in Sprint 1, Iteration 10, fallback to email alerts
- **Owner:** @dev + @qa

---

## 📞 Communication & Ceremonies

### Daily Standups

- **Format:** Async updates via GitHub Issues/Project Board
- **Questions:** What did you do? What will you do? Any blockers?
- **Facilitator:** @sm

### Sprint Planning

- **Frequency:** Every 4 iterations
- **Attendees:** All agents
- **Facilitator:** @sm
- **Outcome:** Sprint backlog committed

### Sprint Review

- **Frequency:** End of each sprint
- **Attendees:** All agents + stakeholders
- **Facilitator:** @pm
- **Outcome:** Demo + feedback

### Sprint Retrospective

- **Frequency:** End of each sprint
- **Attendees:** Core team only
- **Facilitator:** @sm
- **Outcome:** Process improvements

### Coordination Sync

- **Frequency:** As needed
- **Attendees:** @pm, @architect, @dev, @sm
- **Outcome:** Remove blockers, adjust priorities

---

## 📋 Immediate Action Items

### @analyst

- [ ] Research vector databases (Pinecone vs Weaviate vs pgvector)
- [ ] Create comparison matrix with pros/cons/pricing
- [ ] Provide recommendation

### @architect

- [ ] Design Postgres migration plan
- [ ] Document new database schema
- [ ] Create Docker Compose file for local dev
- [ ] Submit for review

### @dev

- [ ] Set up Postgres locally
- [ ] Install Redis + Celery
- [ ] Create base AI agent classes
- [ ] Test environment ready

### @po

- [ ] Refine US4.1 (Auto-geocoding) acceptance criteria
- [ ] Refine US4.3 (Quality scoring) acceptance criteria
- [ ] Prepare Sprint 1 backlog
- [ ] Grooming session scheduled

### @qa

- [ ] Write AI test strategy document
- [ ] Set up test data generator
- [ ] Define performance benchmarks
- [ ] Ready for iteration 2 testing

### @ux-expert

- [ ] Draft "Invisible AI" design principles
- [ ] Sketch recommendation section layouts
- [ ] Submit for @pm review

### @sm

- [ ] Configure sprint coordination
- [ ] Set up project tracking (GitHub Projects)
- [ ] Create Sprint 1 board
- [ ] Initial sprint coordination

### @pm

- [ ] Sprint 1 goals finalized
- [ ] Stakeholder communication plan
- [ ] Risk register created
- [ ] Weekly report template

---

## 🎯 Definition of Done

A user story is DONE when:

- [ ] Code implemented and passes all tests
- [ ] Unit tests written (80%+ coverage)
- [ ] Integration tests pass
- [ ] Code reviewed and approved by @architect
- [ ] QA tested and approved by @qa
- [ ] UX reviewed and approved by @ux-expert
- [ ] Documentation updated
- [ ] Deployed to staging environment
- [ ] Product owner accepts (@po)
- [ ] Release notes written

---

## 📖 Key Documents Reference

- **[AI-PRODUCT-ROADMAP.md](AI-PRODUCT-ROADMAP.md)** - All 47 user stories
- **[AI-ARCHITECTURE-STRATEGY.md](AI-ARCHITECTURE-STRATEGY.md)** - AI agent details
- **[ARCHITECTURE-VISUAL.md](ARCHITECTURE-VISUAL.md)** - System diagrams
- **[EXEC-SUMMARY.md](EXEC-SUMMARY.md)** - Executive overview

---

## 🚀 Let's Build Something Incredible!

Phase 2 starts NOW. Each agent knows their role. The roadmap is clear. Let's ship AI features that delight users and scale to thousands!

**Next Milestone:** Sprint 1 Complete (First AI agent live!)

---

**Status:** Ready for execution  
**Last Updated:** November 3, 2025  
**Orchestrated by:** @bmad-orchestrator
