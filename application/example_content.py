from application.db import DatabaseBridge

#
# WARNING!!!
# DO NOT USE IN PRODUCTION!
# ONLY FOR LOCAL DEMO ONLY!
# Creates demo content for local testing

def create_example_content(db: DatabaseBridge):
    example_user = db.create_user("example_user", "password_hash")
    pyforum = db.create_forum("python", "Python")
    qaforum = db.create_forum("questions", "Questions")
    db.create_thread("Is python the best language?","maybe", example_user.db_id, pyforum.db_id)
    db.create_thread("How to exit vim","help", example_user.db_id, qaforum.db_id)