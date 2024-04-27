from flask.views import View
from flask import render_template, request, abort, redirect
from flask_login import current_user, login_required
from application.db import DatabaseBridge
from application.timestamp import get_date_from_timestamp
from application.permissions import check_permissions_forum, ContentAction

class ForumCreateView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    @login_required
    def dispatch_request(self):
        if request.method == "GET" and check_permissions_forum(current_user, ContentAction.CREATE):
            return render_template(self.template)
        if request.method == "POST" and check_permissions_forum(current_user, ContentAction.CREATE):
            forum_url_name = request.form.get("forum_url_name")
            forum_name = request.form.get("forum_name")
            forum_description = request.form.get("forum_description")
            self.db.create_forum(forum_url_name, forum_name, forum_description, current_user.db_id, False)
            return redirect(f"/forum/{forum_url_name}")
        abort(404)
