from model import User, Meeting
from db import session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'uri': fields.Url('user', absolute=True),
}

user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str)
user_parser.add_argument('email', type=str)

meeting_fields = {
    'id': fields.Integer,
    'owner': fields.String,
    'recording': fields.String,
    'privacy': fields.String,
    'uri': fields.Url('meeting', absolute=True)
}

meeting_parser = reqparse.RequestParser()
meeting_parser.add_argument('owner', type=str)
meeting_parser.add_argument('recording', type=str)
meeting_parser.add_argument('privacy', type=str)


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

    @marshal_with(user_fields)
    def put(self, id):
        parsed_args = user_parser.parse_args()
        new_user = session.query(User).filter(User.id == id).first()
        new_user.name = parsed_args['name']
        new_user.email = parsed_args['email']
        session.add(new_user)
        session.commit()
        return new_user, 201

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

    @marshal_with(meeting_fields)
    def put(self, id):
        parsed_args = meeting_parser.parse_args()
        new_meeting = session.query(Meeting).filter(Meeting.id == id).first()
        new_meeting.owner = parsed_args['owner']
        new_meeting.recording = parsed_args['recording']
        new_meeting.email = parsed_args['privacy']
        session.add(new_meeting)
        session.commit()
        return new_meeting, 201


class MeetingListResource(Resource):
    @marshal_with(meeting_fields)
    def get(self):
        queried_meeting = session.query(Meeting).all()
        return queried_meeting

    @marshal_with(meeting_fields)
    def post(self):
        parsed_args = meeting_parser.parse_args()
        new_meeting = Meeting(owner=parsed_args['owner'], recording=parsed_args['recording'], privacy=parsed_args['privacy'])
        session.add(new_meeting)
        session.commit()
        return new_meeting, 201



