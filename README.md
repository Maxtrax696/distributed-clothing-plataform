# Distributed Clothing Platform

Plataforma web de comercio electrónico dedicada a la venta de camisetas y hoodies personalizados. Los usuarios pueden escoger y personalizar sus prendas con estampados únicos según su estilo y preferencias.

## Estructura del Proyecto

El proyecto está organizado bajo una estructura **MonoRepo**, lo que permite mantener todos los microservicios relacionados en un solo repositorio para una mejor integración y control.

distributed-clothing-plataform/
   .github/Workflows #Cada ci se ejecuta unicamente cuando se detecta un cambio en el microservicio.
      ci-prod.yml
      ci-qa-login.yml
      ci-qa-profile.yml
      ci-qa-registration.yml
      ci-qa-roles.yml
   analytics/ # Microservicio de analítica
   catalog/ # Microservicio de catálogo de productos
   devops/
      init/
         init.sql #db POSTGRES para dominio users
      docker-compose.yml #Levanta la base de datos POSTGRES v.16
   docs/ # Documentación del proyecto
   infra/ # Infraestructura general (terraform, docker-compose, etc.)
   inventory/ # Microservicio de inventario
   orders/ # Microservicio de órdenes
   users/
      login-service/
         app/
            config/
               settings.py
            core/
               connection.py
               security.py
            models/
               login_request.py
            repositories/
               user_repository.py
            routes/
               auth_routes.py
            services/
               login_service.py
   profile-service/
      app/
         controllers/
            profile_controller.py
         core/
            db.py
         models/
            profile_schema.py
         repositories/
            profile_repository.py
         services/
            profile_service.py
   registration-service/
      app/
         core/
            db.py
         models/
            entities.py
            schemas.py
         repositories/
            user_repository.py
         routes/
            registration_router.py
         services/
            registration_service.py
         utils/
            role_assigner.py

   docker-compose.yml # Levanta todos los servicios
   README.md

## Patrón de Arquitectura

Actualmente el proyecto implementa una mezcla bien estructurada de:

### Clean Architecture + MVC distribuido

- **Capa de Presentación (Controller)**: `routes/`
- **Capa de Aplicación (Servicios / Interactor)**: `services/`
- **Capa de Dominio (Modelos)**: `models/`
- **Capa de Infraestructura (Acceso a datos y configuración)**: `repositories/` y `core/`

## Patrón de Diseño

Se está aplicando el principio **SOLID** en cada microservicio para asegurar:

- **S**: Responsabilidad única
- **O**: Abierto a extensión, cerrado a modificación
- **L**: Sustitución de clases
- **I**: Segregación de interfaces (en términos de clases desacopladas)
- **D**: Inversión de dependencias (a través de inyección de repositorios)

## Estado actual del desarrollo

- [x] `login-service` funcional (con JWT, PostgreSQL y autenticación segura)
- [x] `registration-service` registra usuarios, roles y perfiles
- [x] `roles-service` permite actualizar roles
- [ ] Microservicios `profile`, `address`, `catalog`, `orders`, `inventory`, `analytics`: en desarrollo

## 🌐 Endpoints disponibles

| Microservicio         | Método | Endpoint                          | Descripción                             |
|-----------------------|--------|-----------------------------------|-----------------------------------------|
| `login-service`       | POST   | `/api/login`                      | Iniciar sesión y obtener JWT            |
|                       | GET    | `/api/verify`                     | Verificar validez del token             |
| `registration-service`| POST   | `/api/register`                   | Registrar nuevo usuario                 |
|                       | GET    | `/api/register/users`            | Listar usuarios registrados             |
| `roles-service`       | PUT    | `/api/roles/{role_id}`           | Actualizar nombre o descripción de rol  |
|                       | GET    | `/api/roles`                     | Listar todos los roles existentes       |
|                       | POST   | `/api/roles`                     | Crear nuevo rol                         |
|                       | DELETE | `/api/roles/{role_id}`           | Eliminar un rol                         |
|                       | POST   | `/api/roles/assign`              | Asignar rol a un usuario                |

> Todos los endpoints comienzan con `/api/...`, están estructurados con FastAPI y devuelven respuestas en formato JSON.

## Endpoints protegidos por JWT

| Microservicio         | Método | Endpoint                          | Descripción                                 |
|-----------------------|--------|-----------------------------------|---------------------------------------------|
| `login-service`       | GET    | `/api/verify`                     | Verifica que el token JWT sea válido        |
| `registration-service`| GET    | `/api/register/users`            | Listar usuarios (requiere autenticación)    |
| `roles-service`       | POST   | `/api/roles`                     | Crear rol (requiere autenticación)          |
|                       | PUT    | `/api/roles/{role_id}`           | Actualizar rol (requiere autenticación)     |
|                       | DELETE | `/api/roles/{role_id}`           | Eliminar rol (requiere autenticación)       |
|                       | POST   | `/api/roles/assign`              | Asignar rol a un usuario autenticado        |

> ⚠️ Estas rutas requieren el encabezado:  
> `Authorization: Bearer <token>`  
> obtenido desde el endpoint `/api/login`.
