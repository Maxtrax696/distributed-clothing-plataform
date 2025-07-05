from fastapi import HTTPException
from app.models.address_schema import AddressCreate, AddressUpdate
from app.services import address_service

def create_address(data: AddressCreate):
    return address_service.create(data)

def get_user_addresses(user_id: int):
    return address_service.get_by_user(user_id)

def update_address(address_id: int, data: AddressUpdate):
    result = address_service.update(address_id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Dirección no encontrada")
    return {"message": "Dirección actualizada"}

def delete_address(address_id: int):
    result = address_service.delete(address_id)
    if not result:
        raise HTTPException(status_code=404, detail="Dirección no encontrada")
    return {"message": "Dirección eliminada correctamente"}
