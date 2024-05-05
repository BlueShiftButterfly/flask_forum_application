from flask.views import View
from flask import render_template, request, abort, redirect, url_for
from flask_login import login_required, current_user
from application.db import DatabaseBridge
from application.permissions import check_permissions_thread, ContentAction
from application.viewmodels.converter import thread_to_viewmodel, forum_to_viewmodel

class ThreadEditView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    @login_required
    def dispatch_request(self, forum_name, thread_uuid):
        thread = self.db.get_thread_by_uuid(thread_uuid)
        forum = thread.forum
        if not check_permissions_thread(current_user, ContentAction.EDIT, thread=thread):
            abort(403)
        if request.method == "GET":
            forum_vm = forum_to_viewmodel(forum)
            thread_vm = thread_to_viewmodel(thread)
            return render_template(
                self.template,
                forum=forum_vm,
                thread=thread_vm
            )
        if request.method == "POST":
            title = request.form.get("thread_title")
            content = request.form.get("thread_content")
            self.db.update_thread(thread.db_id, title, content)
            return redirect(url_for("thread.thread_view", forum_name=forum_name, thread_uuid=thread_uuid))
        abort(404)
