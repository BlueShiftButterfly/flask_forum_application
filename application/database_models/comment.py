from dataclasses import dataclass
from application.database_models.user import User
from application.database_models.thread import Thread

@dataclass
class Comment:
    db_id: int
    uuid: str
    content: str
    poster: User
    thread: Thread
    is_reply: bool
    reply_comment_id: int
    creation_timestamp: int
    last_edit_timestamp: int
