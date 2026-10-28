from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    assert client.get("/").status_code == 200

def test_health():
    assert client.get("/health").status_code == 200

def test_person_detected():
    r = client.post("/extract", json={"text": "Elon Musk founded SpaceX."})
    assert r.status_code == 200
    types = [e["type"] for e in r.json()["entities"]]
    assert "PER" in types
    assert "ORG" in types

def test_empty_text():
    r = client.post("/extract", json={"text": "The weather is nice today."})
    assert r.status_code == 200
    assert r.json()["entities"] == []
