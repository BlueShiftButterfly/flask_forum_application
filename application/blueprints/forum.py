from flask import Blueprint
from application.views import forum

class ForumBlueprint:
    def __init__(self, db) -> None:
        self.blueprint = Blueprint("forum", __name__, url_prefix="/forum")
        self.blueprint.add_url_rule("/<forum_name>", view_func=forum.ForumView.as_view("forum_view", "forum.html", db))
