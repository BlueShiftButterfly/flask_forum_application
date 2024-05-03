from flask import Blueprint
from application.views import comment

class CommentBlueprint:
    def __init__(self, db) -> None:
        self.blueprint = Blueprint("comment", __name__)
        self.blueprint.add_url_rule("/forum/<forum_name>/thread/<thread_uuid>/comments/<comment_uuid>", view_func=comment.CommentView.as_view("comment_view", "comment.html", db))
