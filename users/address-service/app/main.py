from fastapi import FastAPI
from app.routes import address_routes

app = FastAPI(
    title="Address Service",
    description="Microservicio que gestiona direcciones de usuarios (envío y facturación) para la plataforma Distributed Clothing.",
    version="1.0.0",
    contact={
        "name": "Equipo Distributed Clothing Platform",
        "email": "soporte@lightbuild.com",
        "url": "https://github.com/Maxtrax696/distributed-clothing-plataform"
    },
)

# Registrar rutas
app.include_router(address_routes.router)
