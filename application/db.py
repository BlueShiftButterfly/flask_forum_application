from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from application.user import User

class DatabaseBridge:
    def __init__(self, app, debug: bool = False) -> None:
        self.__users:dict[str, User] = {}
        self.__taken_usernames = set()
        self.__app = app
        self.__db = SQLAlchemy(app)
        self.__debug = debug

    def add_user(self, user: User):
        if self.__debug:
            self.__users[user.credentials_data.username] = user
            self.__taken_usernames.add(user.credentials_data.username)
        else:
            pass

    def get_user(self, username: str):
        if self.__debug:
            if username not in self.__users:
                return None
            return self.__users[username]
        else:
            pass

    def get_usernames(self):
        if self.__debug:
            return self.__taken_usernames
        else:
            pass
