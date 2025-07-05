from fastapi import APIRouter
from app.models.profile_schema import Profile, ProfileUpdate
from app.services.profile_service import ProfileService

router = APIRouter(prefix="/api/profiles")
service = ProfileService()

@router.get("/{user_id}")
def get_profile(user_id: int):
    return service.get_profile(user_id)

@router.get("/", tags=["Profiles"], summary="Listar perfiles")
def list_profiles():
    return service.list_profiles()

@router.put("/{user_id}")
def update_profile(user_id: int, data: ProfileUpdate):
    return service.update_profile(user_id, data)

@router.delete("/{user_id}")
def delete_profile(user_id: int):
    return service.delete_profile(user_id)
