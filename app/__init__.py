from flask import Flask

from .log import logger


def create_app(conf: dict = None) -> Flask:
    app = Flask(__name__)

    if conf:
        app.config.update(conf)

    app.logger = logger

    # if ENV == PRODUCTION:
    #     app.logger.setLevel(logging.WARNING)
    # else:
    #     app.logger.setLevel(logging.DEBUG)

    @app.route('/')
    def index():
        return ''

    return app
