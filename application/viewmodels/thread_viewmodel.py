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
    forum_link: str
    forum_name: str
    viewer_can_edit: bool
    viewer_can_delete: bool
    viewer_can_comment: bool
