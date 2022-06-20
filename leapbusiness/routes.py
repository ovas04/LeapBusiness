import imp
from flask import Blueprint
from . import controllers

index_blueprint = Blueprint("index", "index", url_prefix="/")
index_blueprint.add_url_rule("", "", controllers.index)

view_blueprint = Blueprint("view", "view", url_prefix="/view")
view_blueprint.add_url_rule("", "", controllers.view)

start_blueprint = Blueprint("start", "start", url_prefix="/start")
start_blueprint.add_url_rule("", "", controllers.start)
