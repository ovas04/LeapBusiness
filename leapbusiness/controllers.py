from flask import jsonify, render_template
from .extensions import *
from service import main


def index():
    return render_template("index.html")


def view():
    return render_template("view.html")


def full_Update():
    main()
    return jsonify(response='full update')


def update_SteamCharts():
    return jsonify(response='update SteamCharts')


def update_SteamPrice():
    return jsonify(response='update SteamPrice')


def update_GameData():
    return jsonify(response='update Game Data')


def update_Metacritic():
    return jsonify(response='update Metacritic')
