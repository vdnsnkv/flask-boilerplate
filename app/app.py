from flask import Flask

import handlers
from logger import app_logger


def configure_handlers(app: Flask) -> None:
    app.add_url_rule('/', view_func=handlers.index)
    return


def create_app(conf: dict = None) -> Flask:
    app = Flask('flask-primer')

    if conf:
        app.config.update(conf)

    app.logger = app_logger

    configure_handlers(app)

    return app
