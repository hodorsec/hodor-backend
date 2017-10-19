# -*- coding: utf-8 -*-
from hodor import app
from flask import jsonify


@app.route('/')
def start():
    return jsonify({'hello': 'world'})


@app.route('/print', methods=['GET', 'POST'])
def printer():
    form = {'hello': 'user'}
    return form
