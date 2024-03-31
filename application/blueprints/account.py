import string
import uuid
from flask import Blueprint, render_template, request, redirect, url_for
from application.user_credentials import User, UserCredentialsData
from application.input_validation import PasswordValidationResult, PasswordValidator, UsernameValidationResult, UsernameValidator
from application.cryptography import hash_password, check_password 
from application.db import DatabaseBridge

blueprint = Blueprint("account", __name__, url_prefix="/account")
db = DatabaseBridge()
un_validator = UsernameValidator(3, 32, set(string.ascii_letters+string.digits))
pw_validator = PasswordValidator(5, 64, set(string.ascii_letters+string.digits+string.punctuation))

@blueprint.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = db.get_user(username)
        if user is not None:
            if check_password(password, user.credentials_data.password_hash):
                print(f"User {user.credentials_data.username} authenticated")
                return redirect(url_for("index"))
    return render_template("user_login.html")

@blueprint.route("/signup", methods=("GET", "POST"))
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        un_result = un_validator.validate(username, db.taken_usernames)
        pw_result = pw_validator.validate(password)
        print(un_result, pw_result)
        if(
            un_result == UsernameValidationResult.VALID and
            pw_result == PasswordValidationResult.VALID
        ):
            new_user_credentials = UserCredentialsData(username, hash_password(password))
            new_user = User(uuid.uuid4(), new_user_credentials)
            db.add_user(new_user)
            print("Added user: ", new_user.uuid, new_user.credentials_data.username)
            return redirect(url_for("index"))     

    return render_template("user_signup.html")
