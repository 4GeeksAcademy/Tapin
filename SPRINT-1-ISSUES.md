# Phase 2 Sprint 1 - Agent Assignments & Issues

**Created:** November 3, 2025  
**Phase:** Phase 2 - AI Infrastructure Setup  
**Sprint:** Sprint 1 (4 Iterations)  
**Status:** Issues Created & Assigned

---

## 🎯 Issue Tracker - All Sprint 1 Tasks

### @analyst - Vector Database Research

**Issue #1: [ANALYST] Vector Database Research & Recommendation**

```
## Objective
Research and recommend optimal vector database (Pinecone vs Weaviate vs pgvector) for Tapin's semantic search

## Context
Phase 2 AI infrastructure foundation depends on this decision. Performance, cost, and scalability impact platform for 2+ years.

## Acceptance Criteria
- [ ] Comparison matrix: Pinecone vs Weaviate vs pgvector with performance/cost/ops benchmarks
- [ ] Cost projections for 3 years (1K users, 10K users, 50K+ users)
- [ ] Risk assessment for each option with mitigation strategies
- [ ] Final recommendation with fallback option and justification

## Dependencies
- Depends on: None (can start immediately)
- Blocks: @architect design decisions, @dev infrastructure setup

## Resources
- [AI-ARCHITECTURE-STRATEGY.md](/Documents/AI-ARCHITECTURE-STRATEGY.md)
- [AI-PRODUCT-ROADMAP.md](/Documents/AI-PRODUCT-ROADMAP.md)
- Vendor docs: Pinecone, Weaviate, pgvector

## Success Looks Like
Team confident to proceed with vector DB choice. Cost/performance/risk tradeoffs clearly documented.
```

---

### @dev - Infrastructure Setup

**Issue #2: [DEV] Set up Local Postgres with pgvector**

```
## Objective
Install and configure PostgreSQL 15 locally with pgvector extension for semantic search capability

## Context
Foundation for AI infrastructure. Enables database migration from SQLite and vector-based queries.

## Acceptance Criteria
- [ ] PostgreSQL 15 installed and running locally
- [ ] pgvector extension installed and enabled
- [ ] Database "tapin_dev" created with proper schema
- [ ] SQLAlchemy ORM configured to use Postgres
- [ ] Test: Connect Flask app successfully to Postgres
- [ ] Documentation: Local setup guide written

## Dependencies
- Depends on: None
- Blocks: Issue #3 (data migration), Issue #4 (Redis/Celery)

## Resources
- PostgreSQL docs: postgresql.org
- pgvector: github.com/pgvector/pgvector
- [backend/requirements.txt](../../backend/requirements.txt)

## Success Looks Like
Flask app connects to local Postgres. Schema ready for data migration. Zero errors in test run.
```

**Issue #3: [DEV] Migrate Data: SQLite → Postgres**

```
## Objective
Safely migrate all existing data from SQLite to PostgreSQL without data loss

## Context
Required to enable new AI features. Rollback procedures must be tested.

## Acceptance Criteria
- [ ] Migration script created and tested
- [ ] All data migrated: users, listings, reviews, ratings
- [ ] Data integrity verified post-migration
- [ ] Rollback procedure tested and documented
- [ ] Backups created before migration
- [ ] Zero data loss verified

## Dependencies
- Depends on: Issue #2 (local Postgres)
- Blocks: Issue #4 (Celery integration)

## Resources
- SQLAlchemy migration tools
- [backend/database/](../../backend/database/)

## Success Looks Like
All data in Postgres. Rollback tested successfully. Migration time <5 minutes.
```

**Issue #4: [DEV] Set up Redis & Celery for Async Tasks**

