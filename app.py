from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from resources import UserListResource, RecordingListResource
from resources import UserResource, RecordingResource

api.add_resource(UserListResource, '/users', endpoint='users')
api.add_resource(UserResource, '/users/<string:id>', endpoint='user')

api.add_resource(RecordingListResource, '/recordings', endpoint='recordings')
api.add_resource(RecordingResource, '/recordings/<string:id>', endpoint='recording')

# api.add_resource(PermissionsListResource, '/users/<string:id>/permissions', endpoint='permissions')


if __name__ == '__main__':
    app.run(debug=True)
