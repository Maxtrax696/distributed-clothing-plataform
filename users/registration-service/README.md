# Registration Service

Microservicio perteneciente al dominio de usuarios del proyecto **Distributed Clothing Platform**, encargado del registro de nuevos usuarios. Al registrar un usuario, este servicio:

- Guarda las credenciales y datos personales en la base de datos `users_db` (PostgreSQL).
- Crea automáticamente su perfil en la tabla `profiles`.
- Le asigna el rol por defecto (`cliente`) a través de la tabla `user_roles`.

---

## Tecnologías Utilizadas

- **Lenguaje:** Python 3.11
- **Framework:** FastAPI
- **Base de Datos:** PostgreSQL
- **Patrones de Diseño:** SOLID
- **Estilo de Arquitectura:** Clean Architecture + MVC distribuido
- **Seguridad:** CORS, validación de duplicados, hash de contraseñas con `bcrypt`
- **Documentación:** Swagger UI (`/docs`)

---

## Estructura del Proyecto

```bash
registration-service/
    app/
        main.py
        core/
            db.py                  # Conexión a PostgreSQL
        models/
            schemas.py             # Pydantic DTOs
            entities.py            # Modelos de la base de datos (si se usan)
        repositories/
            user_repository.py     # Consultas SQL para registro y perfil
        services/
            registration_service.py # Lógica de negocio del registro
        routes/
            registration_router.py # Endpoints expuestos
        utils/
            role_assigner.py       # Asignación automática de roles
    .env                           # Variables de entorno (DB config)
    Dockerfile                     # Construcción del contenedor
    requirements.txt               # Dependencias del microservicio
    README.md                      # Documentación
```

## Despliegue con Docker
docker compose up -d --build registration-service

## Endpoints disponibles
| Método | Endpoint              | Descripción                                      |
| ------ | --------------------- | ------------------------------------------------ |
| POST   | `/api/register/`      | Registra un nuevo usuario y crea su perfil y rol |
| GET    | `/api/register/users` | Lista todos los usuarios registrados (opcional)  |

Documentación Swagger disponible en: http://localhost:8003/docs

## Seguridad
Contraseñas hasheadas con bcrypt

Prevención de duplicación de correos

Middleware CORS habilitado

Endpoints preparados para validación JWT futura

## Autor
Ayrton Yoshua Calahorrano Villamarín
Proyecto de Titulación - Universidad Central del Ecuador
Tutor: Ing. Juan Pablo Guevara
Materia: Programación Distribuida