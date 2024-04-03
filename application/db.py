from application.user import User

class DatabaseBridge:
    def __init__(self) -> None:
        self.__users:dict[str, User] = {}
        self.__taken_usernames = set()

    def add_user(self, user: User):
        self.__users[user.credentials_data.username] = user
        self.__taken_usernames.add(user.credentials_data.username)

    def get_user(self, username: str):
        if username not in self.__users.keys():
            return None
        return self.__users[username]

    def get_usernames(self):
        return self.__taken_usernames