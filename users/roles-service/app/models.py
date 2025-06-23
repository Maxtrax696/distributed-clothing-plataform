from pydantic import BaseModel
from typing import Optional

class Role(BaseModel):
    name: str
    description: Optional[str] = None

class RoleUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]

class UserRoleAssign(BaseModel):
    user_id: int
    role_id: int
