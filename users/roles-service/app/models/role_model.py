from pydantic import BaseModel

class RoleUpdateRequest(BaseModel):
    name: str
    description: str

class RoleResponse(BaseModel):
    id: int
    name: str
    description: str
