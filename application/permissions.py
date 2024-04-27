from dataclasses import dataclass
from enum import Enum

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

def check_permissions_forum(user, action: ContentAction, forum=None) -> bool:
    permission_level = user.role.forum_permissions[action]
    if permission_level is PermissionLevel.OWNED_ONLY and forum is not None:
        if forum.creator.db_id == user.db_id:
            return True
    if permission_level is PermissionLevel.ALL_PUBLIC and forum is not None:
        if forum.is_invite_only == False:
            return True
    if permission_level is PermissionLevel.FULL:
        return True
    return False

def check_permissions_thread(user, action: ContentAction, thread=None) -> bool:
    permission_level = user.role.thread_permissions[action]
    if permission_level is PermissionLevel.OWNED_ONLY and thread is not None:
        if thread.poster.db_id == user.db_id:
            return True
    if permission_level is PermissionLevel.ALL_PUBLIC and thread is not None:
        if thread.forum.is_invite_only == False:
            return True
    if permission_level is PermissionLevel.FULL:
        return True
    return False

def check_permissions_comment(user, action: ContentAction, comment=None) -> bool:
    permission_level = user.role.comment_permissions[action]
    if permission_level is PermissionLevel.OWNED_ONLY and comment is not None:
        if comment.poster.db_id == user.db_id:
            return True
    if permission_level is PermissionLevel.ALL_PUBLIC and comment is not None:
        if comment.thread.forum.is_invite_only == False:
            return True
    if permission_level is PermissionLevel.FULL:
        return True
    return False
