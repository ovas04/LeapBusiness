from flask import jsonify, render_template
from .extensions import *
from service import main, update_modular


def index():
    return render_template("index.html")


def view():
    return render_template("view.html")


def full_Update():
    main()
    return jsonify(response='full update')


def update_GameData():
    update_modular(1)
    return jsonify(response='update Game Data')


def update_Metacritic():
    update_modular(2)
    return jsonify(response='update Metacritic')


def update_SteamPrice():
    update_modular(3)
    return jsonify(response='update SteamPrice')


def update_SteamCharts():
    update_modular(4)
    return jsonify(response='update SteamCharts')
