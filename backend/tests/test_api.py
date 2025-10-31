import pytest

from backend.app import app, db, Item, User
from backend.auth import token_for
from werkzeug.security import generate_password_hash
from backend.app import Item, User
from backend.auth import token_for
from backend.app import app


def test_health(client):
    resp = client.get("/api/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_list_items(client):
    # Initially there are no items; create one directly
    with app.app_context():
        it = Item(name="Seed", description="seed")
        from backend.app import db
        db.session.add(it)
        db.session.commit()
    resp = client.get("/api/items")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "items" in data and isinstance(data["items"], list)
    assert len(data["items"]) >= 1


def test_create_item(client, create_user):
    user_id = create_user()
    token = token_for(user_id)
    headers = {"Authorization": f"Bearer {token}"}
    resp = client.post("/api/items", json={"name": "New", "description": "desc"}, headers=headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["name"] == "New"
