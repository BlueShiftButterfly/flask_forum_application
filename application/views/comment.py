from flask.views import View
from flask import render_template, request, abort
from application.db import DatabaseBridge
from application.viewmodels.converter import comment_dbmodel_to_viewmodel

class CommentView(View):
    methods = ["GET", "POST"]
    def __init__(self, template: str, db: DatabaseBridge) -> None:
        self.template = template
        self.db = db

    def dispatch_request(self, forum_name, thread_uuid, comment_uuid):
        if request.method == "GET":
            comment = comment_dbmodel_to_viewmodel(self.db.get_comment_by_uuid(comment_uuid))
            return render_template(self.template, comment=comment)
        abort(404)
