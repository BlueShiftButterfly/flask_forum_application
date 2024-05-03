from dataclasses import dataclass

@dataclass
class ThreadViewmodel:
    title: str
    content: str
    poster_username: str
    localized_post_date: str
    last_edited_localized_date: str
    link: str
    edit_link: str
    delete_link: str
