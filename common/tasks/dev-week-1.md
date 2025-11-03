# @dev - Immediate Tasks (Week 1)

**Agent:** @dev  
**Role:** Full Stack Development & Implementation  
**Phase:** Phase 2 - Week 1  
**Due:** End of Week 1 (November 8, 2025)

---

## 🎯 Primary Mission

Set up the AI infrastructure foundation: Migrate to Postgres, install Redis + Celery, and create base AI agent architecture. This enables all future AI feature development.

---

## 📋 Tasks

### Task 1: Local Postgres Setup

**Objective:** Get Postgres running locally for development

**Steps:**

1. **Install Postgres**

```bash
# macOS
brew install postgresql@15

# Start service
brew services start postgresql@15

# Verify installation
psql --version  # Should show PostgreSQL 15.x
```

2. **Create Database**

```bash
# Create user
createuser tapin_user -P  # Set password: tapin_dev_pass

# Create database
createdb tapin_db -O tapin_user

# Test connection
psql -U tapin_user -d tapin_db
```

3. **Install pgvector Extension**

```bash
# Install extension
brew install pgvector

# Enable in database
psql -U tapin_user -d tapin_db
CREATE EXTENSION vector;
\dx  # Verify extension installed
```

4. **Update SQLAlchemy Connection**

```python
# backend/app.py or config.py
# OLD
SQLALCHEMY_DATABASE_URI = 'sqlite:///listings.db'

# NEW
SQLALCHEMY_DATABASE_URI = 'postgresql://tapin_user:tapin_dev_pass@localhost:5432/tapin_db'
```

5. **Test Connection**

```bash
cd backend
source venv/bin/activate
python -c "from app import db; db.create_all(); print('✅ Postgres connected!')"
```

**Deliverable:** Postgres running locally with pgvector

**Due:** Monday EOD

---

### Task 2: Cloud Postgres Setup (Render)

**Objective:** Production Postgres instance ready

**Steps:**

1. **Create Render Database**
   - Go to https://render.com
   - New → PostgreSQL
   - Name: tapin-db-prod
   - Plan: Free tier (sufficient for Phase 2)
   - Region: Oregon (US West)

2. **Get Connection String**
   - Copy external database URL
   - Format: `postgresql://user:pass@host:port/db`

3. **Update Environment Variables**

```bash
# backend/.env
DATABASE_URL=postgresql://user:pass@host:port/db

# backend/app.py
import os
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://localhost...')
```

4. **Enable pgvector on Render**

```bash
# Connect via psql
psql $DATABASE_URL
CREATE EXTENSION vector;
```

5. **Test Deployment**

```bash
# Run migrations on Render database
DATABASE_URL=$RENDER_DB_URL python manage.py db upgrade
```

**Deliverable:** Render Postgres with pgvector ready

**Due:** Tuesday EOD

---

### Task 3: Redis + Celery Installation

**Objective:** Background task queue operational

**Steps:**

1. **Install Redis Locally**

```bash
# macOS
brew install redis

# Start Redis
brew services start redis

# Test
redis-cli ping  # Should return "PONG"
```

2. **Install Celery**

```bash
cd backend
source venv/bin/activate
pip install celery redis
pip freeze > requirements.txt
```

3. **Create Celery App**

```python
# backend/celery_app.py
from celery import Celery
import os

redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

celery_app = Celery(
    'tapin',
    broker=redis_url,
    backend=redis_url
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
```

4. **Create Tasks Module**

```python
# backend/tasks.py
from celery_app import celery_app
from app import db
import logging

logger = logging.getLogger(__name__)

@celery_app.task
def test_task(message):
    """Test task to verify Celery is working"""
    logger.info(f"Test task received: {message}")
    return f"Processed: {message}"

@celery_app.task
def enrich_listing(listing_id):
    """Placeholder for data enrichment agent"""
    logger.info(f"Enriching listing {listing_id}")
    # Will implement in Week 3
    return {"listing_id": listing_id, "status": "enriched"}
```

