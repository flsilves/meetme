from flask import Flask
from flask_restful import Api
from resources import UserListResource, RecordingListResource, PermissionListResource
from resources import UserResource, RecordingResource, PermissionResource


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(UserListResource, '/users', endpoint='users')
    api.add_resource(UserResource, '/users/<string:id>', endpoint='user')

    api.add_resource(RecordingListResource, '/recordings', endpoint='recordings')
    api.add_resource(RecordingResource, '/recordings/<string:id>', endpoint='recording')

    api.add_resource(PermissionResource, '/users/<string:user_id>/permissions/<string:recording_id>',
                     endpoint='permission')
    api.add_resource(PermissionListResource, '/users/<string:user_id>/permissions', endpoint='permissions')

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
