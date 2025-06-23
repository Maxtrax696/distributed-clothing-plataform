from fastapi import APIRouter, HTTPException
from app.db import get_connection
from app.models import Profile, ProfileUpdate

router = APIRouter(prefix="/api/profile")

@router.post("/")
def create_profile(profile: Profile):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE id = %s", (profile.user_id,))
    if not cur.fetchone():
        raise HTTPException(status_code=404, detail="User not found")

    cur.execute("""
        INSERT INTO profiles (user_id, full_name, birth_date, phone_number)
        VALUES (%s, %s, %s, %s)
    """, (profile.user_id, profile.full_name, profile.birth_date, profile.phone_number))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Profile created successfully"}

@router.get("/{user_id}")
def get_profile(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT full_name, birth_date, phone_number FROM profiles WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Profile not found")
    return {
        "user_id": user_id,
        "full_name": row[0],
        "birth_date": row[1],
        "phone_number": row[2]
    }

@router.put("/{user_id}")
def update_profile(user_id: int, data: ProfileUpdate):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM profiles WHERE user_id = %s", (user_id,))
    if not cur.fetchone():
        raise HTTPException(status_code=404, detail="Profile not found")

    if data.full_name:
        cur.execute("UPDATE profiles SET full_name = %s WHERE user_id = %s", (data.full_name, user_id))
    if data.birth_date:
        cur.execute("UPDATE profiles SET birth_date = %s WHERE user_id = %s", (data.birth_date, user_id))
    if data.phone_number:
        cur.execute("UPDATE profiles SET phone_number = %s WHERE user_id = %s", (data.phone_number, user_id))

    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Profile updated successfully"}
