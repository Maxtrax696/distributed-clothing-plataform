from pydantic import BaseModel, EmailStr, Field
from datetime import date

class UserCreate(BaseModel):
    first_name: str = Field(..., example="Juan")
    last_name: str = Field(..., example="Pérez")
    birth_date: date = Field(..., example="1990-01-15")
    email: EmailStr = Field(..., example="juan.perez@example.com")
    password: str = Field(..., example="12345678")
    phone_number: str = Field(..., example="+593987654321")
