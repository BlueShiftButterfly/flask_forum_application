from dataclasses import dataclass

@dataclass
class ForumViewModel:
    display_name: str
    url_name: str
    description: str
    localized_creation_date: str
    creator_username: str
    is_invite_only: bool
    link: str
    edit_link: str
    delete_link: str
    thread_create_link: str
    viewer_can_edit: bool
    viewer_can_delete: bool
    viewer_can_create_thread: bool
