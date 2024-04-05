import uuid
from flask import session
import flask_login
from application.user import (
    UsernameValidator,
    PasswordValidator,
    UsernameValidationResult,
    PasswordValidationResult,
    User
)
from application.db import DatabaseBridge
from application.cryptography import check_password, hash_password
from application.timestamp import get_utc_timestamp

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
