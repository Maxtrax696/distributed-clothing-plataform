# Profile Service – Distributed Clothing Platform

Microservicio responsable de gestionar los **perfiles de usuario**. Permite consultar, actualizar y eliminar los datos del perfil personal, basándose en el `user_id` previamente registrado en el microservicio de registro (`registration-service`).

---

## Tecnologías y dependencias

- **Lenguaje**: Python 3.11
- **Framework**: FastAPI
- **Base de datos**: PostgreSQL
- **ORM**: No aplica (conexión directa con `psycopg2`)
- **Arquitectura**: REST + MVC + Principios SOLID
- **Patrones de diseño**: SRP, DRY, Inversión de Dependencias
- **Documentación**: Swagger UI (OpenAPI 3)
- **Despliegue**: Docker + Docker Compose
- **CI/CD**: GitHub Actions

---

## Estructura del proyecto
profile-service/
    app/
        main.py # Entrypoint principal
        core/
            db.py # Conexión a PostgreSQL
        models/
            profile_schema.py # Esquemas de entrada (Pydantic)
        repositories/
            profile_repository.py # Consultas SQL crudas
        services/
            profile_service.py # Lógica de negocio (use cases)
        controllers/
            profile_controller.py # Endpoints del microservicio
Dockerfile # Imagen Docker del servicio
requirements.txt # Dependencias de Python
.gitignore
.flake8 README.md # Este archivo


---

## Configuración de entorno

Asegúrate de definir las siguientes variables de entorno en tu `.env` o en el entorno del contenedor:

```env
POSTGRES_DB=users_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

## Despliegue con Docker
docker build -t profile-service .

## Documentación Swagger
Una vez levantado el servicio, puedes acceder a:

    Swagger UI: http://localhost:8000/docs

    OpenAPI JSON: http://localhost:8000/openapi.json

## Endpoints disponibles
| Método | Endpoint             | Descripción                   |
| ------ | -------------------- | ----------------------------- |
| GET    | `/api/profiles/`     | Listar todos los perfiles     |
| GET    | `/api/profiles/{id}` | Obtener perfil por `user_id`  |
| PUT    | `/api/profiles/{id}` | Actualizar datos del perfil   |
| DELETE | `/api/profiles/{id}` | Eliminar perfil (hard delete) |

## CI/CD (GitHub Actions)
El flujo ci-qa-profile.yml se activa únicamente cuando hay cambios en el path:
```bash
users/profile-service/**
```
E incluye:

    Instalación de dependencias

    Linter (flake8)

    Build Docker image

    (Opcional) Push a DockerHub

    (Opcional) Deploy vía SSH a EC2

## Consideraciones
Validación de existencia en la tabla users antes de actuar sobre profiles.

Sin ORM: se usa psycopg2 y queries SQL manuales por simplicidad y rendimiento.

CORS habilitado globalmente para permitir consumo desde frontend.

## Autor
Desarrollado por el equipo del proyecto Distributed Clothing Platform
Universidad Central del Ecuador
Programación Distribuida 2025.
Ayrton Yoshua Calahorrano Villamarin