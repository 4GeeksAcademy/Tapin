# QA: Create Test Suite for Backend

@qa — please create the comprehensive test suite for the backend. Below are recommended tests to implement and where to place them.

Priority areas (each should be a pytest file under `backend/tests/`):

- `test_auth.py`
  - register (happy path + missing fields + duplicate email)
  - login (valid/invalid credentials)
  - token validation and expiry behavior

- `test_items.py`
  - GET /api/items (empty DB, seeded items)
  - POST /api/items (authorized + unauthorized + validation errors)
  - data integrity (created item persists in DB)

- `test_listings.py`
  - CRUD for listings (list, create with JWT owner, update/delete with ownership checks)
  - filters (q= and location= queries)

- `test_password_reset.py`
  - reset request (smtp configured vs dev fallback)
  - confirm reset (valid token, expired, invalid)

- `test_integration.py`
  - end-to-end flow: register -> login -> create listing -> fetch listing

Guidance
- Use fixtures to provide an in-memory SQLite DB (sqlite:///:memory:) and to create a test user and client.
- Reuse `backend.auth.token_for(user)` when creating tokens in tests.
- Keep tests deterministic and independent; avoid relying on `backend/data.db` file.

Deliverables
- Add pytest files under `backend/tests/` and ensure `pytest -q` passes locally.
- Create a short PR and link here when ready so we can run CI.
