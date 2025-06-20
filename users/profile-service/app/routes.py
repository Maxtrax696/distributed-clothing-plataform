from fastapi import APIRouter


router = APIRouter(prefix="/api/profiles")


@router.get("/")
def get_profiles():
    return {"message": "Listando perfiles"}