5. **Start Celery Worker**

```bash
# Terminal 1: Start worker
cd backend
source venv/bin/activate
celery -A tasks worker --loglevel=info

# Terminal 2: Test task
python
>>> from tasks import test_task
>>> result = test_task.delay("Hello Celery!")
>>> result.get(timeout=5)
'Processed: Hello Celery!'
```

**Deliverable:** Celery workers processing tasks

**Due:** Wednesday EOD

---

### Task 4: Database Migration (SQLite → Postgres)

**Objective:** Migrate existing data without loss

**Steps:**

1. **Backup SQLite Data**

```bash
cp backend/listings.db backend/listings.db.backup
sqlite3 backend/listings.db ".dump" > backup.sql
```

2. **Export Data to JSON**

```python
# backend/migrate_data.py
import json
from app import app, db, User, Listing, Review

with app.app_context():
    # Export users
    users = User.query.all()
    users_data = [{
        'id': u.id,
        'email': u.email,
        'password_hash': u.password_hash,
        'created_at': u.created_at.isoformat() if u.created_at else None
    } for u in users]

    # Export listings
    listings = Listing.query.all()
    listings_data = [{
        'id': l.id,
        'title': l.title,
        'description': l.description,
        'category': l.category,
        'latitude': l.latitude,
        'longitude': l.longitude,
        'owner_id': l.owner_id,
        # ... all fields
    } for l in listings]

    # Export reviews
    reviews = Review.query.all()
    reviews_data = [{
        'id': r.id,
        'listing_id': r.listing_id,
        'user_id': r.user_id,
        'rating': r.rating,
        'comment': r.comment,
    } for r in reviews]

    # Save to JSON
    with open('migration_data.json', 'w') as f:
        json.dump({
            'users': users_data,
            'listings': listings_data,
            'reviews': reviews_data
        }, f, indent=2)

    print(f"✅ Exported {len(users)} users, {len(listings)} listings, {len(reviews)} reviews")
```

3. **Update SQLAlchemy Models for Postgres**

```python
# backend/models.py
# Add new AI-related fields

class Listing(db.Model):
    # ... existing fields ...

    # NEW: AI enhancement fields
    quality_score = db.Column(db.Integer, default=0)  # 0-100
    embedding_generated = db.Column(db.Boolean, default=False)
    enriched_at = db.Column(db.DateTime, nullable=True)
```

4. **Create Fresh Postgres Schema**

```bash
# With Postgres connection string in place
python
>>> from app import db
>>> db.create_all()
>>> print("✅ Postgres schema created")
```

5. **Import Data to Postgres**

```python
# backend/import_data.py
import json
from app import app, db, User, Listing, Review
from datetime import datetime

with app.app_context():
    with open('migration_data.json', 'r') as f:
        data = json.load(f)

    # Import users
    for user_data in data['users']:
        user = User(
            id=user_data['id'],
            email=user_data['email'],
            password_hash=user_data['password_hash'],
            created_at=datetime.fromisoformat(user_data['created_at']) if user_data.get('created_at') else None
        )
        db.session.merge(user)  # merge handles existing IDs

    # Import listings
    for listing_data in data['listings']:
        listing = Listing(**listing_data)
        db.session.merge(listing)

    # Import reviews
    for review_data in data['reviews']:
        review = Review(**review_data)
        db.session.merge(review)

    db.session.commit()
    print("✅ Data imported to Postgres")
```

6. **Verify Data Integrity**

```python
# Compare counts
# SQLite:
sqlite3 listings.db "SELECT COUNT(*) FROM users;"
sqlite3 listings.db "SELECT COUNT(*) FROM listings;"

# Postgres:
psql -U tapin_user -d tapin_db -c "SELECT COUNT(*) FROM users;"
psql -U tapin_user -d tapin_db -c "SELECT COUNT(*) FROM listings;"

# Counts should match!
```

