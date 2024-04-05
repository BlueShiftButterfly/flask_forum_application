from dataclasses import dataclass
from shortuuid import ShortUUID
from application.timestamp import get_utc_timestamp

def create_thread(title: str, content: str, poster_uuid: str, forum_uuid: str):
    return Thread(ShortUUID().uuid(), title, content, poster_uuid, forum_uuid, get_utc_timestamp())

@dataclass
class Thread:
    uuid: str
    title: str
    content: str
    poster_uuid: str
    forum_uuid: str
    creation_timestamp: int
