from flask import Blueprint, render_template, request, redirect, url_for

blueprint = Blueprint("authentication", __name__, url_prefix="/auth")

@blueprint.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return redirect(url_for("index"))

    return render_template("user_login.html")

@blueprint.route("/signup", methods=("GET", "POST"))
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        return redirect(url_for("index"))

    return render_template("user_signup.html")
