import uuid
import flask_login
from application.user import User
from application.db import DatabaseBridge
from application.cryptography import check_password, hash_password
from application.timestamp import get_utc_timestamp
from enum import Enum
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
            if check_password(password, user.password_hash):
                print(f"User {user.username} authenticated")
                #session["username"] = user.username
                flask_login.login_user(user)
                return True
        return False

    def signup(self, username, password):
        un_result = self.username_validator.validate(username, self.db_bridge.get_usernames())
        pw_result = self.password_validator.validate(password)
        print(un_result, pw_result)
        if(
            un_result == UsernameValidationResult.VALID and
            pw_result == PasswordValidationResult.VALID
        ):
            timestamp = get_utc_timestamp()
            new_user = User(uuid.uuid4(), username, hash_password(password), timestamp, True, True, False)
            self.db_bridge.add_user(new_user)
            print("Added user: ", new_user.uuid, new_user.username)
            #session["username"] = new_user.username
            flask_login.login_user(new_user)
            return True
        return False

    def logout(self):
        flask_login.logout_user()
