# Login Service - Distributed Clothing Platform

Este microservicio permite autenticar usuarios y emitir **tokens JWT** válidos para el acceso al resto de servicios protegidos en la plataforma distribuida de ropa personalizada.

Forma parte del sistema distribuido organizado por dominios funcionales y se integra con el dominio de usuarios (`users`).

---

## Tecnologías utilizadas

- **Lenguaje:** Python 3.11
- **Framework:** FastAPI
- **Base de datos:** PostgreSQL (vía psycopg2)
- **Seguridad:** JWT con python-jose y passlib (bcrypt)
- **Contenedores:** Docker
- **CI/CD:** GitHub Actions
- **Documentación:** Swagger (OpenAPI)

---

## Estructura del microservicio
```bash
login-service/
app/
  config/
        settings.py # Variables de entorno y configuración general
  core/
   connection.py # Conexión a la base de datos PostgreSQL
       security.py # Lógica de hashing y creación/verificación JWT
  models/
        login_request.py # Pydantic model para la solicitud de login
  repositories/
        user_repository.py # Acceso a los datos de la tabla users
  routes/
        auth_routes.py # Endpoints: /login y /verify
  services/
        login_service.py # Lógica de autenticación y validación de tokens
.env # Configuración de entorno (conexión DB y JWT)
Dockerfile # Imagen dockerizada
requirements.txt # Dependencias
```

---

## Configuración (`.env`)

```env
POSTGRES_DB=users_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

JWT_SECRET_KEY=supersecretkey123
JWT_ALGORITHM=HS256
```

## Principios aplicados
Arquitectura Clean + MVC:

      routes/ = presentación

      services/ = aplicación

      models/ = dominio

      core/, repositories/ = infraestructura

Diseño SOLID: separación de responsabilidades, reutilización, bajo acoplamiento

## Seguridad
Las contraseñas se almacenan en formato bcrypt y se comparan usando passlib.

Los tokens se generan con python-jose y tienen formato JWT.

El microservicio puede ser combinado con API Gateway o middlewares para validar tokens en producción.

## Endpoints
Documentación Swagger
Disponible automáticamente en: http://localhost:8002/docs

## CI/CD con GitHub Actions
El archivo .github/workflows/ci-qa-login.yml construye e instala dependencias automáticamente al hacer push o PR en la carpeta users/login-service/ hacia la rama qa.

Soporta build de imagen y futuros pasos como pruebas y despliegue.

## Pruebas sugeridas
| Escenario                 | Esperado         |
| ------------------------- | ---------------- |
| Login válido              | JWT emitido      |
| Contraseña incorrecta     | 401 Unauthorized |
| Email no registrado       | 401 Unauthorized |
| Token válido en `/verify` | `valid: true`    |
| Token corrupto/expirado   | `valid: false`   |

## Notas finales
Este servicio debe conectarse a una tabla users en PostgreSQL que contenga los campos: id, email, password.

Puedes extenderlo fácilmente para roles, refresh tokens, expiración, etc.

## Autoría
Proyecto desarrollado para la materia Programación Distribuida
Universidad Central del Ecuador – 2025
Docente: Ing. Juan Pablo Guevara
Equipo: Erick Maigua, Yoshua Calahorrano, y colaboradores