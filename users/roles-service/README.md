# Roles Service

Microservicio para la **gestión de roles de usuarios** en una plataforma distribuida de comercio electrónico. Forma parte del dominio `Users` y cumple el principio **SOLID**, arquitectura REST, y expone su documentación mediante **Swagger**.

---

## Arquitectura

Este microservicio implementa una arquitectura basada en capas y principios SOLID:

- **Controller** → `controllers/`: expone rutas HTTP (FastAPI)
- **Service** → `services/`: lógica de negocio pura
- **Repository** → `repositories/`: acceso a datos
- **Models** → `models/`: entidades de base de datos
- **Schemas** → `schemas/`: validaciones y estructuras de entrada/salida
- **Core** → `core/`: conexión a base de datos y utilitarios comunes

---

## Tecnologías

| Tecnología      | Uso                                |
|----------------|-------------------------------------|
| Python 3.10+    | Lenguaje base                      |
| FastAPI         | Framework web y documentación      |
| PostgreSQL      | Base de datos relacional           |
| SQLAlchemy      | ORM para acceso a datos            |
| Pydantic        | Validación de datos                |
| Uvicorn         | Servidor ASGI                      |
| Docker          | Contenerización                    |
| GitHub Actions  | CI/CD para QA y PROD               |

---

## Estructura del Proyecto
roles-service/
app/
    controllers/
        role_controller.py
    services/
        role_service.py
    repositories/
        role_repository.py
    models/
        role_model.py
    schemas/
        role_schema.py
    core/
        db.py
    main.py
.env
Dockerfile
requirements.txt    
README.md

## Vaiables de entorno
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=users_db

## Uso cn Docker
```bash
docker build -t roles-service .
```

## Endpoints
| Método | Ruta                   | Descripción                     |
| ------ | ---------------------- | ------------------------------- |
| GET    | `/api/roles`           | Listar todos los roles          |
| GET    | `/api/roles/{role_id}` | Obtener un rol específico       |
| POST   | `/api/roles`           | Crear un nuevo rol              |
| PUT    | `/api/roles/{role_id}` | Actualizar nombre o descripción |
| DELETE | `/api/roles/{role_id}` | Eliminar un rol                 |
| POST   | `/api/roles/assign`    | Asignar un rol a un usuario     |

## Swagger Docs
Una vez levantado el microservicio, accede a la documentación interactiva en:

    http://localhost:8000/docs → Swagger UI

    http://localhost:8000/redoc → Redoc

## Seguridad
JWT Token requerido para las siguientes rutas:

    POST /api/roles

    PUT /api/roles/{role_id}

    DELETE /api/roles/{role_id}

    POST /api/roles/assign

Agrega el encabezado:
Authorization: Bearer <JWT_TOKEN>
