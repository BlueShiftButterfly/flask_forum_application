from dataclasses import dataclass
from application.permissions import Role

@dataclass
class User:
    db_id: int
    uuid: str
    username: str
    password_hash: str
    created_at: int
    is_authenticated: bool
    is_active: bool
    is_anonymous: bool
    role: Role

    def get_id(self):
        return self.uuid
