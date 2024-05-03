from flask.views import View
from flask import render_template, request, abort, redirect, url_for
from flask_login import current_user
from application.db import DatabaseBridge
from application.permissions import check_permissions_comment, ContentAction

class CommentEditView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self, forum_name, thread_uuid, comment_uuid):
        comment = self.db.get_comment_by_uuid(comment_uuid)
        thread_url = url_for("thread.thread_view", forum_name=forum_name, thread_uuid=thread_uuid)
        comment_url = url_for("comment.comment_view", forum_name=forum_name, thread_uuid=thread_uuid, comment_uuid=comment_uuid)
        if not check_permissions_comment(current_user, ContentAction.EDIT, comment):
            abort(403)
        if request.method == "GET":
            return render_template(self.template, comment=comment, thread_url=thread_url)
        if request.method == "POST":
            content = request.form.get("comment_content")
            self.db.update_comment(comment.db_id, content)
            return redirect(comment_url)
        abort(404)
