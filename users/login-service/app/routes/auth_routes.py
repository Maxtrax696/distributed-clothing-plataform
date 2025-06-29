from fastapi import APIRouter
from app.models.login_request import LoginRequest
from app.services.login_service import login_user

router = APIRouter(prefix="/api")

@router.post("/login")
def login(credentials: LoginRequest):
    return login_user(credentials.email, credentials.password)
