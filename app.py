from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from resources import UserListResource, recordingListResource
from resources import UserResource, recordingResource

api.add_resource(UserListResource, '/users', endpoint='users')
api.add_resource(UserResource, '/users/<string:id>', endpoint='user')

api.add_resource(recordingListResource, '/recordings', endpoint='recordings')
api.add_resource(recordingResource, '/recordings/<string:id>', endpoint='recording')

# api.add_resource(PermissionsListResource, '/users/<string:id>/permissions', endpoint='permissions')


if __name__ == '__main__':
    app.run(debug=True)