```
## Objective
Install Redis and configure Celery for background task processing

## Context
AI agents need async execution. Celery + Redis enables listing enrichment, matching, and other background work.

## Acceptance Criteria
- [ ] Redis running locally (Docker or native)
- [ ] Celery configured with proper task queue settings
- [ ] First test task: process_listing() triggers on listing creation
- [ ] Task retry logic and error handling implemented
- [ ] Monitoring setup (Flower dashboard accessible)
- [ ] Documentation: How to start workers, view tasks

## Dependencies
- Depends on: Issue #2 (Postgres for task storage)
- Blocks: Issue #5 (Agent architecture)

## Resources
- Celery docs: docs.celeryproject.io
- Redis docs: redis.io
- [Celery best practices](https://docs.celeryproject.io/en/stable/getting-started/introduction.html)

## Success Looks Like
Celery worker processes 1000 tasks/minute without errors. Flower dashboard shows task health.
```

**Issue #5: [DEV] Create Base AI Agent Architecture**

```
## Objective
Build abstract BaseAgent class and first concrete agent implementation

## Context
Foundation for all 6 AI agents (data enrichment, matching, urgent matching, resource discovery, prediction, trust).

## Acceptance Criteria
- [ ] BaseAgent abstract class created with analyze(), enrich(), validate() methods
- [ ] DataEnrichmentAgent concrete implementation (auto-geocoding)
- [ ] Agent integration with Celery task queue
- [ ] Unit tests for agent base class (80%+ coverage)
- [ ] Logging and error handling for all agents
- [ ] Documentation: Agent architecture diagram

## Dependencies
- Depends on: Issue #4 (Celery)
- Blocks: Issue #6 (pgvector integration)

## Resources
- [AI-ARCHITECTURE-STRATEGY.md](/Documents/AI-ARCHITECTURE-STRATEGY.md)
- Python ABC documentation

## Success Looks Like
First agent processes 100 test listings successfully. Unit tests pass. Code reviewed.
```

**Issue #6: [DEV] Integrate pgvector & Generate Embeddings**

```
## Objective
Set up pgvector extension and create pipeline to generate embeddings for listings

## Context
Required for semantic search. Embeddings represent listing content semantically for AI matching.

## Acceptance Criteria
- [ ] pgvector extension enabled in Postgres
- [ ] Embeddings table schema created (1536 dimensions for sentence-transformers)
- [ ] Sentence-transformers model selected and integrated
- [ ] Embedding generation task in Celery (batch_generate_embeddings)
- [ ] IVFFlat indexes created for performance
- [ ] Tested with 1K sample listings

## Dependencies
- Depends on: Issue #4 (Celery), Issue #2 (Postgres)
- Blocks: Issue #7 (Semantic search)

## Resources
- pgvector: github.com/pgvector/pgvector
- sentence-transformers: huggingface.co/sentence-transformers
- [backend/requirements.txt](../../backend/requirements.txt)

## Success Looks Like
1K listings have embeddings. Query latency <100ms. Index created successfully.
```

---

### @pm - Product Management

**Issue #7: [PM] Define Phase 2 MVP & Feature Prioritization**

```
## Objective
Define minimum viable feature set for Phase 2 and prioritize 47 user stories

## Context
Team needs clear scope boundaries. 12 weeks to ship. Must balance scope vs quality.

## Acceptance Criteria
- [ ] MVP features clearly defined (must have vs nice-to-have)
- [ ] All 47 stories prioritized using MoSCoW method
- [ ] Critical path identified (dependencies mapped)
- [ ] Risk register created with top 5 risks + mitigations
- [ ] Stakeholder comms plan documented

## Dependencies
- Depends on: Issue #1 (@analyst vector DB research)
- Blocks: Issue #8 (@po story refinement)

## Resources
- [AI-PRODUCT-ROADMAP.md](/Documents/AI-PRODUCT-ROADMAP.md)
- [EXEC-SUMMARY.md](/Documents/EXEC-SUMMARY.md)

## Success Looks Like
All stakeholders aligned on MVP scope. Team can commit to sprint with confidence.
```

---

### @po - Product Owner

**Issue #8: [PO] Refine Sprint 1 User Stories & Acceptance Criteria**

