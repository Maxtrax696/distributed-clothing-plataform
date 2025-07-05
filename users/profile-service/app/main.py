from fastapi import FastAPI
from app.controllers import profile_controller
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Profile Service API",
    description="API REST para consultar, actualizar y eliminar perfiles de usuario.",
    version="1.0.0"
)

app.include_router(profile_controller.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # puedes restringir esto en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
