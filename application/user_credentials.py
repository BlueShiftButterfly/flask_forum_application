class UserCredentialsData:
    def __init__(self, username, password_hash) -> None:
        self.__username = username
        self.__password_hash = password_hash

    @property
    def username(self):
        return self.__username

    @property
    def password_hash(self):
        return self.__password_hash

class User:
    def __init__(self, uuid, credentials_data: UserCredentialsData) -> None:
        self.__uuid = uuid
        self.__credentials_data = credentials_data

    @property
    def uuid(self):
        return self.__uuid

    @property
    def credentials_data(self):
        return self.__credentials_data
