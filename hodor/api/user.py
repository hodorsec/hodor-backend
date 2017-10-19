from hodor.app import api
from flask_restplus import Resource

ns = api.namespace('/users', description='Operations related to blog posts')

@ns.route('/users')
class listusers(Resource):
    def get(self):
        return {'user': 'noob'}


api.add_resource(listusers, '/users')