# @Architect - Sprint 1 Architecture Designs (Phase 2 Future)

**Status:** IN PROGRESS  
**Sprint:** Sprint 1, Iteration 1  
**Start Date:** November 3, 2025  
**Owner:** @architect (GitHub Copilot)  
**Phase:** Phase 2 (FUTURE Implementation Building on Phase 1)

---

## 🚨 Important: This Is Phase 2 Future Work

```
Phase 1 (CURRENT - Working):
├─ SQLite database ✅
├─ Flask backend ✅
├─ React frontend ✅
└─ Basic features ✅

Phase 2 (FUTURE - Designed Here):
├─ PostgreSQL (migration from SQLite)
├─ Redis + Celery (adds async processing)
├─ 6 AI agents (new intelligence layer)
├─ Semantic search (enhancement)
└─ All builds on Phase 1 foundation

What @architect is designing:
→ The FUTURE infrastructure (Phase 2, Sprint 1-3)
→ How to enhance Phase 1 with AI capabilities
→ Not replacing anything, just adding features
```

---

## 📋 Issues to Complete (In Order)

### HIGH PRIORITY - COMPLETE THIS ITERATION

1. **#34** - PostgreSQL Migration & Schema Design
2. **#35** - Redis + Celery Architecture
3. **#36** - AI Agent Base Architecture
4. **#37** - API Contracts (depends on others)

---

## 🏗️ Issue #34: PostgreSQL Migration & Schema Design

### 🚨 Important: This Is a MIGRATION, Not Replacement

```
Phase 1 (Current):
└─ SQLite database (working fine)

Phase 2 (Future - This Issue):
├─ Migrate ALL data from SQLite → PostgreSQL
├─ Keep ALL existing data (nothing lost)
├─ Add NEW capabilities on top
│  ├─ pgvector for embeddings
│  ├─ Enhanced schema for AI features
│  └─ Better performance at scale
└─ All Phase 1 features still work ✅

Why migrate?
- PostgreSQL is more scalable than SQLite
- pgvector extension enables semantic search
- Better for production deployment
- Can handle more concurrent users

Phase 1 data: PRESERVED ✅
Phase 1 functionality: PRESERVED ✅
```

### Objective

Document PostgreSQL schema design with migration strategy and rollback plan for Phase 2 AI features (FUTURE enhancement to Phase 1).

### Key Deliverables

1. **Current State Analysis**
   - SQLite schema inventory (all tables, columns, relationships)
   - Identify tables affected by Phase 2 AI features
   - Document current indexes and constraints

2. **New Schema Design (pgvector Integration)**
   - Extend Listing model with embeddings column (vector(1536))
   - Create Embedding table: `embeddings` (id, listing_id, vector, model_version, created_at)
   - Add indexes for vector similarity search
   - Plan for other AI-related columns (quality_score, urgency_level, etc.)

3. **Schema Diagram (ERD)**
   - Current schema visualization
   - Proposed schema with pgvector
   - Entity relationships highlighted

4. **Migration Strategy**
   - Forward migration script (SQLite → Postgres)
   - Rollback procedure
   - Data validation checks
   - Performance considerations

5. **Documentation**
   - Schema migration guide (step-by-step)
   - Rollback procedures
   - Index strategy and maintenance

### Current Schema to Migrate

```python
# From backend/app.py (current SQLite schema)
- User (id, username, email, password_hash, created_at, updated_at)
- Listing (id, user_id, title, description, category, location, created_at, status)
- Review (id, listing_id, user_id, rating, comment, created_at)
- SignUp (id, listing_id, user_id, created_at, status)
```

### New Phase 2 Tables to Add

```sql
-- Embeddings table for semantic search
CREATE TABLE embeddings (
    id SERIAL PRIMARY KEY,
    listing_id INTEGER NOT NULL REFERENCES listings(id),
    vector vector(1536),
    model_version VARCHAR(50),
    generated_at TIMESTAMP DEFAULT NOW(),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for vector similarity
CREATE INDEX idx_embeddings_listing ON embeddings(listing_id);
CREATE INDEX idx_embeddings_vector ON embeddings USING ivfflat (vector vector_cosine_ops);
```

### Questions for @analyst (#26)

- [ ] Based on vector DB recommendation, confirm embedding dimension (1536 vs 384)
- [ ] Any specific index strategy recommendations?

### Acceptance Criteria

