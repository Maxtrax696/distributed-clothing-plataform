from pydantic import BaseModel
from typing import Optional

class RoleUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]