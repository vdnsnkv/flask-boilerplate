import os


FLASK_DEBUG = bool(eval(os.getenv('FLASK_DEBUG', '0')))
DEBUG = bool(eval(os.getenv('DEBUG', '0')))

DEBUG = DEBUG or FLASK_DEBUG
