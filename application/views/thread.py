from flask.views import View
from flask import render_template, request, abort, url_for, redirect
from flask_login import current_user
from application.db import DatabaseBridge
from application.timestamp import get_date_from_timestamp

class ThreadView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self, forum_name, thread_uuid):
        if request.method == "GET":
            forum = self.db.get_forum_by_url_name(forum_name)
            thread = self.db.get_thread_by_uuid(thread_uuid)
            user = self.db.get_user_by_id(thread.poster_id)
            post_date = str(get_date_from_timestamp(thread.created_at))
            comments = self.db.get_comments_in_thread(thread.db_id)
            comment_objs = [(c.content, self.db.get_user_by_id(c.poster_id).username, str(get_date_from_timestamp(c.creation_timestamp))) for c in comments]
            if forum.uuid == self.db.get_forum_by_id(thread.forum_id).uuid:
                return render_template(self.template, forum=forum, thread=thread, user=user, post_date=post_date, comments=comment_objs)
            abort(404)
        if request.method == "POST":
            if current_user.is_authenticated:
                comment_content = request.form.get("comment_content")
                thread = self.db.get_thread_by_uuid(thread_uuid)
                self.db.create_comment(comment_content, current_user.db_id, thread.db_id, False)
                return redirect(url_for("thread.thread_view", forum_name=forum_name, thread_uuid=thread_uuid))
            else:
                return redirect(url_for("account.login_view"))
