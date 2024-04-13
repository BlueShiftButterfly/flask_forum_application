import uuid
from dataclasses import dataclass
from application.timestamp import get_utc_timestamp

def create_forum(url_name: str, display_name: str):
    return Forum(-1, uuid.uuid4(), url_name, display_name, get_utc_timestamp())

@dataclass
class Forum:
    db_id: int
    uuid: str
    url_name: str
    display_name: str
    creation_timestamp: str

    @property
    def url(self):
        return "/forum/"+self.url_name
