from fastapi import APIRouter, HTTPException, Query
from app.models import UserCreate
from app.db import get_connection
import bcrypt
import requests
import os

router = APIRouter(prefix="/api/register")

<<<<<<< HEAD

=======
>>>>>>> qa
@router.post("/")
def register_user(user: UserCreate):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id FROM users WHERE email = %s", (user.email,))
        if cur.fetchone():
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_pw = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

        cur.execute("""
            INSERT INTO users (
                first_name, last_name, birth_date,
                email, password, phone_number
            ) VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (
            user.first_name,
            user.last_name,
            user.birth_date,
            user.email,
            hashed_pw.decode('utf-8'),
            user.phone_number
        ))
        user_id = cur.fetchone()[0]
        conn.commit()
    finally:
        cur.close()
        conn.close()

<<<<<<< HEAD
=======
    # Llamar al roles-service para asignar rol "cliente"
>>>>>>> qa
    try:
        roles_url = os.getenv("ROLES_SERVICE_URL", "http://roles-service:8001")
        response = requests.post(f"{roles_url}/api/roles/auto-assign/{user_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="User created but role assignment failed.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"User created but role assignment error: {str(e)}")

    return {"message": "User registered and role assigned successfully"}

<<<<<<< HEAD

=======
>>>>>>> qa
@router.get("/check-email")
def check_email_exists(email: str = Query(...)):
    conn = get_connection()
    cur = conn.cursor()
<<<<<<< HEAD
    try:
        cur.execute("SELECT 1 FROM users WHERE email = %s", (email,))
        exists = cur.fetchone() is not None
        return {"exists": exists}
    finally:
        cur.close()
        conn.close()


@router.get("/all")
def get_all_users():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT id, first_name, last_name, birth_date, email, phone_number, is_active, created_at
            FROM users
            ORDER BY created_at DESC
        """)
        rows = cur.fetchall()
        return [
            {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "birth_date": row[3],
                "email": row[4],
                "phone_number": row[5],
                "is_active": row[6],
                "created_at": row[7]
            }
            for row in rows
        ]
    finally:
        cur.close()
        conn.close()


@router.get("/email/{email}")
def get_user_by_email(email: str):
    email = email.strip().lower()  # limpiar espacios y convertir a minúsculas
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT id, first_name, last_name, email
            FROM users
            WHERE LOWER(email) = %s
        """, (email,))
        row = cur.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="User not found")
        return {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email": row[3]
        }
    finally:
        cur.close()
        conn.close()
=======
    cur.execute("SELECT 1 FROM users WHERE email = %s", (email,))
    exists = cur.fetchone() is not None
    cur.close()
    conn.close()
    return {"exists": exists}

@router.get("/email/{email}")
def get_user_by_email(email: str):
    email = email.strip().lower()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, first_name, last_name, email
        FROM users
        WHERE LOWER(email) = %s
    """, (email,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": row[0],
        "first_name": row[1],
        "last_name": row[2],
        "email": row[3]
    }
>>>>>>> qa

@router.get("/search-by-username")
def search_users_by_email_username(username: str = Query(..., min_length=1)):
    conn = get_connection()
    cur = conn.cursor()
<<<<<<< HEAD
    try:
        cur.execute("""
            SELECT id, first_name, last_name, email
            FROM users
            WHERE LOWER(SPLIT_PART(email, '@', 1)) LIKE %s
        """, (f"%{username.strip().lower()}%",))
        rows = cur.fetchall()
        if not rows:
            return []
        return [
            {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3]
            }
            for row in rows
        ]
    finally:
        cur.close()
        conn.close()
=======
    cur.execute("""
        SELECT id, first_name, last_name, email
        FROM users
        WHERE LOWER(SPLIT_PART(email, '@', 1)) LIKE %s
    """, (f"%{username.strip().lower()}%",))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email": row[3]
        } for row in rows
    ]
>>>>>>> qa
