from fastapi import APIRouter
from app.models import Profile
from app.db import get_connection


router = APIRouter(prefix="/api/profiles")

@router.post("/")
def create_profile(profile: Profile):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO profiles (user_id, full_name, birth_date, phone_number)
        VALUES (%s, %s, %s, %s)
    """, (profile.user_id, profile.full_name, profile.birth_date, profile.phone_number))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Perfil creado"}

#Temporal change