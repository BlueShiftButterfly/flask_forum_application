import os
import string
from flask import Flask, render_template, session
from flask_talisman import Talisman
from flask_login import LoginManager
from dotenv import load_dotenv, find_dotenv
from application.blueprints.account import AccountBlueprint
from application.blueprints.index import IndexBlueprint
from application.authentication import Authenticator
from application.db import DatabaseBridge
from application.user import UsernameValidator, PasswordValidator

UN_CHARACTERS = set(string.ascii_letters + string.digits)
PW_CHARACTERS = set(string.ascii_letters + string.digits + string.punctuation)

def create_app(test_config=None):
    load_dotenv(find_dotenv())

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    login_manager = LoginManager(app)
    Talisman(app)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY")
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db = DatabaseBridge(app, debug=True)
    auth = Authenticator(
        db,
        UsernameValidator(3,30, UN_CHARACTERS),
        PasswordValidator(7, 50, PW_CHARACTERS)
    )
    app.register_blueprint(IndexBlueprint().blueprint)
    app.register_blueprint(AccountBlueprint(auth).blueprint)
    login_manager.user_loader(db.get_user_by_uuid)

    print("APP BUILT")
    return app
