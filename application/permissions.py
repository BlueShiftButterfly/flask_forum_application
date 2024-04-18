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
