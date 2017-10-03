from flask import Flask
from flask_restful import Api
from resources import UserListResource, RecordingListResource
from resources import UserResource, RecordingResource, PermissionResource


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(UserListResource, '/users', endpoint='users')
    api.add_resource(UserResource, '/users/<string:id>', endpoint='user')

    api.add_resource(RecordingListResource, '/recordings', endpoint='recordings')
    api.add_resource(RecordingResource, '/recordings/<string:id>', endpoint='recording')

    #api.add_resource(MembershipListResource, '/users/<string:id>/memberships/', endpoint='memberships')
    api.add_resource(PermissionResource, '/users/<string:user_id>/permissions/<string:id>', endpoint='permission')
    return app
# api.add_resource(PermissionsListResource, '/users/<string:id>/permissions', endpoint='permissions')

if __name__ == '__main__':
    create_app().run(debug=True)
