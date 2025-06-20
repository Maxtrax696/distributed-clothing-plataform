import requests

def test_register_endpoint():
    url = "http://localhost:5002/register"
    payload = {
        "email": "testuser@example.com",
        "password": "test123"
    }
    response = requests.post(url, json=payload)
    
    # Acepta 200 (nuevo registro) o 400 (ya registrado)
    assert response.status_code in [200, 201, 400]
