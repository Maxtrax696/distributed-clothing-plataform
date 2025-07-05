from app.models.address_schema import AddressCreate, AddressUpdate
from app.repositories import address_repository

def create(data: AddressCreate):
    return address_repository.create_address(data)

def get_by_user(user_id: int):
    return address_repository.get_addresses_by_user(user_id)

def update(address_id: int, data: AddressUpdate):
    return address_repository.update_address(address_id, data)

def delete(address_id: int):
    return address_repository.delete_address(address_id)