- [ ] ✅ Current schema documented
- [ ] ✅ New schema design with pgvector integration
- [ ] ✅ ERD diagram created
- [ ] ✅ Migration script strategy documented
- [ ] ✅ Rollback procedures documented
- [ ] ✅ @dev can implement without questions

### Next Steps

→ Share with @dev for #27 (PostgreSQL Setup)

---

## 🏗️ Issue #35: Redis + Celery Architecture

### 🚨 Important: This ADDS to Flask, Doesn't Replace It

```
Phase 1 (Current):
├─ Flask app (synchronous) ✅
└─ Users wait for responses

Phase 2 (Future - This Issue):
├─ Flask app (unchanged) ✅
├─ + Redis (message queue)
├─ + Celery (background workers)
└─ Users get instant response, work happens in background ✅

What this enables:
├─ Async geocoding (doesn't block users)
├─ Async embedding generation (doesn't block users)
├─ Async quality scoring (doesn't block users)
├─ All while Phase 1 API still responds instantly ✅

No breaking changes:
- Phase 1 API unchanged ✅
- Phase 1 responses still instant ✅
- New tasks processed in background ✅
- Existing features unaffected ✅
```

### Objective

Document task queue architecture with Celery + Redis configuration for AI agent execution (FUTURE enhancement for Phase 2 background processing).

### Key Deliverables

1. **Task Topology Map**
   - List all AI agent tasks: `process_listing`, `generate_embedding`, `find_matches`, `score_quality`, `detect_urgency`, `calculate_trust_score`
   - Task dependencies and prerequisites
   - Estimated processing time per task

2. **Queue Strategy**

   ```
   High Priority Queues:
   - urgent_matches (urgent need fulfillment)
   - trust_scoring (security-sensitive)

   Normal Priority Queues:
   - listing_enrichment (auto-geocoding, quality scoring)
   - semantic_matching (finding matches)
   - embeddings_generation (batch embedding)

   Low Priority Queues:
   - analytics (reporting)
   - cleanup (maintenance tasks)
   ```

3. **Worker Configuration**
   - Number of worker processes (recommend: 2-4 per CPU core)
   - Concurrency settings per task type
   - Timeout values (recommend: 5min baseline, 30min for embeddings)
   - Task heartbeat settings

4. **Error Handling Strategy**
   - Dead Letter Queue (DLQ) for failed tasks
   - Retry logic: exponential backoff (3-5 retries)
   - Error notifications (log + optional alert)
   - Manual retry mechanism

5. **Monitoring Plan**
   - Flower dashboard configuration
   - Key metrics to track: task count, success rate, avg latency
   - Alert thresholds: >5% failure rate, >10min latency

6. **Documentation**
   - Architecture diagram showing task flows
   - Operational guide: start/stop/monitor workers
   - Troubleshooting guide

### Architecture Diagram (ASCII)

```
┌─────────────────────────────────────────────────────────────┐
│                    Flask Web Application                      │
│  (Receives requests, enqueues tasks)                         │
└──────────────┬──────────────────────────────────────────────┘
               │
               ├─→ POST /listings/{id}
               ├─→ POST /search/semantic
               └─→ GET /matches/recommended
                        │
                        ↓
        ┌────────────────────────────────────┐
        │    Redis Message Broker            │
        │  (Stores task queue, messages)     │
        │                                    │
        │  Queues:                          │
        │  - urgent_matches                 │
        │  - listing_enrichment             │
        │  - semantic_matching              │
        │  - embeddings_generation          │
        └────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
   [Worker 1]    [Worker 2]    [Flower Dashboard]
   (Processes    (Processes    (Monitoring)
    enrichment,   matching,
    geocoding)    embeddings)

Task Results → PostgreSQL → Web API → Frontend
```

### Task Flow Examples

**Example 1: List Enrichment Flow**

```
1. User creates listing
2. Flask enqueues: process_listing(listing_id)
3. Worker picks up task
4. Auto-geocoding (get lat/long from address)
5. Quality scoring (analyze description, photos, etc.)
6. Update database
7. Return success
```

**Example 2: Semantic Search Flow**

```
1. User searches for "volunteer planting event"
2. Generate embedding from query
3. PostgreSQL vector similarity search
4. Return top 10 matches with scores
5. Frontend shows results (async, <500ms)
```

### Configuration Template

