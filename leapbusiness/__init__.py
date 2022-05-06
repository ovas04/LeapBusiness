from flask import Flask, redirect, url_for, render_template
from .extensions import *
from .routes import *


def create_app():
    app = Flask(__name__, instance_relative_config=True,
                template_folder="ui/templates", static_folder="ui/static")

    with app.app_context():

        app.register_blueprint(index_blueprint)
        app.register_blueprint(view_blueprint)

    return app