```
## Objective
Define clear acceptance criteria for Sprint 1 stories (US4.1, US4.3, US5.1, US5.2)

## Context
@dev needs testable criteria. No ambiguity = no rework.

## Acceptance Criteria
- [ ] US4.1 (Auto-Geocoding): Clear acceptance criteria with test cases
- [ ] US4.3 (Quality Scoring): Metrics defined, scoring logic documented
- [ ] US5.1 (Semantic Search): Relevance standards defined
- [ ] US5.2 (Recommendations): Personalization logic defined
- [ ] All stories estimated with @dev input
- [ ] Definition of Done agreed with @qa

## Dependencies
- Depends on: Issue #7 (@pm prioritization)
- Blocks: Issue #9 (@qa test strategy)

## Resources
- [AI-PRODUCT-ROADMAP.md](/Documents/AI-PRODUCT-ROADMAP.md)

## Success Looks Like
@dev can estimate confidently. @qa knows how to test. Zero ambiguity in stories.
```

---

### @architect - System Design

**Issue #9: [ARCHITECT] Design Postgres Migration & Schema**

```
## Objective
Document Postgres schema design with migration strategy and rollback plan

## Context
@dev needs clear blueprint. Schema changes are critical and must be reversible.

## Acceptance Criteria
- [ ] Current schema analysis (SQLite → Postgres changes needed)
- [ ] New schema design with pgvector integration (embeddings column)
- [ ] Migration script strategy (forward + rollback tested)
- [ ] Performance considerations (indexes, query plans)
- [ ] Data integrity validation strategy
- [ ] Documentation: Schema diagram + migration guide

## Dependencies
- Depends on: Issue #1 (@analyst vector DB choice)
- Blocks: Issue #2 (@dev local setup), Issue #3 (@dev migration)

## Resources
- [core-architecture.md](/docs/core-architecture.md)
- Current schema: [backend/app.py](../../backend/app.py)
- PostgreSQL docs

## Success Looks Like
Clear schema diagram. Migration script reviewed. Rollback tested. Zero questions for @dev.

## Owner: @architect
```

**Issue #10: [ARCHITECT] Design Redis + Celery Architecture**

```
## Objective
Document task queue architecture with Celery + Redis configuration

## Context
AI agents need reliable async execution. Task routing, retry logic, and error handling critical.

## Acceptance Criteria
- [ ] Task topology: All AI agent tasks mapped (enrich, match, score, etc.)
- [ ] Queue strategy: High/normal/low priority queues designed
- [ ] Worker configuration: Number of processes, concurrency, timeouts
- [ ] Error handling: Dead letter queue (DLQ) strategy
- [ ] Monitoring plan: Flower dashboard setup guide
- [ ] Documentation: Architecture diagram + operational guide

## Dependencies
- Depends on: None
- Blocks: Issue #4 (@dev Redis setup), Issue #5 (@dev agents)

## Resources
- Celery docs: docs.celeryproject.io
- Redis docs: redis.io
- [AI-ARCHITECTURE-STRATEGY.md](/Documents/AI-ARCHITECTURE-STRATEGY.md)

## Success Looks Like
Clear task topology diagram. @dev can implement without questions. Monitoring plan clear.

## Owner: @architect
```

**Issue #11: [ARCHITECT] Design AI Agent Base Architecture**

```
## Objective
Document abstract base class design for all 6 AI agents

## Context
Ensures consistency, testability, and maintainability across all agents.

## Acceptance Criteria
- [ ] BaseAgent abstract class interface defined
- [ ] Methods documented: analyze(), enrich(), validate()
- [ ] Agent lifecycle documented (creation → processing → completion)
- [ ] Error handling patterns standardized
- [ ] Logging and observability strategy documented
- [ ] Unit test patterns established (mocks, fixtures, edge cases)
- [ ] Code example: DataEnrichmentAgent template

## Dependencies
- Depends on: None
- Blocks: Issue #5 (@dev agent implementation)

## Resources
- [AI-ARCHITECTURE-STRATEGY.md](/Documents/AI-ARCHITECTURE-STRATEGY.md)
- Python ABC documentation

## Success Looks Like
@dev has clear template to follow. BaseAgent design prevents future rewrites.

## Owner: @architect
```

