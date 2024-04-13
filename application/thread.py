from dataclasses import dataclass
from shortuuid import ShortUUID
from application.timestamp import get_utc_timestamp

def create_thread(title: str, content: str, poster_id: int, forum_id: int):
    return Thread(ShortUUID().uuid(), title, content, poster_id, forum_id, get_utc_timestamp())

@dataclass
class Thread:
    uuid: str
    title: str
    content: str
    poster_id: int
    forum_id: int
    creation_timestamp: int
