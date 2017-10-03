from db import session
from flask_restful import Resource, abort, marshal_with

from models import User, Recording, Permission
from parsers import user_fields, recording_fields, user_parser, recording_parser, permission_fields


class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, id):
        queried_user = session.query(User).filter(User.id == id).first()
        if not queried_user:
            abort(404, message='User {} does not exist'.format(id))
        return queried_user

    def delete(self, id):
        queried_user = session.query(User).filter(User.id == id).first()
        if not queried_user:
            abort(404, message='User {} does not exist'.format(id))
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
        duplicated_email = session.query(User).filter(User.email == parsed_args['email']).first()
        if duplicated_email:
            abort(404, message='An user with the same email already exists')
        new_user = User(name=parsed_args['name'], email=parsed_args['email'])
        session.add(new_user)
        session.commit()
        return new_user, 201


class RecordingResource(Resource):
    @marshal_with(recording_fields)
    def get(self, id):
        queried_recording = session.query(Recording).filter(Recording.id == id).first()
        if not queried_recording:
            abort(404, message='recording {} does not exist'.format(id))
        return queried_recording

    def delete(self, id):
        queried_recording = session.query(Recording).filter(Recording.id == id).first()
        if not queried_recording:
            abort(404, message='recording {} does not exist'.format(id))
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
        duplicated_recording = session.query(Recording).filter(Recording.storage_url == parsed_args['storage_url']).first()
        if duplicated_recording:
            abort(404, message='A recording with the same url already exists')
        new_recording = Recording(owner_id=parsed_args['owner_id'], storage_url=parsed_args['storage_url'],
                                  password=parsed_args['password'])
        session.add(new_recording)
        session.flush()
        new_permission = Permission(user_id=new_recording.owner_id, recording_id=new_recording.id)
        session.add(new_permission)
        session.commit()
        return new_recording, 201


class PermissionResource(Resource):
    @marshal_with(permission_fields)
    def get(self, user_id, recording_id):
        queried_permission = session.query(Permission).filter(Permission.user_id == user_id).filter(
            Permission.recording_id == recording_id).first()
        if not queried_permission:
            abort(404, message='No access to recording {}'.format(recording_id))
        return queried_permission

    def delete(self, user_id, recording_id):
        queried_user = session.query(User).filter(User.id == user_id).first()
        if not queried_user:
            abort(404, message='User {} does not exist'.format(user_id))
        delete_query = session.query(Permission).filter(Permission.user_id == user_id).filter(
            Permission.recording_id == recording_id).first()
        session.delete(delete_query)
        session.commit()
        return {}, 204

    @marshal_with(permission_fields)
    def put(self, user_id, recording_id):
        queried_user = session.query(User).filter(User.id == user_id).first()
        queried_recording = session.query(Recording).filter(Recording.id == recording_id).first()
        if (not queried_user) or (not queried_recording):
            abort(404, message='User/recording does not exist')
        new_permission = Permission(user_id=user_id, recording_id=recording_id)
        session.add(new_permission)
        session.commit()
        return new_permission, 201


class PermissionListResource(Resource):
    @marshal_with(permission_fields)
    def get(self, user_id):
        queried_permissions = session.query(Permission).filter(Permission.user_id == user_id).all()
        return queried_permissions
