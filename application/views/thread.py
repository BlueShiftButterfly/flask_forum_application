from flask.views import View
from flask import render_template, request, abort, url_for, redirect
from flask_login import current_user
from application.db import DatabaseBridge
from application.permissions import check_permissions_thread, check_permissions_comment, ContentAction
from application.viewmodels.converter import comments_to_viewmodels, thread_to_viewmodel

class ThreadView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self, forum_name, thread_uuid):
        thread = self.db.get_thread_by_uuid(thread_uuid)
        if not check_permissions_thread(current_user, ContentAction.VIEW, thread):
            abort(403)
        if request.method == "GET":
            forum = self.db.get_forum_by_url_name(forum_name)
            thread_vm = thread_to_viewmodel(thread)
            comments = comments_to_viewmodels(self.db.get_comments_in_thread(thread.db_id))
            return render_template(self.template, forum=forum, thread=thread_vm, comments=comments)
        if request.method == "POST":
            if request.form.get("comment_submit") == "Submit" and check_permissions_comment(current_user, ContentAction.CREATE):
                comment_content = request.form.get("comment_content")
                self.db.create_comment(comment_content, current_user.db_id, thread.db_id, False)
                return redirect(url_for("thread.thread_view", forum_name=forum_name, thread_uuid=thread_uuid))
            else:
                abort(403)
        abort(404)
