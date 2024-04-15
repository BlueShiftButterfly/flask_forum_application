import uuid
import shortuuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from application.database_models.user import User
from application.database_models.forum import Forum
from application.database_models.thread import Thread
from application.timestamp import get_utc_timestamp

class DatabaseBridge:
    def __init__(self, app) -> None:
        self.__app = app
        self.__db = SQLAlchemy(app)

    def create_user(self, username: str, password_hash: str) -> User:
        user_uuid = str(uuid.uuid4())
        user_timestamp = get_utc_timestamp()

        sql = "INSERT INTO users (uuid, username, password_hash, created_at, is_authenticated, is_active) VALUES (:uuid, :username, :password_hash, :created_at, :is_authenticated, :is_active) RETURNING id"
        sql_args = {
            "uuid": user_uuid,
            "username": username,
            "password_hash": password_hash,
            "created_at": user_timestamp,
            "is_authenticated": True,
            "is_active": True
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        self.__db.session.commit()
        if result is None or result[0] <= 0:
            return None
        return User(result[0], user_uuid, username, password_hash, user_timestamp, True, True, False)

    def remove_user(self, uuid: str):
        sql = "DELETE FROM users WHERE uuid=:uuid"
        sql_args = {
            "uuid": uuid
        }
        self.__db.session.execute(text(sql), sql_args)
        self.__db.session.commit()

    def get_user_by_username(self, username: str):
        sql = "SELECT id, uuid, username, password_hash, created_at, is_authenticated, is_active FROM users WHERE username=:username"
        sql_args = {
            "username": username
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        if result is None:
            return None
        return User(result[0], result[1], result[2], result[3], result[4], result[5], result[6], False)

    def get_user_by_uuid(self, uuid: str):
        sql = "SELECT id, uuid, username, password_hash, created_at, is_authenticated, is_active FROM users WHERE uuid=:uuid"
        sql_args = {
            "uuid": uuid
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        if result is None:
            return None
        return User(result[0], result[1], result[2], result[3], result[4], result[5], result[6], False)

    def get_user_by_id(self, db_id: int):
        sql = "SELECT id, uuid, username, password_hash, created_at, is_authenticated, is_active FROM users WHERE id=:id"
        sql_args = {
            "id": db_id
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        if result is None:
            return None
        return User(result[0], result[1], result[2], result[3], result[4], result[5], result[6], False)

    def get_user_db_id(self, uuid: str):
        sql = "SELECT id, uuid FROM users WHERE uuid=:uuid"
        sql_args = {
            "uuid": uuid
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        if result is None or result[1] != uuid:
            return None
        return result[0]

    def get_usernames(self):
        sql = "SELECT username FROM users"
        result = self.__db.session.execute(text(sql)).fetchall()
        if result is None:
            return None
        return set(result)

    def set_user_authentication_status(self, uuid: str, is_authenticated: bool):
        sql = "UPDATE users SET is_authenticated=:is_authenticated WHERE uuid=:uuid"
        sql_args = {
            "uuid": uuid,
            "is_authenticated": is_authenticated
        }
        self.__db.session.execute(text(sql), sql_args)
        self.__db.session.commit()

    def set_user_active_status(self, uuid: str, is_active: bool):
        sql = "UPDATE users SET is_active=:is_active WHERE uuid=:uuid"
        sql_args = {
            "uuid": uuid,
            "is_active": is_active
        }
        self.__db.session.execute(text(sql), sql_args)
        self.__db.session.commit()

    def create_forum(self, url_name: str, display_name: str, forum_description: str, creator_id: int) -> Forum:
        forum_uuid = str(uuid.uuid4())
        forum_timestamp = get_utc_timestamp()

        sql = "INSERT INTO forums (uuid, url_name, display_name, forum_description, created_at, creator_id) VALUES (:uuid, :url_name, :display_name, :forum_description, :created_at, :creator_id) RETURNING id"
        sql_args = {
            "uuid": forum_uuid,
            "url_name": url_name,
            "display_name": display_name,
            "forum_description": forum_description,
            "created_at": forum_timestamp,
            "creator_id": creator_id
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        self.__db.session.commit()
        if result is None or result[0] <= 0:
            return None
        return Forum(result[0], forum_uuid, url_name, display_name, forum_description, forum_timestamp, creator_id)

    def remove_forum(self, uuid: str):
        sql = "DELETE FROM forums WHERE uuid=:uuid"
        sql_args = {
            "uuid": uuid
        }
        self.__db.session.execute(text(sql), sql_args)
        self.__db.session.commit()

    def get_forum_by_url_name(self, url_name: str):
        sql = "SELECT id, uuid, url_name, display_name, forum_description, created_at, creator_id FROM forums WHERE url_name=:url_name"
        sql_args = {
            "url_name": url_name
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        if result is None:
            return None
        return Forum(result[0], result[1], result[2], result[3], result[4], result[5], result[6])

    def get_forum_by_uuid(self, uuid: str):
        sql = "SELECT id, uuid, url_name, display_name, forum_description, created_at, creator_id FROM forums WHERE uuid=:uuid"
        sql_args = {
            "uuid": uuid
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        if result is None:
            return None
        return Forum(result[0], result[1], result[2], result[3], result[4], result[5], result[6])

    def get_forum_by_id(self, db_id: int):
        sql = "SELECT id, uuid, url_name, display_name, forum_description, created_at, creator_id FROM forums WHERE id=:id"
        sql_args = {
            "id": db_id
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        if result is None:
            return None
        return Forum(result[0], result[1], result[2], result[3], result[4], result[5], result[6])

    def get_forum_db_id(self, uuid: str):
        sql = "SELECT id, uuid FROM forums WHERE uuid=:uuid"
        sql_args = {
            "uuid": uuid
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        if result is None or result[1] != uuid:
            return None
        return result[0]

    def get_all_forums(self):
        sql = "SELECT id, uuid, url_name, display_name, forum_description, created_at, creator_id FROM forums"
        result = self.__db.session.execute(text(sql)).fetchall()
        if result is None:
            return None
        forum_objects: list[Forum] = []
        for r in result:
            forum_objects.append(Forum(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
        return forum_objects

    def create_thread(self, title: str, content: str, poster_id: int, forum_id: int) -> Thread:
        thread_uuid = str(shortuuid.uuid())
        thread_timestamp = get_utc_timestamp()

        sql = "INSERT INTO threads (uuid, title, content, poster_id, forum_id, created_at, last_edited_at) VALUES (:uuid, :title, :content, :poster_id, :forum_id, :created_at, :last_edited_at) RETURNING id"
        sql_args = {
            "uuid": thread_uuid,
            "title": title,
            "content": content,
            "poster_id": poster_id,
            "forum_id": forum_id,
            "created_at": thread_timestamp,
            "last_edited_at": -1
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        self.__db.session.commit()
        if result is None or result[0] <= 0:
            return None
        return Thread(result[0], thread_uuid, title, content, poster_id, forum_id, thread_timestamp, -1)

    def remove_thread(self, uuid: str):
        sql = "DELETE FROM threads WHERE uuid=:uuid"
        sql_args = {
            "uuid": uuid
        }
        self.__db.session.execute(text(sql), sql_args)
        self.__db.session.commit()

    def get_thread_by_uuid(self, uuid: str):
        sql = "SELECT id, uuid, title, content, poster_id, forum_id, created_at, last_edited_at FROM threads WHERE uuid=:uuid"
        sql_args = {
            "uuid": uuid
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        if result is None:
            return None
        
        return Thread(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])

    def get_threads_in_forum(self, forum_id: int):
        sql = "SELECT id, uuid, title, content, poster_id, forum_id, created_at, last_edited_at FROM threads WHERE forum_id=:forum_id"
        sql_args = {
            "forum_id": forum_id
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchall()
        if result is None:
            return None
        thread_objects: list[Thread] = []
        for r in result:
            thread_objects.append(Thread(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))
        return thread_objects
