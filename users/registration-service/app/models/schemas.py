from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    email: EmailStr
    password: str
    phone_number: str
