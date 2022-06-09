from multiprocessing import context
from sre_constants import SUCCESS
from flask import jsonify, render_template
from .extensions import *
from services import Videogame
from service import main


def index():
    context = {"title": "Home"}
    return render_template("index.html", **context)


def view():

    videogame = Videogame.Videogame("GTAV")

    context = {"title": videogame.getVideogame()}
    return render_template("view.html", **context)


def start():
    print("Start of process")
    success = main()
    status = "Realizando el web scrapping"
    return jsonify(status=status)
