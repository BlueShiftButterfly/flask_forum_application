from flask.views import View
from flask import render_template, request, abort, url_for
from application.db import DatabaseBridge
from application.timestamp import get_date_from_timestamp

class CommentView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self):
        abort(404)