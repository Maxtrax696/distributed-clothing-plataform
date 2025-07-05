from fastapi import APIRouter, HTTPException
from app.models.schemas import UserCreate
from app.services.registration_service import RegistrationService

router = APIRouter(
    prefix="/api/register",
    tags=["Registro"]
)

service = RegistrationService()

@router.post(
    "/",
    summary="Registrar un nuevo usuario",
    description="Registra un nuevo usuario, crea su perfil y le asigna el rol por defecto.",
    response_description="Confirmación de usuario registrado exitosamente"
)
def register(user: UserCreate):
    try:
        return service.register_user(user)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
