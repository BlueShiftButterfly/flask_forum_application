from flask.views import View
from flask import render_template, request, redirect, url_for
from application.db import DatabaseBridge

class IndexView(View):
    methods = ["GET", "POST"]
    def __init__(self, template, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self):
        forums = self.db.get_all_forums()
        return render_template(self.template, forums=forums)