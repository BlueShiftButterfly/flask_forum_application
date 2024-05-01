from flask.views import View
from flask import render_template, request, abort, url_for, redirect
from flask_login import current_user
from application.db import DatabaseBridge
from application.permissions import check_permissions_thread, check_permissions_comment, ContentAction

class ThreadView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self, forum_name, thread_uuid):
        thread = self.db.get_thread_by_uuid(thread_uuid)
        if request.method == "GET" and check_permissions_thread(current_user, ContentAction.VIEW, thread):
            forum = self.db.get_forum_by_url_name(forum_name)
            thread_vm = self.db.get_thread_viewmodel(thread.db_id)
            comments = self.db.get_comment_viewmodels_in_thread(thread.db_id)
            links = {
                "edit": url_for("thread.thread_edit_view", forum_name=forum.url_name, thread_uuid=thread_uuid),
                "delete": url_for("thread.thread_delete_view", forum_name=forum.url_name, thread_uuid=thread_uuid),
                "forum": url_for("forum.forum_view", forum_name=forum_name)
            }
            permissions = {
                "view": check_permissions_thread(current_user, ContentAction.VIEW, thread),
                "create_comment": check_permissions_comment(current_user, ContentAction.CREATE),
                "edit": check_permissions_thread(current_user, ContentAction.EDIT, thread),
                "delete": check_permissions_thread(current_user, ContentAction.DELETE, thread)
            }
            return render_template(self.template, forum=forum, thread=thread_vm, comments=comments, links=links, permissions=permissions)
        if request.method == "POST":
            if current_user.is_authenticated:
                if request.form.get("comment_submit") == "Submit" and check_permissions_comment(current_user, ContentAction.CREATE):
                    comment_content = request.form.get("comment_content")
                    self.db.create_comment(comment_content, current_user.db_id, thread.db_id, False)
                    return redirect(url_for("thread.thread_view", forum_name=forum_name, thread_uuid=thread_uuid))
                if request.form.get("delete_thread") == "Delete Thread" and check_permissions_comment(current_user, ContentAction.DELETE, thread):
                    self.db.remove_thread(thread.uuid)
                    return redirect(url_for("forum.forum_view", forum_name=forum_name))
            else:
                return redirect(url_for("account.login_view"))
        abort(404)
