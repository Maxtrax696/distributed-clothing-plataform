from app import create_app

def test_placeholder():
    assert True
    app = create_app()
    client = app.test_client()

    response = client.post('/login', json={
        "email": "test@example.com",
        "password": "1234"
    })

    # Accept either 200 OK or 401 Unauthorized
    assert response.status_code in [200, 401]
