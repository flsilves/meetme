from flask_restful import Resource
from flask_restful import abort
from flask_restful import marshal_with

from db import session
from models import User, Recording, Permission
from parsers import *

# TODO http://127.0.0.1:5000/users/1/permissions/3 -> should return false or true
# TODO http://127.0.0.1:5000/users/1/permissions -> list with object permissions
class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, id):
        queried_user = session.query(User).filter(User.id == id).first()
        permission = session.query(User) # join get list of permissions
        if not queried_user:
            abort(404, message="User {} doesn't exist".format(id))
        return [queried_user, queried_user]

    def delete(self, id):
        queried_user = session.query(User).filter(User.id == id).first()
        if not queried_user:
            abort(404, message="User {} doesn't exist".format(id))
        session.delete(queried_user)
        session.commit()
        return {}, 204


class UserListResource(Resource):
    @marshal_with(user_fields)
    def get(self):
        queried_user = session.query(User).all()
        return queried_user

    @marshal_with(user_fields)
    def post(self):
        parsed_args = user_parser.parse_args()
        new_user = User(name=parsed_args['name'], email=parsed_args['email'])
        session.add(new_user)
        try:
            session.commit()
        except:
            session.rollback()
            print("Error: email: \"{}\" already registered".format(new_user.email))
            abort(404, message="Error: email: \"{}\" already registered".format(new_user.email))
        return new_user, 201


class RecordingResource(Resource):
    @marshal_with(recording_fields)
    def get(self, id):
        queried_recording = session.query(Recording).filter(Recording.id == id).first()
        if not queried_recording:
            abort(404, message="recording {} doesn't exist".format(id))
        return queried_recording

    def delete(self, id):
        queried_recording = session.query(Recording).filter(Recording.id == id).first()
        if not queried_recording:
            abort(404, message="recording {} doesn't exist".format(id))
        session.delete(queried_recording)
        session.commit()
        return {}, 204


class RecordingListResource(Resource):
    @marshal_with(recording_fields)
    def get(self):
        queried_recording = session.query(Recording).all()
        return queried_recording

    @marshal_with(recording_fields)
    def post(self):
        parsed_args = recording_parser.parse_args()
        new_recording = Recording(owner_id=parsed_args['owner_id'], storage_url=parsed_args['storage_url'],
                                  privacy=parsed_args['privacy'])
        new_recording2 = Recording(owner_id=parsed_args['owner_id'], storage_url='cenas',
                                  privacy=parsed_args['privacy'])
        session.add(new_recording)

        session.flush()
        session.add(new_recording2)
        session.flush()
        print(new_recording.id)
        new_permission = Permission(user_id=new_recording.owner_id, recording_id=new_recording.id)
        new_permission3 = Permission(user_id=new_recording.owner_id, recording_id=new_recording2.id)
        new_permission2 = Permission(user_id=2, recording_id=new_recording.id)
        session.add(new_permission)
        session.add(new_permission2)
        session.add(new_permission3)
        session.commit()

        return new_recording, 201


class PermissionResource(Resource):
    @marshal_with(permission_fields) ## falta o marshal
    def get(self, user_id, id):
        queried_permission = session.query(Permission).filter(Permission.user_id == user_id).all()
        print(repr(queried_permission))
        if not queried_permission:
            abort(404, message="recording {} doesn't exist".format(id))
        return queried_permission




    # class MembershipListResource(Resource):
#     @marshal_with(membership_fields)
#     def get(self):
#         queried_recording = session.query(Recording).all()
#         return queried_recording
#
#     @marshal_with(recording_fields)
#     def post(self):
#         parsed_args = recording_parser.parse_args()
#         new_recording = Recording(owner_id=parsed_args['owner_id'], storage_url=parsed_args['storage_url'],
#                                   privacy=parsed_args['privacy'])
#         session.add(new_recording)
#         session.flush()
#         print(new_recording.id)
#         new_permission = Permission(user_id=new_recording.owner_id, recording_id=new_recording.id)
#         session.add(new_permission)
#         session.commit()
#
#         return new_recording, 201
