from flask.views import View
from flask import request, abort, redirect, url_for
from flask_login import current_user, login_required
from application.db import DatabaseBridge
from application.permissions import check_permissions_forum, ContentAction

class ForumDeleteView(View):
    methods = ["GET", "POST"]
    def __init__(self, db: DatabaseBridge) -> None:
        self.db = db

    @login_required
    def dispatch_request(self, forum_name):
        forum = self.db.get_forum_by_url_name(forum_name)
        if request.method == "POST" and check_permissions_forum(current_user, ContentAction.DELETE, forum):
            self.db.remove_forum(forum.uuid)
            return redirect(url_for("index.index_view"))
        abort(404)
