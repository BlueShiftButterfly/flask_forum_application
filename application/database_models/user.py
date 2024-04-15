from dataclasses import dataclass

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

    def get_id(self):
        return self.uuid
