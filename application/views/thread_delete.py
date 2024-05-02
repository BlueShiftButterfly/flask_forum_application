from flask.views import View
from flask import request, abort, redirect, url_for
from flask_login import login_required, current_user
from application.db import DatabaseBridge
from application.permissions import check_permissions_thread, ContentAction

class ThreadDeleteView(View):
    methods = ["POST"]
    def __init__(self, db: DatabaseBridge) -> None:
        self.db = db

    @login_required
    def dispatch_request(self, forum_name, thread_uuid):
        thread = self.db.get_thread_by_uuid(thread_uuid)
        if not check_permissions_thread(current_user, ContentAction.DELETE, thread=thread):
            abort(403)
        if request.method == "POST":
            return redirect(url_for("thread.thread_view", forum_name=forum_name, thread_uuid=thread_uuid))
        abort(404)
