import os
import string
import click
from flask import Flask
from flask.cli import AppGroup
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from dotenv import load_dotenv, find_dotenv
from application.blueprints.account import AccountBlueprint
from application.blueprints.index import IndexBlueprint
from application.blueprints.forum import ForumBlueprint
from application.blueprints.thread import ThreadBlueprint
from application.blueprints.comment import CommentBlueprint
from application.authentication import Authenticator
from application.db import DatabaseBridge
from application.authentication import UsernameValidator, PasswordValidator
from application.example_content import create_example_content, clear_database, set_admin, remove_admin

UN_CHARACTERS = set(string.ascii_letters + string.digits)
PW_CHARACTERS = set(string.ascii_letters + string.digits + string.punctuation)

def create_app():
    load_dotenv(find_dotenv())

    app = Flask(__name__)

    login_manager = LoginManager(app)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["WTF_CSRF_SECRET_KEY"] = os.environ.get("WTF_CSRF_SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    csrf = CSRFProtect(app)

    db = DatabaseBridge(app)
    auth = Authenticator(
        db,
        UsernameValidator(3,30, UN_CHARACTERS),
        PasswordValidator(7, 50, PW_CHARACTERS)
    )
    ib = IndexBlueprint(db)
    ab = AccountBlueprint(auth)
    fb = ForumBlueprint(db)
    tb = ThreadBlueprint(db)
    cb = CommentBlueprint(db)

    app.register_blueprint(ib.blueprint)
    app.register_blueprint(ab.blueprint)
    app.register_blueprint(fb.blueprint)
    app.register_blueprint(tb.blueprint)
    app.register_blueprint(cb.blueprint)

    login_manager.user_loader(db.get_user_by_uuid)
    login_manager.login_view = "account.login_view"
    login_manager.anonymous_user = auth.get_anonymous_user
    
    user_cli = AppGroup('user')
    database_cli = AppGroup('database')

    @user_cli.command('create-demo')
    def create_demo():
        create_example_content(db)

    @user_cli.command('give-admin')
    @click.argument("username")
    def give_admin(username):
        set_admin(username, db)

    @user_cli.command('remove-admin')
    @click.argument("username")
    def revoke_admin(username):
        remove_admin(username, db)

    @database_cli.command('wipe')
    def wipe_content():
        clear_database(db)

    app.cli.add_command(user_cli)
    app.cli.add_command(database_cli)

    return app
