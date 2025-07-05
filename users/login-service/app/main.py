from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth_routes import router

app = FastAPI(
    title="Login Service - API",
    description="""
Este microservicio se encarga de la **autenticación de usuarios** en la plataforma distribuida.  
Permite validar credenciales y emitir un **token JWT** para el resto de servicios protegidos.

Endpoint principal: `/api/login`
""",
    version="1.0.0",
    contact={
        "name": "Equipo de Desarrollo",
        "email": "soporte@lightbuild.com"
    },
    openapi_tags=[
        {
            "name": "Autenticación",
            "description": "Endpoints relacionados con inicio de sesión y emisión de token JWT"
        }
    ]
)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(router)

# Endpoint base
@app.get("/", tags=["Autenticación"])
def root():
    return {"message": "Login Service is running"}
