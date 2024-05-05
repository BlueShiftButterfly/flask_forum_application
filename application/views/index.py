from flask.views import View
from flask import render_template, url_for, request, abort
from flask_login import current_user
from application.db import DatabaseBridge
from application.permissions import check_permissions_forum, ContentAction
from application.viewmodels.converter import forums_to_viewmodels

class IndexView(View):
    methods = ["GET"]
    def __init__(self, template, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self):
        if request.method == "GET":
            forums = self.db.get_all_forums()
            viewable_forums = [
                forum
                for forum in forums
                if (
                    forum.is_invite_only == False or 
                    (forum.is_invite_only and current_user.username in forum.invited_users)
                )
            ]
            viewable_forums = forums_to_viewmodels(viewable_forums)
            forum_permission = check_permissions_forum(current_user, ContentAction.CREATE)
            return render_template(
                self.template,
                forums=viewable_forums,
                can_create_forum=forum_permission,
                forum_create_link=url_for("forum.forum_create_view")
            )
        abort(404)
