from flask.views import View
from flask import render_template, request, abort, redirect
from flask_login import login_required, current_user
from application.db import DatabaseBridge
from application.thread import create_thread

class ThreadCreateView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    @login_required
    def dispatch_request(self, forum_name):
        forum = self.db.get_forum_by_url_name(forum_name)
        if request.method == "GET":
            return render_template(self.template, forum_name=forum.display_name, forum_url=f"/forum/{forum_name}")
        if request.method == "POST":
            title = request.form.get("thread_title")
            content = request.form.get("thread_content")
            new_thread = create_thread(title, content, current_user.uuid, forum.uuid)
            self.db.add_thread(new_thread)
            return redirect(f"/forum/{forum_name}/thread/{new_thread.uuid}")
        abort(404)
