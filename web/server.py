import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

app = Flask(__name__)

@app.route('/')
def foo():
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    app.logger.info('Info')
    return "foo"

if __name__ == '__main__':
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    #handler.setLevel(logging.INFO)
    #log = logging.getLogger('werkzeug')
    #log.setLevel(logging.DEBUG)
    
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    #app.logger.addHandler(log)
    app.run()
