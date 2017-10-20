# -*- coding: utf-8 -*-
from hodor import app
from flask import request, jsonify, abort, make_response
from hodor.models.user import User
from sqlalchemy.exc import IntegrityError


# Get all Users
@app.route('/users', methods=['GET', 'POST'])
def get_all_users():
    response = {}
    response['status'] = 200
    response ['data'] = []
    """
    This function iterates the database to find all users and returns it as JSON.
    :return: Response Code
    """

    for ele in User.get_all():
        user = ele.__dict__
        print user
    return 'Work in Progress'


@app.route('/users/new', methods=['GET', 'POST'])
def add_new_user():
    """
    This function adds a new user
    :return: Response Code
    """
    newuser = {}

    if request.method == "POST":
        try:
            newuser['username'] = str(request.data.get('username').strip())
            newuser['first_name'] = str(request.data.get('first_name').strip())
            newuser['last_name'] = str(request.data.get('last_name').strip())
            newuser['email'] = str(request.data.get('email').strip())
            newuser['password'] = str(request.data.get('password').strip())
            newuser['verification_code'] = str(request.data.get('verification_code').strip()) or newuser['verification_code']
        except Exception as e:
            print(e)
            abort(500)
        print newuser
        user = User(**newuser)
        user.save()
    return make_response(jsonify(status=201, msg="User {} successfully added to database".format(user.username)), 201)


@app.errorhandler(IntegrityError)
def handle_sqlalchemy_assertion_error(err):
    try:
        '''
        err.orig.args is from the DBAPIError class of SQLAlchemy. It usually contains the original error message.
        The below is an attempt to clean up the message and only return the relevant part to API
        '''
        errmsg = err.orig.args[0].split('\n')[1][9:]
    except IndexError:
        errmsg = err.orig.args[0].split('\n')
    except IndexError:
        errmsg = err.orig.args[0]
    return make_response(jsonify(status=400, msg=errmsg), 400)


@app.route('/print', methods=['GET', 'POST'])
def printer():
    form = {'hello': 'user'}
    return form
