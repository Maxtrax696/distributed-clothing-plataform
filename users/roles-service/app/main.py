from fastapi import FastAPI
from app.controllers import role_controller

app = FastAPI(
    title="Roles Service API",
    description="Microservicio para gestionar y actualizar roles de usuarios.",
    version="1.0.0"
)

app.include_router(role_controller.router, prefix="/api/roles", tags=["Roles"])
