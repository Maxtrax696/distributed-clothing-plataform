from fastapi import APIRouter, HTTPException
from app.db import get_connection
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/api/roles")

class Role(BaseModel):
    name: str
    description: Optional[str] = None

class RoleUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]

class UserRoleAssign(BaseModel):
    user_id: int
    role_id: int

@router.get("/")
def list_roles():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, description FROM roles")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1], "description": r[2]} for r in rows]

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
    cur.execute("SELECT id FROM roles WHERE id = %s", (role_id,))
    if not cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Role not found")
    cur.execute("UPDATE roles SET name = %s, description = %s WHERE id = %s",
                (role.name, role.description, role_id))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Role successfully updated"}

@router.delete("/{role_id}")
def delete_role(role_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM roles WHERE id = %s", (role_id,))
    if not cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Role not found")
    cur.execute("DELETE FROM roles WHERE id = %s", (role_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Role successfully deleted"}

@router.post("/assign")
def assign_role(data: UserRoleAssign):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM user_roles WHERE user_id = %s AND role_id = %s", (data.user_id, data.role_id))
    if cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=400, detail="Role already assigned to this user.")
    cur.execute("INSERT INTO user_roles (user_id, role_id) VALUES (%s, %s)", (data.user_id, data.role_id))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": f"Role {data.role_id} assigned to user {data.user_id}"}

@router.get("/user/{user_id}")
def get_roles_by_user(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT r.id, r.name, r.description
        FROM roles r
        JOIN user_roles ur ON r.id = ur.role_id
        WHERE ur.user_id = %s
    """, (user_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1], "description": r[2]} for r in rows]

@router.post("/auto-assign/{user_id}")
def auto_assign_cliente(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id FROM roles WHERE name = 'cliente'")
        cliente_role = cur.fetchone()
        if not cliente_role:
            raise HTTPException(status_code=404, detail="Rol 'cliente' no encontrado")

        role_id = cliente_role[0]
        cur.execute("SELECT 1 FROM user_roles WHERE user_id = %s AND role_id = %s", (user_id, role_id))
        if cur.fetchone():
            return {"message": "El usuario ya tiene el rol cliente"}

        cur.execute("INSERT INTO user_roles (user_id, role_id) VALUES (%s, %s)", (user_id, role_id))
        conn.commit()
        return {"message": f"Rol 'cliente' asignado automáticamente al usuario {user_id}"}
    finally:
        cur.close()
        conn.close()

@router.delete("/user/{user_id}")
def delete_user_roles(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM user_roles WHERE user_id = %s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": f"Todos los roles eliminados del usuario {user_id}"}
