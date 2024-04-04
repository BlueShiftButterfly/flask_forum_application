from flask.views import View
from flask import render_template, request, redirect, url_for, session

class IndexView(View):
    methods = ["GET", "POST"]
    def __init__(self, template) -> None:
        self.template = template

    def dispatch_request(self):
        return render_template(self.template, session=session)