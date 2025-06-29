from app.repositories.role_repository import RoleRepository

class RoleService:
    def __init__(self):
        self.repository = RoleRepository()

    def update_role(self, role_id: int, name: str, description: str):
        return self.repository.update_role(role_id, name, description)

# --- app/routes/role_routes.py ---
from fastapi import APIRouter, HTTPException
from app.models.role_model import RoleUpdate
from app.services.role_service import RoleService

router = APIRouter(prefix="/api/roles")
service = RoleService()

@router.put("/{role_id}")
def update_role(role_id: int, role: RoleUpdate):
    updated = service.update_role(role_id, role.name, role.description)
    if not updated:
        raise HTTPException(status_code=404, detail="Role not found")
    return updated
