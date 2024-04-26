from application.db import DatabaseBridge
from application.permissions import STANDARD

#
# WARNING!!!
# DO NOT USE IN PRODUCTION!
# ONLY FOR LOCAL DEMO ONLY!
# Creates demo content for local testing
#

def create_example_content(db: DatabaseBridge):
    if db.get_user_by_username("example_user") is not None:
        print("Content already exists, exiting...")
        return
    example_user = db.create_user("example_user", "password_hash", STANDARD)
    if example_user is None:
        print("oh no")
        return
    pyforum = db.create_forum("python", "Python", "Forum for Python related discussion", example_user.db_id, False)
    qaforum = db.create_forum("questions", "Questions", "Forum for asking questions", example_user.db_id, False)
    db.create_thread("Is python the best language?","maybe", example_user.db_id, pyforum.db_id)
    db.create_thread("How to exit vim","help", example_user.db_id, qaforum.db_id)
