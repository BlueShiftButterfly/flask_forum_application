from flask.views import View
from flask import render_template, request, abort, url_for
from flask_login import current_user
from application.db import DatabaseBridge
from application.permissions import check_permissions_forum, check_permissions_thread, ContentAction
from application.viewmodels.converter import thread_dbmodels_to_viewmodels

class ForumView(View):
    methods = ["GET"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self, forum_name):
        forum = self.db.get_forum_by_url_name(forum_name)
        if not check_permissions_forum(current_user, ContentAction.VIEW, forum):
            abort(403)
        if request.method == "GET":
            if forum:
                threads = thread_dbmodels_to_viewmodels(self.db.get_threads_in_forum(forum.db_id))
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
