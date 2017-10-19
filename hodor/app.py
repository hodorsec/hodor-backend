from flask import Flask, request
from flask_restplus import Resource, Api
from api.user import ns as user_namespace

app = Flask(__name__)
api = Api(app)

todos = {}

@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_namespace(user_namespace)
if __name__ == '__main__':
    app.run(debug=True)