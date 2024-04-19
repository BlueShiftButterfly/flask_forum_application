from flask import Blueprint
from application.views import forum, forum_create

class ForumBlueprint:
    def __init__(self, db) -> None:
        self.blueprint = Blueprint("forum", __name__)
        self.blueprint.add_url_rule("/forum/<forum_name>", view_func=forum.ForumView.as_view("forum_view", "forum.html", db))
        self.blueprint.add_url_rule("/create_forum", view_func=forum_create.ForumCreateView.as_view("forum_create_view", "forum_create.html", db))
