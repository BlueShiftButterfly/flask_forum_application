from flask import Blueprint
from application.views import account

class AccountBlueprint:
    def __init__(self, authenticator) -> None:
        self.blueprint = Blueprint("account", __name__, url_prefix="/account")
        self.blueprint.add_url_rule("/login", view_func=account.LoginView.as_view("login_view", "user_login.html", authenticator))
        self.blueprint.add_url_rule("/signup", view_func=account.SignupView.as_view("signup_view", "user_signup.html", authenticator))
        self.blueprint.add_url_rule("/logout", view_func=account.LogoutView.as_view("logout_view", authenticator))
