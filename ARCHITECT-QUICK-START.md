# @Architect - Quick Reference for GitHub Issues

## 🎯 Your Role This Sprint

As @architect, you're the **Lead Infrastructure Designer**. Your designs unblock all @dev work.

**Your Issues (4):**

- #34 PostgreSQL Migration & Schema Design
- #35 Redis + Celery Architecture
- #36 AI Agent Base Architecture
- #37 API Contracts (blocked, start after #34 & #36)

---

## ⚡ START HERE - Issue #34: PostgreSQL Schema Design

**Why:** @dev cannot setup PostgreSQL (#27) without your schema design

**What to Deliver:**

1. Current state analysis (SQLite schema inventory)
2. New schema with pgvector integration
3. ERD diagram (visual representation)
4. Migration script strategy
5. Rollback procedures
6. Share file: `ARCHITECT-SPRINT-1-DESIGNS.md` (done!)

**Key Details:**

- Listing embedding column: `vector(1536)`
- Create IVFFlat indexes for similarity search
- Migration from SQLite → PostgreSQL
- Plan forward for quality_score, urgency_level columns

**Blockers:**

- Waiting on @analyst (#26) vector DB recommendation (affects embedding dimension)
- Share design in issue #34 comments

**Timeline:** Complete this iteration (4 days)

---

## ⚡ PARALLEL: Issue #35: Redis + Celery Architecture

**Why:** @dev cannot setup Redis+Celery (#29) without your architecture design

**What to Deliver:**

1. Task topology map (all 6 AI agent tasks listed)
2. Queue strategy (urgent, normal, low priority)
3. Worker configuration (processes, concurrency, timeouts)
4. Error handling (DLQ, retry logic, alerts)
5. Monitoring plan (Flower, metrics, thresholds)
6. Architecture diagram

**Key Details:**

```
6 AI Agent Tasks to Map:
- process_listing (enrichment)
- generate_embeddings (batch operation)
- find_semantic_matches
- score_quality
- detect_urgency
- calculate_trust_score

3 Priority Queues:
- urgent_matches (urgent fulfillment)
- listing_enrichment (normal work)
- embeddings_generation (batch, lower priority)
```

**Timeline:** Complete this iteration (4 days)

---

## ⚡ PARALLEL: Issue #36: AI Agent Base Architecture

**Why:** @dev cannot implement agents (#30) without your base class design

**What to Deliver:**

1. BaseAgent abstract class interface
2. Core methods: analyze(), enrich(), validate(), execute()
3. Agent lifecycle documentation
4. Error handling patterns
5. Testing patterns
6. Concrete example: DataEnrichmentAgent

**Key Code Pattern:**

```python
class BaseAgent(ABC):
    def execute(data):
        analyze() → enrich() → validate() → return result

    Result Format:
    {
        'status': 'success|partial|failed',
        'result': {...},
        'confidence': 0.0-1.0,
        'errors': [...],
        'metadata': {...}
    }
```

**Timeline:** Complete this iteration (4 days)

---

## ⏳ LATER: Issue #37: API Contracts

**Status:** BLOCKED - Wait for #34 & #36

**What to Deliver:**

1. New endpoints: GET /listings/{id}/enriched, POST /search/semantic, etc.
2. Request/response schemas with examples
3. Webhook callbacks
4. OpenAPI/Swagger spec

**Timeline:** Start after #34 & #36 complete (2 days)

---

## 📋 Execution Plan

### Iteration 1 (This Week)

1. [ ] Complete #34 - PostgreSQL Schema
   - Share file: `ARCHITECT-SPRINT-1-DESIGNS.md`
   - Post in issue #34 with diagram
   - Comment: "Ready for @dev"

2. [ ] Complete #35 - Redis + Celery
   - Share file updates: `ARCHITECT-SPRINT-1-DESIGNS.md`
   - Post task topology diagram in issue #35
   - Comment: "Ready for @dev"

3. [ ] Complete #36 - AI Agent Base
   - Share file updates: `ARCHITECT-SPRINT-1-DESIGNS.md`
   - Post Python code examples in issue #36
   - Comment: "Ready for @dev"

### Iteration 2 (Next Week)

4. [ ] Complete #37 - API Contracts
   - Post OpenAPI spec in issue #37
   - Comment: "Ready for frontend & external integrations"

---

## 🎯 Success Criteria

**For each issue you complete:**

- [ ] Design document clear and unambiguous
- [ ] Diagrams included (ASCII or image)
- [ ] Code examples provided
- [ ] @dev can estimate implementation confidently
- [ ] No follow-up questions from @dev

**Overall:**

- [ ] 4/4 design issues complete
- [ ] 0 clarifications needed from @dev
- [ ] Team confident in architecture

---

## 📝 How to Update Your Issues

**Posting Design:**

1. Go to GitHub issue (e.g., #34)
2. Add comment with your design
3. Tag @dev: "Hey @dev, design ready for #27"
4. Link to `ARCHITECT-SPRINT-1-DESIGNS.md`

**Format:**

```markdown
### Design for [Issue Name]

See detailed design in: [ARCHITECT-SPRINT-1-DESIGNS.md](../ARCHITECT-SPRINT-1-DESIGNS.md)

**Key Points:**

- Point 1
- Point 2
- Point 3

**Questions for @analyst:**

- Question 1?

**Ready for @dev:** Yes, no ambiguity
```

---

## 🚀 Quick Checklist

### Issue #34 - PostgreSQL

- [ ] Current SQLite schema documented
- [ ] New Postgres schema with pgvector
- [ ] ERD diagram created
- [ ] Migration strategy (forward + rollback)
- [ ] Ready for @dev #27

### Issue #35 - Redis + Celery

- [ ] Task topology (6 tasks mapped)
- [ ] Queue strategy (3 priority levels)
- [ ] Worker config (processes, concurrency, timeouts)
- [ ] Error handling (DLQ, retries, alerts)
- [ ] Architecture diagram
- [ ] Ready for @dev #29

### Issue #36 - AI Agent Base

- [ ] BaseAgent abstract class
- [ ] Core methods (analyze, enrich, validate, execute)
- [ ] Agent lifecycle documented
- [ ] Error handling patterns
- [ ] Testing patterns
- [ ] DataEnrichmentAgent example
- [ ] Ready for @dev #30

### Issue #37 - API Contracts

- [ ] (Blocked on #34 & #36)
- [ ] Endpoints documented
- [ ] Schemas with examples
- [ ] Webhooks documented
- [ ] OpenAPI spec
- [ ] Ready for frontend & integrations

---

## 💬 Blockers & Help

**Need help from @analyst:**

- Embedding dimension confirmation (1536 vs other?)
- Vector DB performance implications?

**Need help from @pm:**

- Scale targets? (1K, 10K, 100K users?)
- Latency requirements?

**Communicate via:**

- GitHub issue comments (tag agents)
- Document: `ARCHITECT-SPRINT-1-DESIGNS.md`

---

## 📚 Reference Materials

**In Repo:**

- [ARCHITECT-SPRINT-1-DESIGNS.md](../ARCHITECT-SPRINT-1-DESIGNS.md) - Your main design document
- [AI-ARCHITECTURE-STRATEGY.md](/Documents/AI-ARCHITECTURE-STRATEGY.md) - Phase 2 strategy
- [BMAD-ORCHESTRATION-PLAN.md](/Documents/BMAD-ORCHESTRATION-PLAN.md) - Overall plan
- [backend/app.py](../../backend/app.py) - Current code

**External Docs:**

- PostgreSQL: https://www.postgresql.org/docs/
- pgvector: https://github.com/pgvector/pgvector
- Celery: https://docs.celeryproject.io/
- Redis: https://redis.io/

---

**Status:** Ready to start Issue #34  
**Estimated Duration:** 4-5 days for all 3 design issues  
**Next Checkpoint:** Issue #34 complete + @dev feedback
