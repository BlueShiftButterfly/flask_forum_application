from enum import Enum
from dataclasses import dataclass
from application.string_validator import is_length_valid, are_characters_valid

class UsernameValidationResult(Enum):
    VALID = 0
    NOT_UNIQUE = 1
    INVALID_LENGTH = 2
    INVALID_CHARACTERS = 4

class PasswordValidationResult(Enum):
    VALID = 0
    INVALID_LENGTH = 1
    INVALID_CHARACTERS = 2

class UsernameValidator:
    def __init__(
        self,
        min_length: int,
        max_length: int,
        valid_characters: set[str]
    ) -> None:
        self.min_length = min_length
        self.max_length = max_length
        self.valid_characters = valid_characters

    def validate(self, username: str, other_usernames: set[str]) -> UsernameValidationResult:
        if username in other_usernames:
            return UsernameValidationResult.NOT_UNIQUE
        if not is_length_valid(username, self.min_length, self.max_length):
            return UsernameValidationResult.INVALID_LENGTH
        if not are_characters_valid(username, self.valid_characters):
            return UsernameValidationResult.INVALID_CHARACTERS
        return UsernameValidationResult.VALID

class PasswordValidator:
    def __init__(
        self,
        min_length: int,
        max_length: int,
        valid_characters: set[str]
    ) -> None:
        self.min_length = min_length
        self.max_length = max_length
        self.valid_characters = valid_characters

    def validate(self, password: str) -> PasswordValidationResult:
        if not is_length_valid(password, self.min_length, self.max_length):
            return PasswordValidationResult.INVALID_LENGTH
        if not are_characters_valid(password, self.valid_characters):
            return PasswordValidationResult.INVALID_CHARACTERS
        return PasswordValidationResult.VALID

@dataclass
class User:
    uuid:str
    username: str
    password_hash: str
    creation_timestamp: int
    is_authenticated: bool
    is_active: bool
    is_anonymous: bool

    def get_id(self):
        return self.uuid
