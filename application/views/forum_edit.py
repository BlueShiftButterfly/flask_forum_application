from flask.views import View
from flask import render_template, request, abort, redirect, url_for
from flask_login import current_user, login_required
from application.db import DatabaseBridge
from application.permissions import check_permissions_forum, ContentAction

class ForumEditView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    @login_required
    def dispatch_request(self, forum_name):
        forum = self.db.get_forum_by_url_name(forum_name)
        if request.method == "GET" and check_permissions_forum(current_user, ContentAction.EDIT, forum):
            invite_list = "\n".join(list(forum.invited_users))
            return render_template(self.template, forum=forum, cancel_link=url_for("forum.forum_view", forum_name=forum_name), invite_list=invite_list)
        if request.method == "POST" and check_permissions_forum(current_user, ContentAction.EDIT, forum):
            display_name = request.form.get("forum_name")
            url_name = request.form.get("forum_url_name")
            description = request.form.get("forum_description")
            is_invite_only = request.form.get("is_invite_only")
            user_list = set([u.strip() for u in request.form.get("forum_invite_list").strip().split("\n")])
            if (
                forum.display_name != display_name or
                forum.url_name != url_name or
                forum.forum_description != description or
                forum.is_invite_only != is_invite_only 
            ):
                self.db.edit_forum(forum.db_id, url_name, display_name, description, bool(is_invite_only))
                print(user_list)
                for u in user_list:
                    self.db.set_user_forum_access(self.db.get_user_by_username(u).db_id, forum.db_id, True)
                return redirect(url_for("forum.forum_view", forum_name=url_name))
            return redirect(url_for("forum.forum_view", forum_name=forum_name))
        abort(404)
