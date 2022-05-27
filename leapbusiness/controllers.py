from multiprocessing import context
from flask import jsonify, render_template
from .extensions import *
from services import videogame as Videogame
from scraps import Scrap_algorithm as Scrapping


def index():
    context = {"title": "Home"}
    return render_template("index.html", **context)


def view():

    videogame = Videogame.videogame("GTAV")

    context = {"title": videogame.getVideogame()}
    return render_template("view.html", **context)


def start():
    print("Start")
    Scrapping.scrap_metacritic()
    status = "Haciendo el web scrapping"
    return jsonify(status=status)
