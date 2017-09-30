from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from resources import UserListResource
from resources import UserResource

api.add_resource(UserListResource, '/users', endpoint='users')
api.add_resource(UserResource, '/users/<string:id>', endpoint='user')

if __name__ == '__main__':
    app.run(debug=True)