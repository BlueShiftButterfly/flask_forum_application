import uuid
from dataclasses import dataclass
from application.timestamp import get_utc_timestamp

def create_user(username: str, password_hash: str):
    return User(str(uuid.uuid4()), username, password_hash, get_utc_timestamp(), True, True, False)

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
