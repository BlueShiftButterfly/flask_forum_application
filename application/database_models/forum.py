from dataclasses import dataclass

@dataclass
class Forum:
    db_id: int
    uuid: str
    url_name: str
    display_name: str
    forum_description: str
    created_at: int
    creator_id: int
    is_invite_only: bool

    @property
    def url(self):
        return "/forum/"+self.url_name
