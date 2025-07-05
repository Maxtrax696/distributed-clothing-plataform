from pydantic import BaseModel
from typing import Optional

class AddressCreate(BaseModel):
    user_id: int
    street: str
    city: str
    state: str
    postal_code: str
    country: str
    address_type: str

class AddressUpdate(BaseModel):
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    address_type: Optional[str]
