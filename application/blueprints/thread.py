from flask import Blueprint
from application.views import thread, thread_create, thread_delete, thread_edit

class ThreadBlueprint:
    def __init__(self, db) -> None:
        self.blueprint = Blueprint("thread", __name__)
        self.blueprint.add_url_rule("/forum/<forum_name>/thread/<thread_uuid>", view_func=thread.ThreadView.as_view("thread_view", "thread.html", db))
        self.blueprint.add_url_rule("/forum/<forum_name>/create_thread", view_func=thread_create.ThreadCreateView.as_view("thread_create_view", "thread_create.html", db))
        self.blueprint.add_url_rule("/forum/<forum_name>/thread/<thread_uuid>/edit", view_func=thread_edit.ThreadEditView.as_view("thread_edit_view", "thread_edit.html", db))
        self.blueprint.add_url_rule("/forum/<forum_name>/thread/<thread_uuid>/delete", view_func=thread_delete.ThreadDeleteView.as_view("thread_delete_view", db))
