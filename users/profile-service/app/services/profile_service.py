from fastapi import HTTPException
from app.repositories.profile_repository import ProfileRepository
from app.models.profile_schema import Profile, ProfileUpdate

class ProfileService:
    def __init__(self):
        self.repo = ProfileRepository()

    def get_profile(self, user_id: int):
        profile = self.repo.get_profile(user_id)
        self.repo.close()
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")
        return {
            "user_id": user_id,
            "full_name": profile[0],
            "birth_date": profile[1],
            "phone_number": profile[2],
        }

    def list_profiles(self):
        data = self.repo.list_profiles()
        self.repo.close()
        return [
            {
                "user_id": r[0],
                "full_name": r[1],
                "birth_date": r[2],
                "phone_number": r[3]
            }
            for r in data
        ]

    def update_profile(self, user_id: int, data: ProfileUpdate):
        if not self.repo.profile_exists(user_id):
            raise HTTPException(status_code=404, detail="Profile not found")
        self.repo.update(user_id, data.full_name, data.birth_date, data.phone_number)
        self.repo.close()
        return {"message": "Profile updated successfully"}

    def delete_profile(self, user_id: int):
        if not self.repo.profile_exists(user_id):
            raise HTTPException(status_code=404, detail="Profile not found")
        self.repo.delete(user_id)
        self.repo.close()
        return {"message": "Profile deleted successfully"}
