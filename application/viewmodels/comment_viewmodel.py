from dataclasses import dataclass

@dataclass
class CommentViewmodel:
    content: str
    poster_username: str
    localized_date: str
    last_edited_localized_date: str
    link: str
    is_reply: bool
    reply_content: str
