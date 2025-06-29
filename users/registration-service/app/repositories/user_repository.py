from app.core.db import get_connection

class UserRepository:
    def __init__(self):
        self.conn = get_connection()

    def email_exists(self, email: str) -> bool:
        with self.conn.cursor() as cur:
            cur.execute("SELECT 1 FROM users WHERE email = %s", (email,))
            return cur.fetchone() is not None

    def create_user(self, user_data: dict) -> int:
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO users (first_name, last_name, birth_date, email, password, phone_number)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (
                user_data["first_name"],
                user_data["last_name"],
                user_data["birth_date"],
                user_data["email"],
                user_data["password"],
                user_data["phone_number"]
            ))
            user_id = cur.fetchone()[0]

            # Insertar en tabla profiles
            cur.execute("""
                INSERT INTO profiles (user_id, full_name, birth_date, phone_number)
                VALUES (%s, %s, %s, %s)
            """, (
                user_id,
                f"{user_data['first_name']} {user_data['last_name']}",
                user_data["birth_date"],
                user_data["phone_number"]
            ))

            # Asignar rol 'cliente' desde tabla roles
            cur.execute("SELECT id FROM roles WHERE name = %s", ("cliente",))
            role_row = cur.fetchone()
            if role_row:
                role_id = role_row[0]
                cur.execute("INSERT INTO user_roles (user_id, role_id) VALUES (%s, %s)", (user_id, role_id))

            self.conn.commit()
            return user_id
