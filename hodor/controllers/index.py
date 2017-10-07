# -*- coding: utf-8 -*-
from hodor import app
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CreateForm(FlaskForm):
    text = StringField('name', validators=[DataRequired()])


@app.route('/')
def start():
    pass

@app.route('/app')
def application():
    pass
