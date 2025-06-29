import os
import requests

def assign_default_role(user_id: int):
    roles_url = os.getenv("ROLES_SERVICE_URL", "http://roles-service:8001")
    response = requests.post(f"{roles_url}/api/roles/auto-assign/{user_id}")
    if response.status_code != 200:
        raise Exception("Role assignment failed")
