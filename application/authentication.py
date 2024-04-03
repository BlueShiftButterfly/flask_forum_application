import uuid
from flask import session
from application.user import (
    UsernameValidator,
    PasswordValidator,
    UsernameValidationResult,
    PasswordValidationResult,
    User,
    UserCredentialsData
)
from application.db import DatabaseBridge
from application.cryptography import check_password, hash_password

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
        user: User = self.db_bridge.get_user(username)
        if user is not None:
            if check_password(password, user.credentials_data.password_hash):
                print(f"User {user.credentials_data.username} authenticated")
                session["username"] = user.credentials_data.username
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
            new_user_credentials = UserCredentialsData(username, hash_password(password))
            new_user = User(uuid.uuid4(), new_user_credentials)
            self.db_bridge.add_user(new_user)
            print("Added user: ", new_user.uuid, new_user.credentials_data.username)
            session["username"] = new_user.credentials_data.username
            return True
        return False