```python
# celery_config.py
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

CELERY_TASK_DEFAULT_QUEUE = 'default'
CELERY_TASK_QUEUES = {
    'urgent_matches': {'exchange': 'urgent'},
    'listing_enrichment': {'exchange': 'enrichment'},
    'semantic_matching': {'exchange': 'matching'},
    'embeddings_generation': {'exchange': 'embeddings'},
    'analytics': {'exchange': 'analytics'},
}

CELERY_TASK_ROUTES = {
    'tasks.urgency.*': {'queue': 'urgent_matches'},
    'tasks.enrich.*': {'queue': 'listing_enrichment'},
    'tasks.match.*': {'queue': 'semantic_matching'},
    'tasks.embed.*': {'queue': 'embeddings_generation'},
}

# Retry strategy: 3 attempts with exponential backoff
CELERY_TASK_ACKS_LATE = True
CELERY_TASK_REJECT_ON_WORKER_LOST = True
```

### Questions for @analyst (#26)

- [ ] Does vector DB choice impact Celery design?
- [ ] Any performance considerations for embedding generation at scale?

### Acceptance Criteria

- [ ] ✅ Task topology documented with all 6 AI agent tasks
- [ ] ✅ Queue strategy with routing rules clear
- [ ] ✅ Worker configuration recommended
- [ ] ✅ Error handling strategy (DLQ, retries, alerts)
- [ ] ✅ Monitoring plan (Flower, metrics, thresholds)
- [ ] ✅ Architecture diagram created
- [ ] ✅ Operational guide written
- [ ] ✅ @dev can implement without questions

### Next Steps

→ Share with @dev for #29 (Redis & Celery Setup)

---

## 🏗️ Issue #36: AI Agent Base Architecture

### 🚨 Important: These Are NEW Agents, Not Replacing Phase 1

```
Phase 1 (Current):
├─ Basic matching (manual) ✅
├─ User signup (manual) ✅
└─ Simple search (text-based) ✅

Phase 2 (Future - This Issue):
├─ 6 new AI agents (in background)
├─ DataEnrichmentAgent (auto-geocoding, quality scores)
├─ SemanticMatchingAgent (intelligent matching)
├─ UrgencyDetectionAgent (urgent need detection)
├─ TrustScoringAgent (volunteer trustworthiness)
├─ PredictiveAgent (predict good fits)
└─ ResourceDiscoveryAgent (match resources to needs)

How they work:
- Users use Phase 1 API as normal ✅
- Agents process in background (Celery tasks)
- Enhanced results available via Phase 2 API
- All Phase 1 features still work ✅

No replacement:
- Phase 1 features STAY ✅
- Phase 2 agents are ADDITIONS ✅
- Users choose old or new features ✅
```

### Objective

Document abstract base class design for all 6 AI agents (FUTURE Phase 2 feature for intelligent background processing).

### Key Deliverables

1. **BaseAgent Abstract Class**

```python
from abc import ABC, abstractmethod
from typing import Any, Dict, List
import logging

class BaseAgent(ABC):
    """
    Abstract base class for all AI agents in Tapin.

    Ensures consistency in:
    - Input/output handling
    - Error management
    - Logging and observability
    - Testing patterns
    """

    def __init__(self, agent_name: str, config: Dict[str, Any] = None):
        self.agent_name = agent_name
        self.config = config or {}
        self.logger = logging.getLogger(f"agent.{agent_name}")

    @abstractmethod
    def analyze(self, data: Any) -> Dict[str, Any]:
        """
        Analyze input data and return structured output.

        Args:
            data: Input data to analyze (varies by agent)

        Returns:
            Dict with keys: status, result, confidence, errors
            {
                'status': 'success' | 'partial' | 'failed',
                'result': {...},
                'confidence': 0.0-1.0,
                'errors': [list of errors if any],
                'metadata': {'processing_time': X, 'version': 'v1'}
            }
        """
        pass

    @abstractmethod
    def enrich(self, data: Any) -> Dict[str, Any]:
        """
        Enrich data with additional information.
        """
        pass

    @abstractmethod
    def validate(self, result: Dict[str, Any]) -> bool:
        """
        Validate the agent's output before persistence.

        Returns: True if valid, False otherwise
        """
        pass

    def execute(self, data: Any) -> Dict[str, Any]:
        """
        Execute agent workflow: analyze → enrich → validate.

        This is the main entry point called by Celery tasks.
        """
        try:
            self.logger.info(f"Starting {self.agent_name} analysis")

            # Step 1: Analyze
            analysis = self.analyze(data)
            if analysis['status'] == 'failed':
                self.logger.error(f"Analysis failed: {analysis['errors']}")
                return analysis

            # Step 2: Enrich
            enriched = self.enrich(analysis['result'])
            self.logger.info(f"Enrichment complete")

            # Step 3: Validate
            if not self.validate(enriched):
                self.logger.error("Validation failed")
                return {
                    'status': 'failed',
                    'errors': ['Validation failed'],
                    'metadata': {'processing_time': 0}
                }

            return {
                'status': 'success',
                'result': enriched,
                'confidence': enriched.get('confidence', 0.9),
                'errors': [],
                'metadata': {'version': '1.0'}
            }

        except Exception as e:
            self.logger.error(f"Exception in {self.agent_name}: {str(e)}")
            return {
                'status': 'failed',
                'errors': [str(e)],
                'metadata': {'error_type': type(e).__name__}
            }
```

