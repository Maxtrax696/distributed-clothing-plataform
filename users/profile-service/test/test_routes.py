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
    assert response.json()["message"] == "Perfil creado correctamente"


def test_get_profile():
    response = client.get(f"/api/profiles/{test_profile['user_id']}")
    assert response.status_code == 200
    assert response.json()["user_id"] == test_profile["user_id"]


def test_update_profile():
    updated_data = {
        "full_name": "Test User Updated",
        "birth_date": "1991-01-01",
        "phone_number": "0980000000"
    }
    response = client.put(f"/api/profiles/{test_profile['user_id']}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Perfil actualizado correctamente"


def test_delete_profile():
    response = client.delete(f"/api/profiles/{test_profile['user_id']}")
    assert response.status_code == 200
    assert response.json()["message"] == "Perfil eliminado correctamente"
