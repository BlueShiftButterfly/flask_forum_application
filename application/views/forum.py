from flask.views import View
from flask import render_template, request, abort
from flask_login import current_user
from application.db import DatabaseBridge
from application.timestamp import get_date_from_timestamp
from application.permissions import check_permissions_forum, ContentAction

class ForumView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self, forum_name):
        if request.method == "GET":
            forum = self.db.get_forum_by_url_name(forum_name)
            if forum and check_permissions_forum(current_user, ContentAction.VIEW, forum):
                threads = self.db.get_thread_viewmodels_in_forum(forum.db_id)
                return render_template(self.template, forum=forum, threads=threads, create_link=f"{forum.url}/create_thread")
        abort(404)
