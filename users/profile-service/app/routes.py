from fastapi import APIRouter
from app.models import Profile
from app.db import get_connection


router = APIRouter(prefix="/api/profiles")


@router.get("/")
def get_profiles():
    return {"message": "Listando perfiles"}
