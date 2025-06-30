from app.repositories.user_repository import UserRepository
import bcrypt

class RegistrationService:
    def __init__(self):
        self.repo = UserRepository()

    def register_user(self, user_data):
        if self.repo.email_exists(user_data.email):
            raise ValueError("Email already registered")

        hashed_pw = bcrypt.hashpw(
            user_data.password.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')  # solo se decodifica el resultado final

        user_dict = user_data.dict()
        user_dict["password"] = hashed_pw

        user_id = self.repo.create_user(user_dict)
        return {"message": "User, profile and role assigned successfully"}
