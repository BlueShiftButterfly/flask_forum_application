from application.user_credentials import User

class DatabaseBridge:
    def __init__(self) -> None:
        self.users:list[User] = []
        self.taken_usernames = set()

    def add_user(self, user: User):
        self.users.append(user)
        self.taken_usernames.add(user.credentials_data.username)

    def get_user(self):
        pass
