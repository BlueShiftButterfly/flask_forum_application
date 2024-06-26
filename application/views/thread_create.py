from flask.views import View
from flask import render_template, request, abort, redirect, url_for
from flask_login import login_required, current_user
from application.db import DatabaseBridge
from application.permissions import check_permissions_thread, ContentAction
from application.viewmodels.converter import forum_to_viewmodel

class ThreadCreateView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    @login_required
    def dispatch_request(self, forum_name):
        if not check_permissions_thread(current_user, ContentAction.CREATE):
            abort(403)
        forum = self.db.get_forum_by_url_name(forum_name)
        if request.method == "GET":
            forum_vm = forum_to_viewmodel(forum)
            return render_template(self.template, forum=forum_vm)
        if request.method == "POST":
            title = request.form.get("thread_title")
            content = request.form.get("thread_content")
            if title == "" or content == "":
                return redirect(url_for("thread.thread_create_view", forum_name=forum_name))
            new_thread = self.db.create_thread(title, content, current_user.db_id, forum.db_id)
            return redirect(url_for("thread.thread_view", forum_name=forum_name, thread_uuid=new_thread.uuid))
        abort(404)
