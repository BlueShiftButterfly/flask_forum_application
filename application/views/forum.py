from flask.views import View
from flask import render_template, request, abort, url_for
from flask_login import current_user
from application.db import DatabaseBridge
from application.permissions import check_permissions_forum, ContentAction
from application.viewmodels.converter import threads_to_viewmodels, forum_to_viewmodel

class ForumView(View):
    methods = ["GET"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self, forum_name):
        forum = self.db.get_forum_by_url_name(forum_name)
        if not check_permissions_forum(current_user, ContentAction.VIEW, forum):
            abort(403)
        if forum is None:
            abort(404)
        if request.method == "GET":
            threads = threads_to_viewmodels(self.db.get_threads_in_forum(forum.db_id))
            forum_vm = forum_to_viewmodel(forum)
            return render_template(self.template, forum=forum_vm, threads=threads)
        abort(404)
