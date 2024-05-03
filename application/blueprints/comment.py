from flask import Blueprint
from application.views import comment, comment_delete, comment_edit

class CommentBlueprint:
    def __init__(self, db) -> None:
        self.blueprint = Blueprint("comment", __name__)
        self.blueprint.add_url_rule("/forum/<forum_name>/thread/<thread_uuid>/comments/<comment_uuid>", view_func=comment.CommentView.as_view("comment_view", "comment.html", db))
        self.blueprint.add_url_rule("/forum/<forum_name>/thread/<thread_uuid>/comments/<comment_uuid>/edit", view_func=comment_edit.CommentEditView.as_view("comment_edit_view", "comment_edit.html", db))
        self.blueprint.add_url_rule("/forum/<forum_name>/thread/<thread_uuid>/comments/<comment_uuid>/delete", view_func=comment_delete.CommentDeleteView.as_view("comment_delete_view", db))
