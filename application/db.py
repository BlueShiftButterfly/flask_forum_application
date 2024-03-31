from application.user_credentials import User

class DatabaseBridge:
    def __init__(self) -> None:
        self.users:dict[str, User] = {}
        self.taken_usernames = set()

    def add_user(self, user: User):
        self.users[user.credentials_data.username] = user
        self.taken_usernames.add(user.credentials_data.username)

    def get_user(self, username: str):
        if username not in self.users.keys:
            return None
        return self.users[username]
