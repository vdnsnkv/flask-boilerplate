from flask import Flask

from logger import app_logger


def create_app(conf: dict = None) -> Flask:
    app = Flask(__name__)

    if conf:
        app.config.update(conf)

    app.logger = app_logger

    @app.route('/')
    def index():
        return ''

    return app
