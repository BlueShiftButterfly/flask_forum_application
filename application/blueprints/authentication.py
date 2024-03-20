from flask import Blueprint, render_template

blueprint = Blueprint("authentication", __name__, url_prefix="/auth")

@blueprint.route("/login")
def login():
    return render_template("user_login.html")
