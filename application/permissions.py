from dataclasses import dataclass
from enum import Enum

class PermissionLevel(Enum):
    NONE = 0
    OWNED_ONLY = 1
    ALL_PUBLIC = 2
    FULL = 3

class RoleAction(Enum):
    VIEW = 0
    CREATE = 1
    EDIT = 2
    DELETE = 3

@dataclass(frozen=True)
class Role:
    forum_permissions: dict[RoleAction, PermissionLevel]
    thread_permissions: dict[RoleAction, PermissionLevel]
    comment_permissions: dict[RoleAction, PermissionLevel]

ADMINISTRATOR = Role(
    {
        RoleAction.VIEW: PermissionLevel.FULL,
        RoleAction.CREATE: PermissionLevel.FULL,
        RoleAction.EDIT: PermissionLevel.FULL,
        RoleAction.DELETE: PermissionLevel.FULL
    },
    {
        RoleAction.VIEW: PermissionLevel.FULL,
        RoleAction.CREATE: PermissionLevel.FULL,
        RoleAction.EDIT: PermissionLevel.FULL,
        RoleAction.DELETE: PermissionLevel.FULL
    },
    {
        RoleAction.VIEW: PermissionLevel.FULL,
        RoleAction.CREATE: PermissionLevel.FULL,
        RoleAction.EDIT: PermissionLevel.FULL,
        RoleAction.DELETE: PermissionLevel.FULL
    }
)

REGULAR = Role(
    {
        RoleAction.VIEW: PermissionLevel.ALL_PUBLIC,
        RoleAction.CREATE: PermissionLevel.NONE,
        RoleAction.EDIT: PermissionLevel.NONE,
        RoleAction.DELETE: PermissionLevel.NONE
    },
    {
        RoleAction.VIEW: PermissionLevel.ALL_PUBLIC,
        RoleAction.CREATE: PermissionLevel.FULL,
        RoleAction.EDIT: PermissionLevel.OWNED_ONLY,
        RoleAction.DELETE: PermissionLevel.OWNED_ONLY
    },
    {
        RoleAction.VIEW: PermissionLevel.ALL_PUBLIC,
        RoleAction.CREATE: PermissionLevel.FULL,
        RoleAction.EDIT: PermissionLevel.OWNED_ONLY,
        RoleAction.DELETE: PermissionLevel.OWNED_ONLY
    }
)

ANONYMOUS = Role(
    {
        RoleAction.VIEW: PermissionLevel.ALL_PUBLIC,
        RoleAction.CREATE: PermissionLevel.NONE,
        RoleAction.EDIT: PermissionLevel.NONE,
        RoleAction.DELETE: PermissionLevel.NONE
    },
    {
        RoleAction.VIEW: PermissionLevel.ALL_PUBLIC,
        RoleAction.CREATE: PermissionLevel.NONE,
        RoleAction.EDIT: PermissionLevel.NONE,
        RoleAction.DELETE: PermissionLevel.NONE
    },
    {
        RoleAction.VIEW: PermissionLevel.ALL_PUBLIC,
        RoleAction.CREATE: PermissionLevel.NONE,
        RoleAction.EDIT: PermissionLevel.NONE,
        RoleAction.DELETE: PermissionLevel.NONE
    }
)
