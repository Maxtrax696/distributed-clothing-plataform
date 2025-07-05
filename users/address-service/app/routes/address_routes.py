from fastapi import APIRouter
from app.controllers import address_controller
from app.models.address_schema import AddressCreate, AddressUpdate

router = APIRouter(prefix="/address", tags=["Addresses"])

router.post("/", response_model=dict)(address_controller.create_address)
router.get("/{user_id}", response_model=list)(address_controller.get_user_addresses)
router.put("/{address_id}", response_model=dict)(address_controller.update_address)
router.delete("/{address_id}", response_model=dict)(address_controller.delete_address)
