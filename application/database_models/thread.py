from dataclasses import dataclass

@dataclass
class Thread:
    db_id: int
    uuid: str
    title: str
    content: str
    poster_id: int
    forum_id: int
    created_at: int
    last_edited_at: int
