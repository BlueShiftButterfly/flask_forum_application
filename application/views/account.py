from flask.views import View
from flask_login import login_required
from flask import render_template, request, redirect, url_for
from application.authentication import Authenticator

class LoginView(View):
    methods = ["GET", "POST"]
    def __init__(self, template, authenticator: Authenticator) -> None:
        self.template = template
        self.authenticator = authenticator

    def dispatch_request(self):
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            if self.authenticator.login(username, password):
                return redirect(url_for("index.index_view"))
        return render_template(self.template)

class SignupView(View):
    methods = ["GET", "POST"]
    def __init__(self, template, authenticator: Authenticator) -> None:
        self.template = template
        self.authenticator = authenticator

    def dispatch_request(self):        
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            if self.authenticator.signup(username, password):
                return redirect(url_for("index.index_view"))
        return render_template(self.template)

class LogoutView(View):
    methods = ["GET", "POST"]
    def __init__(self, authenticator: Authenticator) -> None:
        self.authenticator = authenticator

    @login_required
    def dispatch_request(self):
        self.authenticator.logout()
        return redirect(url_for("index.index_view"))
