import flask_login
from application.database_models.user import User
from application.db import DatabaseBridge
from application.cryptography import check_password, hash_password
from enum import Enum
from application.string_validator import is_length_valid, are_characters_valid
from application.permissions import STANDARD, ANONYMOUS

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
        self.validation_messages = {
            UsernameValidationResult.VALID: "Username is valid.",
            UsernameValidationResult.NOT_UNIQUE: "Username is already taken.",
            UsernameValidationResult.INVALID_LENGTH: f"Username is too long or too short. It should be {self.min_length}-{self.max_length} characters long.",
            UsernameValidationResult.INVALID_CHARACTERS: "Username contains invalid characters."
        }

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
        self.validation_messages = {
            PasswordValidationResult.VALID: "Password is valid.",
            PasswordValidationResult.INVALID_LENGTH: f"Password is too long or too short. It should be {self.min_length}-{self.max_length} characters long.",
            PasswordValidationResult.INVALID_CHARACTERS: "Password contains invalid characters."
        }

    def validate(self, password: str) -> PasswordValidationResult:
        if not is_length_valid(password, self.min_length, self.max_length):
            return PasswordValidationResult.INVALID_LENGTH
        if not are_characters_valid(password, self.valid_characters):
            return PasswordValidationResult.INVALID_CHARACTERS
        return PasswordValidationResult.VALID

class Authenticator:
    def __init__(
        self,
        db_bridge: DatabaseBridge,
        username_validator: UsernameValidator,
        password_validator: PasswordValidator
    ) -> None:
        self.db_bridge = db_bridge
        self.username_validator = username_validator
        self.password_validator = password_validator

    def login(self, username, password):
        user: User = self.db_bridge.get_user_by_username(username)
        if user is not None:
            if flask_login.login_user(user) and check_password(password, user.password_hash):
                return True
        return False

    def signup(self, username, password):
        un_result = self.username_validator.validate(username, self.db_bridge.get_usernames())
        pw_result = self.password_validator.validate(password)
        if(
            un_result == UsernameValidationResult.VALID and
            pw_result == PasswordValidationResult.VALID
        ):
            new_user = self.db_bridge.create_user(username, hash_password(password), STANDARD)
            flask_login.login_user(new_user)
            return True
        return False

    def get_anonymous_user(self):
        return User(
            -1,
            "",
            "ANONYMOUS",
            "",
            -1,
            False,
            False,
            True,
            ANONYMOUS
        )

    def logout(self):
        flask_login.logout_user()
