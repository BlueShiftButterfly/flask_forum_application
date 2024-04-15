from dataclasses import dataclass

@dataclass
class Comment:
    db_id: int
    uuid: str
    content: str
    poster_id: int
    thread_id: int
    is_reply: bool
    reply_comment_id: int
    creation_timestamp: int
    last_edit_timestamp: int
