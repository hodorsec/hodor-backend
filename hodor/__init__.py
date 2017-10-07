# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

ENV = 'development'

app = Flask('hodor')
app.config['SECRET_KEY'] = 'CHANGE_ME_IN_PRODUCTION'

from hodor.controllers import *

if ENV == 'development':
    app.debug = True
    toolbar = DebugToolbarExtension(app)
else:
    app.debug = False
    if app.config['SECRET_KEY'] == 'CHANGE_ME_IN_PRODUCTION':
        print("[!] Please change your secret key before running in production");
