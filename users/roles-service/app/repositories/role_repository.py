from app.core.db import get_connection

class RoleRepository:
    def update_role(self, role_id: int, name: str, description: str):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM roles WHERE id = %s", (role_id,))
        if not cur.fetchone():
            conn.close()
            return None
        cur.execute("UPDATE roles SET name = %s, description = %s WHERE id = %s",
                    (name, description, role_id))
        conn.commit()
        conn.close()
        return {"message": "Role successfully updated"}
