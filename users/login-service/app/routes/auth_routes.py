from fastapi import APIRouter, Query
from app.models.login_request import LoginRequest
from app.services.login_service import login_user, verify_token

router = APIRouter(prefix="/api")

@router.post("/login",
    tags=["Autenticación"],
    summary="Iniciar sesión",
    description="Valida las credenciales del usuario y retorna un token JWT válido para autenticar peticiones futuras.",
    response_description="Token JWT y tipo de autenticación")

def login(credentials: LoginRequest):
    return login_user(credentials.email, credentials.password)

@router.get(
    "/verify",
    tags=["Autenticación"],
    summary="Verificar token JWT",
    description="Valida que un token JWT proporcionado sea válido y no esté expirado.",
    response_description="Resultado de validación del token"
)
def verify(token: str = Query(..., description="Token JWT que se desea validar")):
    return verify_token(token)
