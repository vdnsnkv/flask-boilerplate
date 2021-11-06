from flask import Flask

from .log import logger


def create_app(conf: dict = None) -> Flask:
    app = Flask(__name__)

    if conf:
        app.config.update(conf)

    app.logger = logger

    @app.route('/')
    def index():
        return ''

    return app
