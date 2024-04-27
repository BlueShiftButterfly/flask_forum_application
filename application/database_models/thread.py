from dataclasses import dataclass
from application.database_models.user import User
from application.database_models.forum import Forum

@dataclass
class Thread:
    db_id: int
    uuid: str
    title: str
    content: str
    poster: User
    forum: Forum
    created_at: int
    last_edited_at: int
