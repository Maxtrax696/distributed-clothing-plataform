from fastapi import HTTPException
from app.core.security import verify_password, create_token
from app.repositories.user_repository import get_user_by_email
from jose import jwt, JWTError
from app.config.settings import settings

def login_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")

    user_id, user_email, hashed_password = user

    if isinstance(hashed_password, memoryview):
        hashed_password = hashed_password.tobytes()
    if isinstance(hashed_password, bytes):
        try:
            hashed_password = bytes.fromhex(hashed_password.hex()).decode("utf-8")
        except:
            hashed_password = hashed_password.decode("utf-8")

        
    if not verify_password(password, hashed_password):
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")

    token = create_token({"user_id": user_id, "email": user_email})
    return {"access_token": token, "token_type": "bearer"}

def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return {
            "valid": True,
            "user_id": payload.get("user_id"),
            "email": payload.get("email")
        }
    except JWTError:
        return {
            "valid": False,
            "message": "Token inválido o expirado"
        }
