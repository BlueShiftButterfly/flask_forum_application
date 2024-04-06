from flask.views import View
from flask import render_template, request, redirect, url_for, abort
from application.db import DatabaseBridge

class ThreadView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self, forum_name, thread_id):
        if request.method == "GET":
            forum = self.db.get_forum_by_url_name(forum_name)
            thread = self.db.get_thread_by_uuid(thread_id)
            if forum.uuid == thread.forum_uuid:
                return render_template(self.template, forum_name=forum_name, thread=thread)
        abort(404)
