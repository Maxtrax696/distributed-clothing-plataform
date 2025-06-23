from fastapi import APIRouter, HTTPException
from app.models import Profile, ProfileUpdate
from app.db import get_connection

router = APIRouter(prefix="/api/profiles")


@router.get("/")
def get_all_profiles():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT p.user_id, p.full_name, p.birth_date, p.phone_number, u.email
            FROM profiles p
            JOIN users u ON p.user_id = u.id
        """)
        rows = cur.fetchall()
        return [
            {
                "user_id": row[0],
                "full_name": row[1],
                "birth_date": row[2],
                "phone_number": row[3],
                "email": row[4]
            }
            for row in rows
        ]
    finally:
        cur.close()
        conn.close()


@router.get("/{user_id}")
def get_profile(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT p.full_name, p.birth_date, p.phone_number, u.email
            FROM profiles p
            JOIN users u ON p.user_id = u.id
            WHERE p.user_id = %s
        """, (user_id,))
        row = cur.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Profile not found")
        return {
            "user_id": user_id,
            "full_name": row[0],
            "birth_date": row[1],
            "phone_number": row[2],
            "email": row[3]
        }
    finally:
        cur.close()
        conn.close()


@router.post("/")
def create_profile(profile: Profile):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id FROM users WHERE id = %s", (profile.user_id,))
        if not cur.fetchone():
            raise HTTPException(status_code=400, detail="User ID does not exist in users table")

        cur.execute("""
            INSERT INTO profiles (user_id, full_name, birth_date, phone_number)
            VALUES (%s, %s, %s, %s)
        """, (
            profile.user_id,
            profile.full_name,
            profile.birth_date,
            profile.phone_number,
        ))
        conn.commit()
        return {"message": "Profile successfully created"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating profile: {str(e)}")
    finally:
        cur.close()
        conn.close()


@router.put("/{user_id}")
def update_profile(user_id: int, update: ProfileUpdate):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id FROM profiles WHERE user_id = %s", (user_id,))
        if not cur.fetchone():
            raise HTTPException(status_code=404, detail="Profile not found")

        cur.execute("""
            UPDATE profiles
            SET full_name = %s, birth_date = %s, phone_number = %s
            WHERE user_id = %s
        """, (
            update.full_name,
            update.birth_date,
            update.phone_number,
            user_id
        ))
        conn.commit()
        return {"message": "Profile successfully updated"}
    finally:
        cur.close()
        conn.close()


@router.delete("/{user_id}")
def delete_profile(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM profiles WHERE user_id = %s", (user_id,))
        conn.commit()
        return {"message": "Profile successfully deleted"}
    finally:
        cur.close()
        conn.close()
