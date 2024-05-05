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
    python_fan_user = db.create_user("pythonfan13", "password_hash", STANDARD)
    cpp_fan_user = db.create_user("cplusplusenthusiast", "password_hash", STANDARD)
    if example_user is None:
        print("Failed to create demo content!")
        return
    pyforum = db.create_forum("python", "Python", "Forum for Python related discussion", example_user.db_id, False)
    qaforum = db.create_forum("questions", "Questions", "Forum for asking questions", example_user.db_id, False)
    pt = db.create_thread("Is python the best language?","It is a great language in my opinion. What are your thoughts?", example_user.db_id, pyforum.db_id)
    pt2 = db.create_thread("How to use print?","How do I print text?", example_user.db_id, pyforum.db_id)
    db.create_comment("I don't like dynamically typed languages.", cpp_fan_user.db_id, pt.db_id, False)
    db.create_comment("I really like python.", python_fan_user.db_id, pt.db_id, False)
    db.create_comment("Just do print(\"text\")", python_fan_user.db_id, pt2.db_id, False)
    qt = db.create_thread("Which code editors are good","Which one should I use?", example_user.db_id, qaforum.db_id)
    db.create_comment("I like using vim. Very efficient and powerful.", cpp_fan_user.db_id, qt.db_id, False)
    db.create_comment("VSCode is pretty easy to use and setup.", python_fan_user.db_id, qt.db_id, False)
    print("Created demo content succesfully")

def clear_database(db: DatabaseBridge):
    print("Truncating database...")
    db.wipe_database()
    print("Done")

def set_admin(username: str, db: DatabaseBridge):
    user = db.get_user_by_username(username)
    db.set_user_role(user.db_id, 0)
    print(f"{user.username} is now an administrator")

def remove_admin(username: str, db: DatabaseBridge):
    user = db.get_user_by_username(username)
    db.set_user_role(user.db_id, 1)
    print(f"{user.username} is no longer an administrator")
