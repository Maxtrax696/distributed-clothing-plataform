from typing import Optional
from app.core.db import get_connection

class RoleRepository:
    def update_role(self, role_id: int, name: Optional[str], description: Optional[str]):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT id FROM roles WHERE id = %s", (role_id,))
        if not cur.fetchone():
            conn.close()
            return None

        query = "UPDATE roles SET "
        params = []

        if name is not None:
            query += "name = %s"
            params.append(name)

        if description is not None:
            if name is not None:
                query += ", "
            query += "description = %s"
            params.append(description)

        query += " WHERE id = %s"
        params.append(role_id)

        cur.execute(query, tuple(params))
        conn.commit()
        conn.close()

        return {"message": "Role successfully updated"}
