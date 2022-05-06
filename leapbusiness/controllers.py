from multiprocessing import context
from flask import request, render_template
from .extensions import *
from services import videogame as Videogame


def index():
    context = {"title": "Home"}
    return render_template("index.html", **context)


def view():

    videogame = Videogame.videogame("GTAV")

    context = {"title": videogame.getVideogame()}
    return render_template("view.html", **context)
