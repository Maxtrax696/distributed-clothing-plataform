from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import registration_router

app = FastAPI(
    title="Registration Service - API",
    description="Microservicio responsable del registro de usuarios, creación automática de perfiles y asignación del rol 'cliente'.",
    version="1.0.0",
    contact={
        "name": "Distributed Clothing Team",
        "email": "soporte@distribuidos.com"
    },
    openapi_tags=[
        {
            "name": "Registro",
            "description": "Operaciones relacionadas con el registro de usuarios"
        }
    ]
)

app.include_router(registration_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Registro"])
def root():
    return {"message": "Registration Service is running"}
