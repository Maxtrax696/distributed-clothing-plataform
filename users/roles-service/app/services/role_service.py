from typing import Optional
from app.repositories.role_repository import RoleRepository

class RoleService:
    def __init__(self):
        self.repository = RoleRepository()

    def update_role(self, role_id: int, name: Optional[str], description: Optional[str]):
        return self.repository.update_role(role_id, name, description)