**Issue #12: [ARCHITECT] Design API Contracts for AI Features**

```
## Objective
Document REST API endpoints, webhooks, and error responses for AI features

## Context
Frontend, backend, and agents need clear contract. Prevents integration issues.

## Acceptance Criteria
- [ ] API endpoints documented (GET /listings/{id}/enriched, POST /search/semantic, etc.)
- [ ] Request/response schemas defined (with examples)
- [ ] Webhook callbacks documented (on-enrichment-complete, on-match-found, etc.)
- [ ] Error responses standardized (error codes, messages)
- [ ] Rate limiting strategy documented
- [ ] Deprecation & versioning strategy

## Dependencies
- Depends on: Issue #11 (@architect agent design)
- Blocks: Frontend integration

## Resources
- OpenAPI/Swagger standards
- [backend/API_DOCS.md](../../backend/API_DOCS.md)

## Success Looks Like
Frontend can implement with clear API spec. Zero integration confusion.

## Owner: @architect
```

---

### @qa - Quality Assurance

**Issue #13: [QA] Create AI Test Strategy & Test Plan**

```
## Objective
Document comprehensive testing approach for AI infrastructure

## Context
AI features must be reliable. Test strategy prevents critical failures.

## Acceptance Criteria
- [ ] Unit test strategy: Test each agent component independently
- [ ] Integration test strategy: End-to-end workflows
- [ ] Performance test targets: <500ms p95 for semantic search
- [ ] Security test checklist: Input validation, injection prevention
- [ ] Data quality tests: Embeddings accuracy verification
- [ ] Test coverage goals: 80%+ for business logic
- [ ] CI/CD test automation plan

## Dependencies
- Depends on: Issue #8 (@po acceptance criteria)
- Blocks: Issue #14 (@qa test data)

## Resources
- Pytest docs
- [backend/tests/](../../backend/tests/)

## Success Looks Like
Clear test strategy. @dev knows what to test. CI/CD automation planned.

## Owner: @qa
```

**Issue #14: [QA] Create Test Data Generator**

```
## Objective
Build realistic test data scenarios for AI feature testing

## Context
Good test data catches edge cases early.

## Acceptance Criteria
- [ ] Valid address generator (US + international)
- [ ] Invalid address generator (typos, malformed, missing fields)
- [ ] Edge case generator (long names, special chars, duplicates)
- [ ] Performance load generator (1K, 10K, 100K listings)
- [ ] Test data fixtures for pytest
- [ ] Documentation: How to use test data

## Dependencies
- Depends on: Issue #13 (@qa test strategy)
- Blocks: Issue #2-6 (@dev implementation)

## Resources
- Faker library (Python)
- Pytest fixtures

## Success Looks Like
Test data covers all scenarios. @dev can run tests immediately.

## Owner: @qa
```

---

### @ux-expert - UX Design

**Issue #15: [UX] Design "Invisible AI" Design Principles**

```
## Objective
Define design principles for AI features that are invisible but delightful

## Context
Users should trust AI without seeing complexity.

## Acceptance Criteria
- [ ] 5 core design principles documented (trust, speed, control, graceful failure, transparency)
- [ ] Design pattern library (components for recommendations, loading, errors)
- [ ] "Why this match?" explanation UI mockups
- [ ] Loading state designs (show progress during AI processing)
- [ ] Error state designs (graceful fallback when AI fails)
- [ ] Mobile-first approach validated

## Dependencies
- Depends on: None
- Blocks: Issue #16 (@ux mockups)

## Resources
- [frontend/src/](../../frontend/src/)
- Design system docs

## Success Looks Like
Clear design guidelines. Team knows how AI should feel to users.

## Owner: @ux-expert
```

**Issue #16: [UX] Create Mockups: Search Results & Recommendations**

