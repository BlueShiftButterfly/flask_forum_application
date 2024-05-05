from flask.views import View
from flask import render_template, request, abort, redirect, url_for
from flask_login import current_user, login_required
from application.db import DatabaseBridge
from application.permissions import check_permissions_forum, ContentAction

class ForumCreateView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    @login_required
    def dispatch_request(self):
        if not check_permissions_forum(current_user, ContentAction.CREATE):
            abort(403)
        if request.method == "GET":
            return render_template(self.template)
        if request.method == "POST":
            forum_url_name = request.form.get("forum_url_name")
            forum_name = request.form.get("forum_name")
            forum_description = request.form.get("forum_description")
            forum_is_invite_only = request.form.get("is_invite_only")
            user_list = set([u.strip() for u in request.form.get("forum_invite_list").strip().split("\n")])
            if(forum_url_name == "" or forum_name == ""):
                return redirect(url_for("forum.forum_create_view"))
            forum = self.db.create_forum(forum_url_name, forum_name, forum_description, current_user.db_id, False)
            for u in user_list:
                self.db.set_user_forum_access(self.db.get_user_by_username(u).db_id, forum.db_id, True)
            return redirect(url_for("forum.forum_view", forum_name=forum_url_name))
        abort(404)
