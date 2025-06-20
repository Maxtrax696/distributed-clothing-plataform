from pydantic import BaseModel
from typing import Optional
from datetime import date


class Profile(BaseModel):
    user_id: str
    full_name: Optional[str]
    birth_date: Optional[date]
    phone_number: Optional[str]


class ProfileUpdate(BaseModel):
    full_name: Optional[str]
    birth_date: Optional[date]
    phone_number: Optional[str]
