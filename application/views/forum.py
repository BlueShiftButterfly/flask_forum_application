from flask.views import View
from flask import render_template, request, abort, url_for
from flask_login import current_user
from application.db import DatabaseBridge
from application.permissions import check_permissions_forum, check_permissions_thread, ContentAction

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
                links = {
                    "edit": url_for("forum.forum_edit_view", forum_name=forum.url_name),
                    "create_thread": url_for("thread.thread_create_view", forum_name=forum.url_name),
                    "delete": url_for("forum.forum_delete_view", forum_name=forum.url_name)
                }
                permissions = {
                    "view": check_permissions_forum(current_user, ContentAction.VIEW, forum),
                    "create_thread": check_permissions_thread(current_user, ContentAction.CREATE),
                    "edit": check_permissions_forum(current_user, ContentAction.EDIT, forum),
                    "delete": check_permissions_forum(current_user, ContentAction.DELETE, forum)
                }
                return render_template(self.template, forum=forum, threads=threads, links=links, permissions=permissions)
        abort(404)
