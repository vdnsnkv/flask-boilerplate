import logging
from logging import LogRecord

from flask import request, has_request_context
from pythonjsonlogger import jsonlogger

from . import config


class CustomJsonFormatter(jsonlogger.JsonFormatter):

    def format(self, record: LogRecord):
        record.level = record.levelname
        if has_request_context():
            record.path = request.path
        else:
            record.path = None
        return super(CustomJsonFormatter, self).format(record)


json_formatter = CustomJsonFormatter()

handler = logging.StreamHandler()
handler.setFormatter(json_formatter)

logger = logging.getLogger()
logger.addHandler(handler)

wrkzg_logger = logging.getLogger("werkzeug")

if config.DEBUG:
    logger.setLevel(logging.DEBUG)
    wrkzg_logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.WARNING)
    wrkzg_logger.setLevel(logging.WARNING)
