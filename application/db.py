from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from application.user import User
from application.forum import Forum
from application.thread import Thread

class DatabaseBridge:
    def __init__(self, app, debug: bool = False) -> None:
        self.__app = app
        self.__db = SQLAlchemy(app)
        self.__debug = debug

    def add_user(self, user: User):
        sql = "INSERT INTO users (uuid, username, password_hash, created, is_authenticated, is_active) VALUES (:uuid_var, :username_var, :passwordhash_var, :created_var, :is_authenticated_var, :is_active_var)"
        sql_args = {
            "uuid_var": user.uuid,
            "username_var": user.username,
            "passwordhash_var": user.password_hash,
            "created_var": user.creation_timestamp,
            "is_authenticated_var": user.is_authenticated,
            "is_active_var": user.is_active
        }
        self.__db.session.execute(text(sql), sql_args)
        self.__db.session.commit()

    def get_user_by_username(self, username: str):
        sql = "SELECT uuid, username, password_hash, created, is_authenticated, is_active FROM users WHERE username=:username"
        sql_args = {
            "username": username
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        if result is None:
            return None
        return User(result[0], result[1], result[2], result[3], result[4], result[5], False)
        

    def get_usernames(self):
        sql = "SELECT username FROM users"
        result = self.__db.session.execute(text(sql)).fetchall()
        if result is None:
            return None
        return set(result)

    def get_user_by_uuid(self, uuid: str):
        sql = "SELECT uuid, username, password_hash, created, is_authenticated, is_active FROM users WHERE uuid=:uuid"
        sql_args = {
            "uuid": uuid
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        if result is None:
            return None
        return User(result[0], result[1], result[2], result[3], result[4], result[5], False)

    def add_forum(self, forum: Forum):
        sql = "INSERT INTO forums (uuid, url_name, display_name, created) VALUES (:uuid, :url_name, :display_name, :created)"
        sql_args = {
            "uuid": forum.uuid,
            "url_name": forum.url_name,
            "display_name": forum.display_name,
            "created": forum.creation_timestamp
        }
        self.__db.session.execute(text(sql), sql_args)
        self.__db.session.commit()

    def get_forum_by_url_name(self, url_name: str):
        sql = "SELECT uuid, url_name, display_name, created FROM forums WHERE url_name=:url_name"
        sql_args = {
            "url_name": url_name
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        if result is None:
            return None
        return Forum(result[0], result[1], result[2], result[3])

    def get_forum_by_uuid(self, uuid: str):
        sql = "SELECT uuid, url_name, display_name, created FROM forums WHERE uuid=:uuid"
        sql_args = {
            "uuid": uuid
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchone()
        if result is None:
            return None
        return Forum(result[0], result[1], result[2], result[3])

    def get_all_forums(self):
        sql = "SELECT uuid, url_name, display_name, created FROM forums"
        result = self.__db.session.execute(text(sql)).fetchall()
        if result is None:
            return None
        forum_objects: list[Forum] = []
        for r in result:
            forum_objects.append(Forum(r[0], r[1], r[2], r[3]))
        return forum_objects

    def add_thread(self, thread: Thread):
        sql = "INSERT INTO threads (uuid, title, content, poster_uuid, forum_uuid, created) VALUES (:uuid, :title, :content, :poster_uuid, :forum_uuid, :created)"
        sql_args = {
            "uuid": thread.uuid,
            "title": thread.title,
            "content": thread.content,
            "poster_uuid": thread.poster_uuid,
            "forum_uuid": thread.forum_uuid,
            "created": thread.creation_timestamp
        }
        self.__db.session.execute(text(sql), sql_args)
        self.__db.session.commit()

    def get_threads_in_forum(self, forum_uuid: str):
        sql = "SELECT uuid, title, content, poster_uuid, forum_uuid, created FROM threads WHERE forum_uuid=:forum_uuid"
        sql_args = {
            "forum_uuid": forum_uuid
        }
        result = self.__db.session.execute(text(sql), sql_args).fetchall()
        if result is None:
            return None
        thread_objects: list[Thread] = []
        for r in result:
            thread_objects.append(Thread(r[0], r[1], r[2], r[3], r[4], r[5]))
        return thread_objects