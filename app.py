from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from resources import UserListResource, MeetingListResource
from resources import UserResource, MeetingResource

api.add_resource(UserListResource, '/users', endpoint='users')
api.add_resource(UserResource, '/users/<string:id>', endpoint='user')

api.add_resource(MeetingListResource, '/meetings', endpoint='meetings')
api.add_resource(MeetingResource, '/meetings/<string:id>', endpoint='meeting')

# api.add_resource(PermissionsListResource, '/users/<string:id>/permissions', endpoint='permissions')


if __name__ == '__main__':
    app.run(debug=True)
