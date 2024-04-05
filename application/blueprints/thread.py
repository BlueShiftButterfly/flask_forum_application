from flask import Blueprint
from application.views import thread

class ThreadBlueprint:
    def __init__(self, db) -> None:
        self.blueprint = Blueprint("thread", __name__, url_prefix="/thread")
        self.blueprint.add_url_rule("/<thread_id>", view_func=thread.ThreadView.as_view("thread_view", "thread.html", db))
