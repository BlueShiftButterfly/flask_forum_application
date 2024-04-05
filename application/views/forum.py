from flask.views import View
from flask import render_template, request, redirect, url_for, abort
from application.db import DatabaseBridge

class ForumView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self, forum_name):
        if request.method == "GET":
            forum = self.db.get_forum_by_url_name(forum_name)
            if forum:
                return render_template(self.template, forum_name=forum.display_name)
        abort(404)
