from fastapi import APIRouter, HTTPException
from app.models import Role, RoleUpdate
from app.db import get_connection

router = APIRouter(prefix="/api/roles")

@router.get("/")
def list_roles():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, description FROM roles")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": row[0], "name": row[1], "description": row[2]} for row in rows]

@router.get("/{role_id}")
def get_role(role_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, description FROM roles WHERE id = %s", (role_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Role not found")
    return {"id": row[0], "name": row[1], "description": row[2]}

@router.post("/")
def create_role(role: Role):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO roles (name, description) VALUES (%s, %s)", (role.name, role.description))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Role successfully created"}

@router.put("/{role_id}")
def update_role(role_id: int, role: RoleUpdate):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE roles SET name = %s, description = %s WHERE id = %s", (role.name, role.description, role_id))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Role successfully updated"}

@router.delete("/{role_id}")
def delete_role(role_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM roles WHERE id = %s", (role_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Role successfully deleted"}
