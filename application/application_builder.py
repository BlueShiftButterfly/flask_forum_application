import os
import string
from flask import Flask
from flask.cli import AppGroup
from flask_login import LoginManager
from dotenv import load_dotenv, find_dotenv
from application.blueprints.account import AccountBlueprint
from application.blueprints.index import IndexBlueprint
from application.blueprints.forum import ForumBlueprint
from application.blueprints.thread import ThreadBlueprint
from application.authentication import Authenticator
from application.db import DatabaseBridge
from application.authentication import UsernameValidator, PasswordValidator
from application.example_content import create_example_content

UN_CHARACTERS = set(string.ascii_letters + string.digits)
PW_CHARACTERS = set(string.ascii_letters + string.digits + string.punctuation)

def create_app():
    load_dotenv(find_dotenv())

    app = Flask(__name__)
    login_manager = LoginManager(app)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY")
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    db = DatabaseBridge(app, debug=True)
    auth = Authenticator(
        db,
        UsernameValidator(3,30, UN_CHARACTERS),
        PasswordValidator(7, 50, PW_CHARACTERS)
    )
    ib = IndexBlueprint(db)
    ab = AccountBlueprint(auth)
    fb = ForumBlueprint(db)
    tb = ThreadBlueprint(db)

    app.register_blueprint(ib.blueprint)
    app.register_blueprint(ab.blueprint)
    app.register_blueprint(fb.blueprint)
    app.register_blueprint(tb.blueprint)

    login_manager.user_loader(db.get_user_by_uuid)
    login_manager.login_view = "account.login_view"
    
    user_cli = AppGroup('demo')

    @user_cli.command('create')
    def create_demo():
        create_example_content(db, auth)

    app.cli.add_command(user_cli)

    return app
