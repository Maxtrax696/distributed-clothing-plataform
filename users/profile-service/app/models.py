from pydantic import BaseModel
from typing import Optional
from datetime import date

class Profile(BaseModel):
    user_id: int
<<<<<<< HEAD
    full_name: Optional[str]
    birth_date: Optional[date]
    phone_number: Optional[str]
=======
    full_name: str
    birth_date: date
    phone_number: str
>>>>>>> qa

class ProfileUpdate(BaseModel):
    full_name: Optional[str]
    birth_date: Optional[date]
    phone_number: Optional[str]
