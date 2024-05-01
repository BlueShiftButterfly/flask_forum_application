from flask import Blueprint
from application.views import forum, forum_create, forum_edit, forum_delete

class ForumBlueprint:
    def __init__(self, db) -> None:
        self.blueprint = Blueprint("forum", __name__)
        self.blueprint.add_url_rule("/forum/<forum_name>", view_func=forum.ForumView.as_view("forum_view", "forum.html", db))
        self.blueprint.add_url_rule("/create_forum", view_func=forum_create.ForumCreateView.as_view("forum_create_view", "forum_create.html", db))
        self.blueprint.add_url_rule("/forum/<forum_name>/edit", view_func=forum_edit.ForumEditView.as_view("forum_edit_view", "forum_edit.html", db))
        self.blueprint.add_url_rule("/forum/<forum_name>/delete", view_func=forum_delete.ForumDeleteView.as_view("forum_delete_view", db))
