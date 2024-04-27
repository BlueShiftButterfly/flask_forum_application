from dataclasses import dataclass
from application.database_models.user import User

@dataclass
class Forum:
    db_id: int
    uuid: str
    url_name: str
    display_name: str
    forum_description: str
    created_at: int
    creator: User
    is_invite_only: bool
    invited_users: set

    @property
    def url(self):
        return "/forum/"+self.url_name
