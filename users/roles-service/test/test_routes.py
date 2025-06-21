from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_role():
    response = client.post("/api/roles/", json={"name": "admin"})
    assert response.status_code == 200
    assert response.json()["message"] == "Role created successfully"

def test_get_roles():
    response = client.get("/api/roles/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
