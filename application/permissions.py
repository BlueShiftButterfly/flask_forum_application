from dataclasses import dataclass
from enum import Enum
from application.database_models.forum import Forum
from application.database_models.thread import Thread
from application.database_models.comment import Comment

class PermissionLevel(Enum):
    NONE = 0
    OWNED_ONLY = 1
    ALL_PUBLIC = 2
    FULL = 3

class ContentAction(Enum):
    VIEW = 0
    CREATE = 1
    EDIT = 2
    DELETE = 3

@dataclass(frozen=True)
class Role:
    db_id: int
    forum_permissions: dict[ContentAction, PermissionLevel]
    thread_permissions: dict[ContentAction, PermissionLevel]
    comment_permissions: dict[ContentAction, PermissionLevel]

ADMINISTRATOR = Role(
    0,
    {
        ContentAction.VIEW: PermissionLevel.FULL,
        ContentAction.CREATE: PermissionLevel.FULL,
        ContentAction.EDIT: PermissionLevel.FULL,
        ContentAction.DELETE: PermissionLevel.FULL
    },
    {
        ContentAction.VIEW: PermissionLevel.FULL,
        ContentAction.CREATE: PermissionLevel.FULL,
        ContentAction.EDIT: PermissionLevel.FULL,
        ContentAction.DELETE: PermissionLevel.FULL
    },
    {
        ContentAction.VIEW: PermissionLevel.FULL,
        ContentAction.CREATE: PermissionLevel.FULL,
        ContentAction.EDIT: PermissionLevel.FULL,
        ContentAction.DELETE: PermissionLevel.FULL
    }
)

STANDARD = Role(
    1,
    {
        ContentAction.VIEW: PermissionLevel.ALL_PUBLIC,
        ContentAction.CREATE: PermissionLevel.NONE,
        ContentAction.EDIT: PermissionLevel.NONE,
        ContentAction.DELETE: PermissionLevel.NONE
    },
    {
        ContentAction.VIEW: PermissionLevel.ALL_PUBLIC,
        ContentAction.CREATE: PermissionLevel.FULL,
        ContentAction.EDIT: PermissionLevel.OWNED_ONLY,
        ContentAction.DELETE: PermissionLevel.OWNED_ONLY
    },
    {
        ContentAction.VIEW: PermissionLevel.ALL_PUBLIC,
        ContentAction.CREATE: PermissionLevel.FULL,
        ContentAction.EDIT: PermissionLevel.OWNED_ONLY,
        ContentAction.DELETE: PermissionLevel.OWNED_ONLY
    }
)

ANONYMOUS = Role(
    2,
    {
        ContentAction.VIEW: PermissionLevel.ALL_PUBLIC,
        ContentAction.CREATE: PermissionLevel.NONE,
        ContentAction.EDIT: PermissionLevel.NONE,
        ContentAction.DELETE: PermissionLevel.NONE
    },
    {
        ContentAction.VIEW: PermissionLevel.ALL_PUBLIC,
        ContentAction.CREATE: PermissionLevel.NONE,
        ContentAction.EDIT: PermissionLevel.NONE,
        ContentAction.DELETE: PermissionLevel.NONE
    },
    {
        ContentAction.VIEW: PermissionLevel.ALL_PUBLIC,
        ContentAction.CREATE: PermissionLevel.NONE,
        ContentAction.EDIT: PermissionLevel.NONE,
        ContentAction.DELETE: PermissionLevel.NONE
    }
)

ROLE_LOOKUP = [
    ADMINISTRATOR,
    STANDARD,
    ANONYMOUS
]

def check_permissions_forum(user, action: ContentAction, forum: Forum=None) -> bool:
    permission_level = user.role.forum_permissions[action]
    if permission_level is PermissionLevel.OWNED_ONLY and forum is not None:
        if forum.creator_id == user.db_id:
            return True
    if permission_level is PermissionLevel.FULL or permission_level is PermissionLevel.ALL_PUBLIC:
        return True
    return False

def check_permissions_thread(user, action: ContentAction, thread: Thread=None) -> bool:
    permission_level = user.role.thread_permissions[action]
    if permission_level is PermissionLevel.OWNED_ONLY and thread is not None:
        if thread.poster_id == user.db_id:
            return True
    if permission_level is PermissionLevel.FULL or permission_level is PermissionLevel.ALL_PUBLIC:
        return True
    return False

def check_permissions_comment(user, action: ContentAction, comment: Comment=None) -> bool:
    permission_level = user.role.comment_permissions[action]
    if permission_level is PermissionLevel.OWNED_ONLY and comment is not None:
        if comment.poster_id == user.db_id:
            return True
    if permission_level is PermissionLevel.FULL or permission_level is PermissionLevel.ALL_PUBLIC:
        return True
    return False
