import os
from flask import Flask, render_template

from . import config


def create_app(test_config=None):
    """
    this function is an application factory for Flask. it is called automatically to
    create the app when you execute `flask --app {app-name} run`

    https://flask.palletsprojects.com/en/3.0.x/patterns/appfactories/
    """

    app = Flask(__name__, instance_relative_config=True)
    # use the config file when override not provided
    if test_config is None:
        app.config.from_object(config)
    else:
        app.config.from_mapping(test_config)

    from . import database, main

    database.init_app(app)
    app.register_blueprint(main.bp)

    return app
