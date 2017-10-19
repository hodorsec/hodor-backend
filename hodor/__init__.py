# app/__init__.py
import time
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

from hodor.models import *


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    if config_name != 'production':
        for x in range(0,5):
            print "*** YOU ARE NOT RUNNING THE APP IN PRODUCTION MODE!! *** CTRL + C TO ABORT. APP WILL RUN IN {} SECONDS".format(5-x)
            time.sleep(1)

    if config_name == 'production':
        app.config['DEFAULT_RENDERERS'] = [
            'flask.ext.api.renderers.JSONRenderer',
        ]

    return app


app = create_app('testing')

from hodor.controllers import *
