from flask.views import View
from flask import request, abort, redirect
from flask_login import current_user
from application.db import DatabaseBridge
from application.permissions import check_permissions_comment, ContentAction

class CommentDeleteView(View):
    methods = ["POST"]
    def __init__(self, db: DatabaseBridge) -> None:
        self.db = db

    def dispatch_request(self, forum_name, thread_uuid, comment_uuid):
        comment = self.db.get_comment_by_uuid(comment_uuid)
        if not check_permissions_comment(current_user, ContentAction.DELETE, comment):
            abort(403)
        if request.method == "POST":
            self.db.remove_comment(comment_uuid)
            return redirect("thread.thread_view", forum_name=forum_name, thread_uuid=thread_uuid)
        abort(404)
