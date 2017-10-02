from parsers import *
from models import User, Meeting, Permission
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


class MeetingResource(Resource):
    @marshal_with(meeting_fields)
    def get(self, id):
        queried_meeting = session.query(Meeting).filter(Meeting.id == id).first()
        if not queried_meeting:
            abort(404, message="Meeting {} doesn't exist".format(id))
        return queried_meeting

    def delete(self, id):
        queried_meeting = session.query(Meeting).filter(Meeting.id == id).first()
        if not queried_meeting:
            abort(404, message="Meeting {} doesn't exist".format(id))
        session.delete(queried_meeting)
        session.commit()
        return {}, 204


class MeetingListResource(Resource):
    @marshal_with(meeting_fields)
    def get(self):
        queried_meeting = session.query(Meeting).all()
        return queried_meeting

    @marshal_with(meeting_fields)
    def post(self):
        parsed_args = meeting_parser.parse_args()
        new_meeting = Meeting(owner_id=parsed_args['owner_id'], recording=parsed_args['recording'], privacy=parsed_args['privacy'])
        session.add(new_meeting)
        session.flush()
        print(new_meeting.id)
        new_permission = Permission(user_id=new_meeting.owner_id, meeting_id=new_meeting.id)
        session.add(new_permission)
        session.commit()

        return new_meeting, 201
