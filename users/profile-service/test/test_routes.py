from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

test_profile = {
    "user_id": "11111111-1111-1111-1111-111111111111",
    "full_name": "Test User",
    "birth_date": "1990-01-01",
    "phone_number": "0990000000"
}


def test_create_profile():
    response = client.post("/api/profiles/", json=test_profile)
    assert response.status_code == 200
    assert response.json()["message"] == "Profile successfully created"


def test_get_profile():
    # Asegura que el perfil existe antes de consultarlo
    client.post("/api/profiles/", json=test_profile)
    response = client.get(f"/api/profiles/{test_profile['user_id']}")
    assert response.status_code == 200
    assert response.json()["user_id"] == test_profile["user_id"]


def test_update_profile():
    updated_data = {
        "full_name": "Updated User",
        "birth_date": "1991-01-01",
        "phone_number": "0987654321"
    }
    client.post("/api/profiles/", json=test_profile)
    response = client.put(f"/api/profiles/{test_profile['user_id']}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Profile successfully updated"


def test_delete_profile():
    client.post("/api/profiles/", json=test_profile)
    response = client.delete(f"/api/profiles/{test_profile['user_id']}")
    assert response.status_code == 200
    assert response.json()["message"] == "Profile successfully deleted"
