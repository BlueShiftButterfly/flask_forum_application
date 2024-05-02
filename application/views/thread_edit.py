from flask.views import View
from flask import render_template, request, abort, redirect, url_for
from flask_login import login_required, current_user
from application.db import DatabaseBridge
from application.permissions import check_permissions_thread, ContentAction

class ThreadEditView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    @login_required
    def dispatch_request(self, forum_name, thread_uuid):
        forum = self.db.get_forum_by_url_name(forum_name)
        thread = self.db.get_thread_by_uuid(thread_uuid)
        if not check_permissions_thread(current_user, ContentAction.EDIT, thread=thread):
            abort(403)
        if request.method == "GET":
            return render_template(
                self.template,
                forum=forum,
                thread=thread,
                thread_url=url_for("thread.thread_view", forum_name=forum_name, thread_uuid=thread_uuid)
            )
        if request.method == "POST":
            title = request.form.get("thread_title")
            content = request.form.get("thread_content")
            self.db.update_thread(thread.db_id, title, content)
            return redirect(url_for("thread.thread_view", forum_name=forum_name, thread_uuid=thread_uuid))
        abort(404)
