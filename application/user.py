from dataclasses import dataclass

@dataclass
class User:
    uuid:str
    username: str
    password_hash: str
    creation_timestamp: int
    is_authenticated: bool
    is_active: bool
    is_anonymous: bool

    def get_id(self):
        return self.uuid
