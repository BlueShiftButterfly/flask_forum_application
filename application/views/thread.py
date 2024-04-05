from flask.views import View
from flask import render_template, request, redirect, url_for, abort
from application.db import DatabaseBridge

class ThreadView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self):
        abort(404)
