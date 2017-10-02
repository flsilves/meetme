from parsers import *
from models import User, recording, Permission
from db import session

from flask_restful import abort
from flask_restful import Resource
from flask_restful import marshal_with


class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, id):
        queried_user = session.query(User).filter(User.id == id).first()
        if not queried_user:
            abort(404, message="User {} doesn't exist".format(id))
        return queried_user

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
        queried_recording = session.query(recording).filter(recording.id == id).first()
        if not queried_recording:
            abort(404, message="recording {} doesn't exist".format(id))
        return queried_recording

    def delete(self, id):
        queried_recording = session.query(recording).filter(recording.id == id).first()
        if not queried_recording:
            abort(404, message="recording {} doesn't exist".format(id))
        session.delete(queried_recording)
        session.commit()
        return {}, 204


class RecordingListResource(Resource):
    @marshal_with(recording_fields)
    def get(self):
        queried_recording = session.query(recording).all()
        return queried_recording

    @marshal_with(recording_fields)
    def post(self):
        parsed_args = recording_parser.parse_args()
        new_recording = recording(owner_id=parsed_args['owner_id'], recording=parsed_args['recording'], privacy=parsed_args['privacy'])
        session.add(new_recording)
        session.flush()
        print(new_recording.id)
        new_permission = Permission(user_id=new_recording.owner_id, recording_id=new_recording.id)
        session.add(new_permission)
        session.commit()

        return new_recording, 201