**Deliverable:** All data migrated to Postgres

**Due:** Thursday EOD

---

### Task 5: Create Base AI Agent Classes

**Objective:** Reusable architecture for all 6 AI agents

**Steps:**

1. **Create Agents Directory**

```bash
mkdir -p backend/agents
touch backend/agents/__init__.py
```

2. **Base Agent Class**

```python
# backend/agents/base_agent.py
from abc import ABC, abstractmethod
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    """Base class for all AI agents"""

    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(f"agents.{name}")

    @abstractmethod
    async def process(self, entity_id, entity_type):
        """
        Main processing method each agent must implement

        Args:
            entity_id: ID of entity to process (listing, user, etc.)
            entity_type: Type of entity ('listing', 'user', etc.)

        Returns:
            dict: Processing result
        """
        pass

    def log_action(self, action, entity_id, result, execution_time_ms):
        """Log agent action to database for monitoring"""
        from app import db
        from models import AgentLog

        log = AgentLog(
            agent_name=self.name,
            action=action,
            entity_id=entity_id,
            result=result,
            execution_time_ms=execution_time_ms,
            created_at=datetime.utcnow()
        )
        db.session.add(log)
        db.session.commit()

        self.logger.info(f"{action} completed in {execution_time_ms}ms")
```

3. **Data Enrichment Agent (Placeholder)**

```python
# backend/agents/data_enrichment.py
from agents.base_agent import BaseAgent
import time

class DataEnrichmentAgent(BaseAgent):
    """Enriches listings with geocoding, tags, quality score"""

    def __init__(self):
        super().__init__("data_enrichment")

    async def process(self, listing_id, entity_type='listing'):
        start_time = time.time()

        self.logger.info(f"Processing listing {listing_id}")

        # Placeholder - will implement in Week 3
        result = {
            'listing_id': listing_id,
            'geocoded': False,  # Will implement
            'quality_score': 0,  # Will implement
            'tags_generated': False  # Will implement
        }

        execution_time = int((time.time() - start_time) * 1000)
        self.log_action('enrich', listing_id, result, execution_time)

        return result
```

4. **Matching Agent (Placeholder)**

```python
# backend/agents/matching.py
from agents.base_agent import BaseAgent

class MatchingAgent(BaseAgent):
    """Handles semantic search and personalized recommendations"""

    def __init__(self):
        super().__init__("matching_intelligence")

    async def process(self, user_id, entity_type='user'):
        # Placeholder - will implement in Sprint 2
        return {'user_id': user_id, 'matches': []}
```

5. **Agent Factory**

```python
# backend/agents/__init__.py
from agents.data_enrichment import DataEnrichmentAgent
from agents.matching import MatchingAgent

def get_agent(agent_name):
    """Factory to instantiate agents by name"""
    agents = {
        'data_enrichment': DataEnrichmentAgent,
        'matching': MatchingAgent,
        # Add more as we build them
    }

    agent_class = agents.get(agent_name)
    if not agent_class:
        raise ValueError(f"Unknown agent: {agent_name}")

    return agent_class()
```

6. **Create AgentLog Model**

```python
# backend/models.py
class AgentLog(db.Model):
    __tablename__ = 'ai_agent_logs'

    id = db.Column(db.Integer, primary_key=True)
    agent_name = db.Column(db.String(100), nullable=False)
    action = db.Column(db.String(100), nullable=False)
    entity_type = db.Column(db.String(50), nullable=False)
    entity_id = db.Column(db.Integer, nullable=False)
    result = db.Column(db.JSON)
    execution_time_ms = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

7. **Test Agent System**

```python
# Test script
from agents import get_agent
import asyncio

async def test_agents():
    # Test data enrichment agent
    enrichment_agent = get_agent('data_enrichment')
    result = await enrichment_agent.process(listing_id=1)
    print(f"✅ Data enrichment: {result}")

    # Test matching agent
    matching_agent = get_agent('matching')
    result = await matching_agent.process(user_id=1)
    print(f"✅ Matching: {result}")