```
## Objective
Design UI mockups for semantic search and AI recommendations

## Context
Frontend implementation depends on visual designs.

## Acceptance Criteria
- [ ] Search results page mockup (with AI match confidence scores)
- [ ] "Recommended for You" section mockup
- [ ] "Why this match?" tooltip explanations
- [ ] Loading state animations during AI processing
- [ ] Error state designs (when auto-verification fails)
- [ ] Mobile layout validated

## Dependencies
- Depends on: Issue #15 (@ux principles)
- Blocks: Frontend implementation

## Resources
- Figma or design tool
- [frontend/](../../frontend/)

## Success Looks Like
Frontend can implement from mockups. Users understand AI recommendations.

## Owner: @ux-expert
```

---

### @sm - Scrum Master

**Issue #17: [SM] Set up GitHub Project Board for Sprint 1**

```
## Objective
Configure GitHub Project Board with all sprint work items and tracking

## Context
Team needs visibility into progress and blockers.

## Acceptance Criteria
- [ ] GitHub Project Board created (board view with status columns)
- [ ] All issues added to sprint (Issues #1-16 above)
- [ ] Status columns configured: Backlog → Todo → In Progress → Review → Done
- [ ] Sprint settings configured (1 iteration cycle)
- [ ] Automation rules created (auto-move on PR activity)
- [ ] Daily standup template created (template issue for daily updates)

## Dependencies
- Depends on: None
- Blocks: All other work starts

## Resources
- GitHub Projects documentation

## Success Looks Like
Project board reflects all work. Team updates daily. Progress visible to all.

## Owner: @sm
```

**Issue #18: [SM] Establish Blocker Resolution Process**

```
## Objective
Create process to identify, escalate, and resolve blockers daily

## Context
Blockers can paralyze progress. Quick resolution critical.

## Acceptance Criteria
- [ ] Blocker template created (issue template)
- [ ] Daily blocker check-in process documented
- [ ] Escalation path defined (@sm → @pm/@architect → decision)
- [ ] Maximum 24-hour resolution target documented
- [ ] Blocker tracking dashboard or report

## Dependencies
- Depends on: Issue #17 (@sm project board)
- Blocks: Nothing, runs in parallel

## Resources
- None

## Success Looks Like
Blockers resolved within 24 hours. No work pauses due to blockers.

## Owner: @sm
```

---

## 📊 Agent Assignment Summary

| Agent          | Issue Count | Issues             | Priority                            |
| -------------- | ----------- | ------------------ | ----------------------------------- |
| **@architect** | 4           | #9, #10, #11, #12  | HIGHEST - Blocks all others         |
| **@dev**       | 5           | #2, #3, #4, #5, #6 | HIGH - Depends on #9, #10, #11      |
| **@analyst**   | 1           | #1                 | HIGH - Blocks @pm, @architect       |
| **@pm**        | 1           | #7                 | MEDIUM - Depends on #1              |
| **@po**        | 1           | #8                 | MEDIUM - Depends on #7              |
| **@qa**        | 2           | #13, #14           | MEDIUM - Parallel work              |
| **@ux-expert** | 2           | #15, #16           | MEDIUM - Parallel work              |
| **@sm**        | 2           | #17, #18           | CRITICAL - Setup only, then ongoing |

---

## 🚀 Sprint 1 - Execution Order

**Immediately (Now):**

1. @sm: Create Project Board (Issue #17)
2. @sm: Create Blocker Resolution (Issue #18)
3. @analyst: Start Vector DB research (Issue #1)

**Parallel (Week 1):** 4. @architect: Design all 4 architecture issues (#9-12) - START NOW 5. @pm: Start prioritization when @analyst done (Issue #7) 6. @qa: Create test strategy & data generators (#13-14) 7. @ux-expert: Design principles (#15-16)

**Week 2+ (Dependent on architecture):** 8. @dev: Implement infrastructure (Issues #2-6 once @architect designs ready) 9. @po: Refine stories once @pm done (Issue #8)

---

**Status:** All issues documented and ready for assignment  
**Next Step:** Create in GitHub Issues and assign to agents
