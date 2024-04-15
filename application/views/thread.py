from flask.views import View
from flask import render_template, request, abort
from application.db import DatabaseBridge
from application.timestamp import get_date_from_timestamp

class ThreadView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self, forum_name, thread_id):
        if request.method == "GET":
            forum = self.db.get_forum_by_url_name(forum_name)
            thread = self.db.get_thread_by_uuid(thread_id)
            user = self.db.get_user_by_id(thread.poster_id)
            post_date = str(get_date_from_timestamp(thread.created_at))
            if forum.uuid == self.db.get_forum_by_id(thread.forum_id).uuid:
                return render_template(self.template, forum_name=forum.display_name, thread=thread, user=user, post_date=post_date)
        abort(404)
