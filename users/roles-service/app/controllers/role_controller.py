from fastapi import APIRouter, HTTPException, Depends
from app.schemas.role_schema import RoleUpdateRequest, RoleResponse
from app.services.role_service import RoleService

router = APIRouter()
role_service = RoleService()

@router.put("/{role_id}", response_model=RoleResponse, summary="Actualizar un rol", description="Actualiza el nombre o descripción de un rol existente.")
def update_role(role_id: int, data: RoleUpdateRequest):
    updated = role_service.update_role(role_id, data)
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Rol no encontrado")
