import uuid
from application.authentication import Authenticator
from application.db import DatabaseBridge
from application.thread import create_thread, Thread
from application.forum import create_forum, Forum
from application.user import User

#
# WARNING!!!
# DO NOT USE IN PRODUCTION!
# ONLY FOR LOCAL DEMO ONLY!
# Creates demo content for local testing

def create_example_content(db: DatabaseBridge):
    db.add_user(User("placeholder_uuid", "example_user", "password_hash", 0, True, True, False))
    pyforum: Forum = create_forum("python", "Python")
    qaforum: Forum = create_forum("questions", "Questions")
    db.add_forum(pyforum)
    db.add_forum(qaforum)
    db.add_thread(create_thread("Is python the best language?","maybe", 1, 1))
    db.add_thread(create_thread("How to exit vim","help", 1, 2))