2. **Concrete Implementation Example: DataEnrichmentAgent**

```python
class DataEnrichmentAgent(BaseAgent):
    """
    Enriches listings with auto-geocoding and quality scoring.
    """

    def __init__(self, config: Dict[str, Any] = None):
        super().__init__("DataEnrichmentAgent", config)
        self.geocoder = GeocodingService()  # Dependency injection
        self.quality_scorer = QualityScorer()

    def analyze(self, listing: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and analyze listing data."""
        try:
            # Extract address
            address = f"{listing['street']}, {listing['city']}, {listing['state']}"

            # Geocode
            coords = self.geocoder.geocode(address)

            # Quality score
            quality = self.quality_scorer.score(listing)

            return {
                'status': 'success',
                'result': {
                    'listing_id': listing['id'],
                    'latitude': coords['lat'],
                    'longitude': coords['lon'],
                    'quality_score': quality,
                },
                'confidence': 0.95,
                'errors': []
            }
        except Exception as e:
            return {
                'status': 'failed',
                'errors': [str(e)],
                'result': None
            }

    def enrich(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Add additional enrichment (geocoding data, etc.)."""
        # Add neighborhood, zip code, demographics
        return {
            **result,
            'neighborhood': self.geocoder.get_neighborhood(result['latitude']),
            'zip_code': self.geocoder.get_zip_code(result['latitude']),
        }

    def validate(self, result: Dict[str, Any]) -> bool:
        """Validate enriched data."""
        return (
            'latitude' in result and
            'longitude' in result and
            'quality_score' in result
        )
```

3. **Agent Lifecycle Documentation**

```
CREATE → CONFIGURE → EXECUTE → PERSIST → LOG

Phase 1: CREATE
  - Instantiate agent with config
  - Load dependencies (geocoder, scorer, models)
  - Initialize logging

Phase 2: CONFIGURE
  - Set timeout (5 min default)
  - Set retry policy (3 attempts)
  - Set error handling (DLQ on final failure)

Phase 3: EXECUTE
  - Call agent.execute(data)
  - Monitor for errors/timeout
  - Collect metrics (duration, confidence, etc.)

Phase 4: PERSIST
  - Save results to database
  - Update listing with enriched data
  - Record success/failure

Phase 5: LOG
  - Log execution metrics
  - Track performance (latency, confidence)
  - Generate alerts if needed
```

4. **Error Handling Patterns**

```python
# Pattern 1: Graceful Degradation
# If auto-geocoding fails, use user-provided coordinates
def analyze(self, listing):
    try:
        coords = self.geocoder.geocode(listing['address'])
    except GeocodingError:
        coords = {
            'lat': listing.get('manual_lat'),
            'lon': listing.get('manual_lon'),
            'source': 'manual'
        }
    return {'status': 'partial', 'result': coords}

# Pattern 2: Retry with Backoff
# Celery decorator handles this
@app.task(
    autoretry_for=(TemporaryError,),
    retry_kwargs={'max_retries': 3},
    retry_backoff=True,
    retry_backoff_max=600,
    retry_jitter=True,
)
def process_listing(listing_id):
    agent = DataEnrichmentAgent()
    return agent.execute(listing_id)

# Pattern 3: Dead Letter Queue
# If task fails after retries, move to DLQ for manual review
def on_failure_handler(self, exc, task_id, args, kwargs, einfo):
    logger.error(f"Task {task_id} failed permanently: {exc}")
    # Move to DLQ (database table for manual review)
    FailedTask.create(task_id=task_id, error=str(exc))
```

5. **Testing Patterns**

