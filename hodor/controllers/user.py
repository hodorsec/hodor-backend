# -*- coding: utf-8 -*-
from hodor import app
from flask import request, jsonify, abort, make_response
from hodor.models.user import User
from sqlalchemy.exc import IntegrityError


# Get all Users
@app.route('/users', methods=['GET', 'POST'])
def get_all_users():
    # TODO: Authentication for calling this API endpoint. Admin only.
    """
    This function iterates the database to find all users and returns as JSON
    :return: Response Code
    """
    response = dict()
    response['status'] = 200
    response['data'] = []

    for user in User.get_all():
        current_user = dict()
        '''
        This can be done by directly dumping the dictionary but there's always
        a risk of data leak.So, we pick what we need to give out out of the API
        '''
        current_user['username'] = user.username
        current_user['first_name'] = user.first_name
        current_user['last_name'] = user.last_name
        current_user['email'] = user.email
        current_user['verified_account'] = user.verified_account
        response['data'].append(current_user)

    return response


# Register a user
@app.route('/users/new', methods=['POST'])
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
            newuser['verification_code'] = str(request.data.get(
                'verification_code').strip())
        except Exception as e:
            print(e)
            abort(500)
        user = User(**newuser)
        user.save()
    return make_response(jsonify(status=201, msg="User {} successfully added" +
                                 "to database".format(user.username)), 201)


#################################################
# Check for an existing user in the database    #
#################################################
@app.route('/users/check', methods=['POST'])
def check_for_existing_user():
    errors = []
    # If the username field is passed, checl the username field.
    if request.data.get('username'):
        check_username = str(request.data.get('username').strip())
        user_checkuser = User.query.filter_by(username=check_username).first()
        if user_checkuser:
            errors.append({
                'field': 'username',
                'error': '{} is taken'.format(check_username)
            })
        del(user_checkuser)

    # If the email field is set, check for duplicate email
    if request.data.get('email'):
        check_email = str(request.data.get('email').strip())
        user_checkmail = User.query.filter_by(email=check_email).first()
        if user_checkmail:
            errors.append({
                'field': 'email',
                'error': '{} exists in the database'.format(check_email)
            })

    if errors:
        return make_response(jsonify(status=400, err=errors), 400)
    else:
        return jsonify(
            status=200,
            msg="ok"
        )


@app.errorhandler(IntegrityError)
def handle_sqlalchemy_assertion_error(err):
    try:
        '''
        err.orig.args is from the DBAPIError class of SQLAlchemy. It usually
        contains the original error message.
        The below is an attempt to clean up the message and only return the
        relevant part to API
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
