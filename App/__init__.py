from App.views import blue
from flask import Flask


def create_app():
    app = Flask(__name__)

    app.register_blueprint(blueprint=blue)

    return app
