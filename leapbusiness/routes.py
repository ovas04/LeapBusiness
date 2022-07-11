from flask import Blueprint
from . import controllers

index_blueprint = Blueprint("index", "index", url_prefix="/")
index_blueprint.add_url_rule("", "", controllers.index)

view_blueprint = Blueprint("view", "view", url_prefix="/view")
view_blueprint.add_url_rule("", "", controllers.view)

api_blueprint = Blueprint("api", "api", url_prefix="/api")
api_blueprint.add_url_rule(
    "/full-update",
    "full Update",
    controllers.full_Update)
api_blueprint.add_url_rule(
    "/game-data",
    "Game Data",
    controllers.update_GameData)
api_blueprint.add_url_rule(
    "/metacritic",
    "Metacritic",
    controllers.update_Metacritic)
api_blueprint.add_url_rule(
    "/steamprice",
    "SteamPrice",
    controllers.update_SteamPrice)
api_blueprint.add_url_rule(
    "/steamcharts",
    "SteamCharts",
    controllers.update_SteamCharts)
