from flask import Blueprint
from application.views import index

class IndexBlueprint:
    def __init__(self, db) -> None:
        self.blueprint = Blueprint("index", __name__, url_prefix="/")
        self.blueprint.add_url_rule("", view_func=index.IndexView.as_view("index_view", "index.html", db))
