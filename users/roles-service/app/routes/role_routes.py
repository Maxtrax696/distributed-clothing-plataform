from fastapi import APIRouter, HTTPException
from app.models.role_model import RoleUpdate
from app.services.role_service import RoleService

router = APIRouter(prefix="/api/roles", tags=["Roles"])
role_service = RoleService()

@router.put("/{role_id}")
def update_role(role_id: int, role: RoleUpdate):
    if role.name is None and role.description is None:
        raise HTTPException(status_code=400, detail="No data provided for update")

    result = role_service.update_role(role_id, role.name, role.description)
    if result is None:
        raise HTTPException(status_code=404, detail="Role not found")
    
    return result