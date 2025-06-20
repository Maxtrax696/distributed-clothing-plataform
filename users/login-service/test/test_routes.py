import requests

def test_login_endpoint():
    url = "http://localhost:5003/login"
    payload = {
        "email": "testuser@example.com",
        "password": "test123"
    }
    response = requests.post(url, json=payload)
    assert response.status_code in [200, 401]
