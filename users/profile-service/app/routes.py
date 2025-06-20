from fastapi import APIRouter, HTTPException
from app.models import Profile, ProfileUpdate
from app.db import get_connection

router = APIRouter(prefix="/api/profiles")


@router.get("/")
def get_all_profiles():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT user_id, full_name, birth_date, phone_number FROM profiles")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {
            "user_id": row[0],
            "full_name": row[1],
            "birth_date": row[2],
            "phone_number": row[3],
        }
        for row in rows
    ]


@router.get("/{user_id}")
def get_profile(user_id: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        cur.execute("SELECT ... FROM profiles WHERE user_id = %s", (user_id,))
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Profile not found")
    return {
        "user_id": user_id,
        "full_name": row[0],
        "birth_date": row[1],
        "phone_number": row[2],
    }


@router.post("/")
def create_profile(profile: Profile):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO profiles (user_id, full_name, birth_date, phone_number)
        VALUES (%s, %s, %s, %s)
        """,
        (
            profile.user_id,
            profile.full_name,
            profile.birth_date,
            profile.phone_number,
        ),
    )
    conn.commit()
    cur.close()
    conn.close()
    return {
        "message": "Profile successfully created"
    }


@router.put("/{user_id}")
def update_profile(user_id: str, update: ProfileUpdate):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM profiles WHERE user_id = %s", (user_id,))
    if not cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Profile not found")

    cur.execute(
        """
        UPDATE profiles
        SET full_name = %s, birth_date = %s, phone_number = %s
        WHERE user_id = %s
        """,
        (update.full_name, update.birth_date, update.phone_number, user_id),
    )
    conn.commit()
    cur.close()
    conn.close()
    return {
        "message": "Profile successfully updated"
    }


@router.delete("/{user_id}")
def delete_profile(user_id: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM profiles WHERE user_id = %s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {
        "message": "Profile successfully deleted"
    }