asyncio.run(test_agents())
```

**Deliverable:** Agent architecture in place

**Due:** Friday EOD

---

### Task 6: Update API to Trigger Agents

**Objective:** Hook agents into listing creation flow

**Steps:**

1. **Update Listing Creation Endpoint**

```python
# backend/app.py (or routes/listings.py)
from tasks import enrich_listing

@app.route('/api/listings', methods=['POST'])
@jwt_required()
def create_listing():
    data = request.json

    # Create listing (existing code)
    listing = Listing(
        title=data['title'],
        description=data['description'],
        # ... other fields
    )
    db.session.add(listing)
    db.session.commit()

    # NEW: Queue background enrichment
    enrich_listing.delay(listing.id)

    return jsonify({
        'listing': listing.to_dict(),
        'message': 'Listing created, AI enrichment in progress'
    }), 201
```

2. **Update Celery Task**

```python
# backend/tasks.py
from agents import get_agent
import asyncio

@celery_app.task
def enrich_listing(listing_id):
    """Background task to enrich listing"""
    agent = get_agent('data_enrichment')

    # Run async agent in sync context
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(agent.process(listing_id))
    loop.close()

    return result
```

3. **Test End-to-End**

```bash
# Start services
redis-server  # Terminal 1
celery -A tasks worker --loglevel=info  # Terminal 2
python app.py  # Terminal 3

# Create listing via API
curl -X POST http://localhost:5000/api/listings \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Test", "description": "Test listing"}'

# Check Celery logs - should see task executed
# Check agent_logs table for entry
```

**Deliverable:** Agents triggered on listing creation

**Due:** Friday EOD

---

## 📊 Success Criteria

Your week is successful if:

- ✅ Postgres running locally and on Render
- ✅ All existing data migrated (zero loss)
- ✅ Redis + Celery processing tasks
- ✅ Base agent architecture created
- ✅ Agents triggered on listing creation
- ✅ No broken functionality from migration

---

## 🚨 Troubleshooting

### Postgres Connection Issues

```bash
# Check if running
brew services list | grep postgresql

# Check logs
tail -f /opt/homebrew/var/log/postgresql@15.log

# Reset if needed
brew services restart postgresql@15
```

### Celery Not Picking Up Tasks

```bash
# Check Redis connection
redis-cli ping

# Purge queue
celery -A tasks purge

# Restart worker
celery -A tasks worker --loglevel=debug
```

### Migration Data Loss

```bash
# Restore from backup
cp backend/listings.db.backup backend/listings.db

# Re-run migration scripts
```

---

## 🤝 Collaboration

**Daily Updates:**

- Post progress in #tapin-daily
- Share blockers immediately

**Key Meetings:**

- Monday: Sprint planning
- Wednesday: Sync with @architect on database schema
- Friday: Demo infrastructure to team

**Who to Contact:**

- Postgres issues → @architect
- Requirements questions → @po
- Testing help → @qa

---

## 📖 Resources

**Postgres:**

- Installation: https://www.postgresql.org/download/
- pgvector docs: https://github.com/pgvector/pgvector

**Celery:**

- Docs: https://docs.celeryq.dev/
- Flask integration: https://flask.palletsprojects.com/patterns/celery/

**Render:**

- Postgres setup: https://render.com/docs/databases

---

## ✅ Checklist

- [ ] Postgres installed locally
- [ ] pgvector extension enabled
- [ ] Render Postgres created
- [ ] Redis installed and running
- [ ] Celery installed and configured
- [ ] Test task working
- [ ] Data migrated (zero loss verified)
- [ ] Base agent classes created
- [ ] Agents triggered on API calls
- [ ] All tests passing
- [ ] Documentation updated

---

**Status:** Active  
**Started:** November 3, 2025  
**Next Review:** November 8, 2025 (Friday demo)
