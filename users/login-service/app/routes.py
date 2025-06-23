from fastapi import APIRouter, HTTPException
from app.models import LoginRequest
from app.db import get_connection
from passlib.context import CryptContext
from jose import jwt
import os

router = APIRouter(prefix="/api")

<<<<<<< HEAD
# Seguridad
=======
>>>>>>> qa
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "secret")
ALGORITHM = "HS256"

@router.post("/login")
def login_user(credentials: LoginRequest):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, email, password FROM users WHERE email = %s", (credentials.email,))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if not user:
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")

    user_id, email, hashed_password = user

    if not pwd_context.verify(credentials.password, hashed_password):
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")

    token = jwt.encode({"user_id": user_id, "email": email}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
