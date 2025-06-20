# Login Service

This microservice handles user authentication in the **Users** domain of the LightBuild platform.

---

## Features

- Authenticate existing users via email and password
- Validates credentials stored in PostgreSQL
- Built with Python (Flask + SQLAlchemy)
- Dockerized with GitHub Actions CI/CD

---

## API Endpoint

### `POST /login`

Authenticates a user with provided credentials.

#### 🔸 Request body:

```json
{
  "email": "user@example.com",
  "password": "securepassword"
}

uccessful Response:
json
Copy code
{
  "message": "Login successful"
}
🔸 Error Responses:
If credentials are incorrect:

json
Copy code
{
  "error": "Invalid credentials"
}
If required fields are missing:

json
Copy code
{
  "error": "Email and password are required"
}
 Run Locally with Docker
bash
Copy code
docker-compose up --build
App available at: http://localhost:5003

PostgreSQL runs on port 5435

 Environment Variables
Stored in .env file:

env
Copy code
DATABASE_URL=postgresql://login_user:login_pass@db:5432/login_db
 Docker Compose Overview
yaml
Copy code
services:
  db:
    image: postgres
    ...

  login-service:
    build: .
    ports:
      - "5003:5003"
 CI/CD
This microservice is configured to:

Build and test on GitHub Actions

Push to Docker Hub on successful build

 Tests
Basic endpoint test located in test/test_routes.py:

bash
Copy code
pytest test/test_routes.py
Accepts response codes:

 200 (success)

 401 (invalid login)

 Project Structure
bash
Copy code
login-service/
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── models.py
│   └── routes.py
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── test/
│   └── test_routes.py
└── README.md