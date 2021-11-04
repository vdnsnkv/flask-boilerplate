from flask import Flask


def create_app(conf: dict = None) -> Flask:
    app = Flask(__name__)

    if conf:
        app.config.update(conf)

    @app.route('/')
    def index():
        return ''

    return app
