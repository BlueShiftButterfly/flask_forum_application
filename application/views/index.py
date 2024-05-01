from flask.views import View
from flask import render_template, url_for
from flask_login import current_user
from application.db import DatabaseBridge
from application.permissions import check_permissions_forum, ContentAction

class IndexView(View):
    methods = ["GET", "POST"]
    def __init__(self, template, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self):
        forums = self.db.get_all_forums()
        return render_template(self.template, forums=forums, can_create_forum=check_permissions_forum(current_user, ContentAction.CREATE), forum_create_link=url_for("forum.forum_create_view"))
    