from app.core.db import get_connection

class ProfileRepository:
    def __init__(self):
        self.conn = get_connection()

    def user_exists(self, user_id: int):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE id = %s", (user_id,))
            return cur.fetchone() is not None

    def get_profile(self, user_id: int):
        with self.conn.cursor() as cur:
            cur.execute("SELECT full_name, birth_date, phone_number FROM profiles WHERE user_id = %s", (user_id,))
            return cur.fetchone()

    def list_profiles(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT user_id, full_name, birth_date, phone_number FROM profiles")
            return cur.fetchall()

    def profile_exists(self, user_id: int):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id FROM profiles WHERE user_id = %s", (user_id,))
            return cur.fetchone() is not None

    def update(self, user_id, full_name, birth_date, phone_number):
        with self.conn.cursor() as cur:
            if full_name:
                cur.execute("UPDATE profiles SET full_name = %s WHERE user_id = %s", (full_name, user_id))
            if birth_date:
                cur.execute("UPDATE profiles SET birth_date = %s WHERE user_id = %s", (birth_date, user_id))
            if phone_number:
                cur.execute("UPDATE profiles SET phone_number = %s WHERE user_id = %s", (phone_number, user_id))
        self.conn.commit()

    def delete(self, user_id):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM profiles WHERE user_id = %s", (user_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