```python
# Unit test example
def test_data_enrichment_agent_with_valid_address():
    agent = DataEnrichmentAgent()
    listing = {
        'id': 1,
        'street': '123 Main St',
        'city': 'Houston',
        'state': 'TX',
    }
    result = agent.execute(listing)

    assert result['status'] == 'success'
    assert 'latitude' in result['result']
    assert result['confidence'] > 0.8

# Mock test (avoid external API calls)
@patch('agents.GeocodingService')
def test_with_mock_geocoder(mock_geocoder):
    mock_geocoder.geocode.return_value = {'lat': 29.76, 'lon': -95.37}
    agent = DataEnrichmentAgent()
    result = agent.execute({...})
    mock_geocoder.geocode.assert_called_once()
```

6. **Unit Test Strategy**

```
Test Coverage Goals: 80%+

Test Categories:
1. Happy Path Tests
   - Valid input → Success
   - Result matches schema

2. Edge Case Tests
   - Empty data
   - Null values
   - Unicode characters
   - Very long strings

3. Error Handling Tests
   - External service fails (geocoding timeout)
   - Invalid data (missing fields)
   - Data validation failures

4. Performance Tests
   - Process 100 listings < 5 seconds
   - Memory usage < 100MB

5. Integration Tests
   - Full workflow: analyze → enrich → validate → persist
   - Database integration
   - Celery task execution
```

### Questions to Resolve

- [ ] Should we use Pydantic for data validation? (recommend: YES)
- [ ] How deeply do agents need to log? (recommend: INFO level for normal ops)
- [ ] Timeout per agent type (recommend: 5min default, 30min for embeddings)

### Acceptance Criteria

- [ ] ✅ BaseAgent abstract class designed
- [ ] ✅ Core methods documented: analyze(), enrich(), validate(), execute()
- [ ] ✅ Agent lifecycle documented
- [ ] ✅ Error handling patterns documented
- [ ] ✅ Testing patterns established
- [ ] ✅ DataEnrichmentAgent template created
- [ ] ✅ Code review ready
- [ ] ✅ @dev can implement without questions

### Next Steps

→ Share with @dev for #30 (Base Agent Implementation)

---

## 🏗️ Issue #37: API Contracts for AI Features

### Status: BLOCKED (Waiting on #34, #36)

This issue depends on completion of:

- [x] #34 - PostgreSQL Schema Design (to understand data model)
- [x] #36 - AI Agent Base Architecture (to understand agent outputs)

Once those are complete, will document:

1. **New API Endpoints**
   - GET `/listings/{id}/enriched` - Get enriched listing data
   - POST `/search/semantic` - Semantic search with embeddings
   - GET `/matches/recommended` - Get AI-recommended matches
   - GET `/matches/{id}/reason` - Why was this match recommended?

2. **Request/Response Schemas**
   - Request examples with all parameters
   - Response examples with status codes
   - Error response formats

3. **Webhook Callbacks**
   - on-enrichment-complete
   - on-match-found
   - on-quality-score-updated

4. **OpenAPI/Swagger Specification**

### Timeline

- [ ] #34 Complete (PostgreSQL Schema)
- [ ] #36 Complete (AI Agent Design)
- Then start #37 immediately

---

## 📊 Progress Tracking

### Sprint 1, Iteration 1

- [ ] #34 - PostgreSQL Schema Design (IN PROGRESS)
- [ ] #35 - Redis + Celery Architecture (TODO)
- [ ] #36 - AI Agent Base Architecture (TODO)
- [ ] #37 - API Contracts (BLOCKED on #34, #36)

### Success Criteria

- [ ] All 4 design documents complete and reviewed
- [ ] No ambiguity for @dev implementation
- [ ] All diagrams and examples provided
- [ ] @dev can estimate implementation confidently

---

## 📄 Related Resources

**Documentation:**

- [AI-ARCHITECTURE-STRATEGY.md](/Documents/AI-ARCHITECTURE-STRATEGY.md)
- [AI-PRODUCT-ROADMAP.md](/Documents/AI-PRODUCT-ROADMAP.md)
- [BMAD-ORCHESTRATION-PLAN.md](/Documents/BMAD-ORCHESTRATION-PLAN.md)

**Code References:**

- [backend/app.py](../../backend/app.py) - Current schema
- [backend/requirements.txt](../../backend/requirements.txt)

**External Docs:**

- PostgreSQL: https://www.postgresql.org/docs/
- Celery: https://docs.celeryproject.io/
- Redis: https://redis.io/

---

**Started by:** GitHub Copilot (@architect)  
**Last Updated:** November 3, 2025  
**Next Review:** After Issue #36 complete
