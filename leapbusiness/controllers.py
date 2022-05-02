from multiprocessing import context
from flask import request, render_template

def index():
    context = {"title": "Home"}
    return render_template("index.html", **context)

def view():
    context = {"title": "View"}
    return render_template("view.html", **context)