# Address Service

**Microservicio del dominio `users`** encargado de gestionar las direcciones asociadas a los usuarios registrados en la plataforma **Distributed Clothing Platform**.

Permite registrar, consultar, actualizar y eliminar direcciones de envío o facturación vinculadas a cada usuario.

## Tecnologías utilizadas

- **Python 3.11**
- **FastAPI**
- **PostgreSQL**
- **psycopg2** (conexión directa sin ORM)
- **Docker** y **Docker Compose**
- **Pydantic v2** + `pydantic-settings`
- Arquitectura **MVC distribuida**
- Principios de diseño **SOLID**


## Estilo de arquitectura

> Este microservicio sigue un estilo **RESTful** y la arquitectura general del sistema está basada en microservicios desacoplados con comunicación por HTTP.


## Patrones de diseño aplicados

| Patrón     | Descripción |
|------------|-------------|
| **KISS**   | Código simple y directo |
| **SOLID**  | Cada archivo cumple una única responsabilidad |
| **DRY**    | Se reutilizan funciones de conexión y validación |
| **YAGNI**  | Solo se implementa lo necesario |
| **POLA**   | Acceso restringido a recursos sensibles mediante roles y tokens |

## Estructura del proyecto

```bash
address-service/
app/
   config/           # Configuración de entorno (BaseSettings)
   core/             # Conexión directa con PostgreSQL (psycopg2)
   controllers/      # Lógica HTTP (validación y manejo de errores)
   models/           # Esquemas de entrada/salida con Pydantic
   repositories/     # Consultas SQL y operaciones de BD
   routes/           # Endpoints públicos
   services/         # Reglas de negocio
    main.py           # Punto de entrada de la aplicación
Dockerfile
requirements.txt    .env
```

## Endpoints
| Método | Endpoint                | Descripción                                 |
| ------ | ----------------------- | ------------------------------------------- |
| GET    | `/address/{user_id}`    | Obtener todas las direcciones de un usuario |
| POST   | `/address/`             | Registrar una nueva dirección               |
| PUT    | `/address/{address_id}` | Actualizar dirección por ID                 |
| DELETE | `/address/{address_id}` | Eliminar dirección por ID                   |

## Segurdad
Este microservicio puede ser extendido para verificar el JWT del usuario usando el campo Authorization: Bearer <token> en los headers.
El token puede ser validado desde el login-service o token-service.

## Variables de entorno (.env)
POSTGRES_DB=users_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
JWT_SECRET_KEY=supersecretkey123

## Docker
Build de servicio
```bash
docker compose build address-service
```
## Levantar el servicio
```bash
docker compose up address-service
```

## Notas finales
Este servicio depende del contenedor users_db definido en docker-compose.yml.

La tabla addresses está relacionada por clave foránea con la tabla users.

Usa psycopg2 para mayor control en las operaciones CRUD.