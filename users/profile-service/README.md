##Distributed-clothing-pltaform

#  Profile Service

This microservice belongs to the `users` domain and is responsible for managing user profile information within the distributed platform.

---

##  Technologies Used

-  Python 3.11
-  FastAPI
-  PostgreSQL
-  Docker & Docker Compose

---

##  Project Structure

users/
└── profile-service/
├── app/
│ ├── main.py
│ ├── routes.py
│ ├── models.py
│ └── db.py
├── test/
│ └── test_routes.py
├── Dockerfile
├── requirements.txt
└── ...


---

##  Run Locally (Development Mode)

1. Clone the repository

git clone https://github.com/Maxtrax696/distributed-clothing-plataform.git
cd distributed-clothing-plataform

2. Start the service with Docker Compose

docker-compose -f devops/docker-compose.dev.yml up --build

3. Access the service at:

http://localhost:8000/

Available Endpoint

| Method | Endpoint                  | Description                |
| ------ | ------------------------- | -------------------------- |
| GET    | `/api/profiles/`          | Get all profiles           |
| GET    | `/api/profiles/{user_id}` | Get a profile by user\_id  |
| POST   | `/api/profiles/`          | Create a new profile       |
| PUT    | `/api/profiles/{user_id}` | Update an existing profile |
| DELETE | `/api/profiles/{user_id}` | Delete a profile           |

Run Unit Tests
From inside the container:
docker exec -it profile-service pytest test/

Or directly with Compose:
docker-compose -f devops/docker-compose.dev.yml exec profile-service pytest test/

Environment Variables
These environment variables are already declared in docker-compose.dev.yml:

POSTGRES_DB=users_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

Notes
This service connects to a shared PostgreSQL database (users_db) used by all microservices in the users domain.

The initial table schema is loaded from devops/init/users_schema.sql.