from flask_restful import fields
from flask_restful import reqparse

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'uri': fields.Url('user', absolute=True),
}

user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str)
user_parser.add_argument('email', type=str)

recording_fields = {
    'id': fields.Integer,
    'owner_id': fields.String,
    'recording': fields.String,
    'privacy': fields.String,
    'uri': fields.Url('recording', absolute=True)
}

recording_parser = reqparse.RequestParser()
recording_parser.add_argument('owner_id', type=str)
recording_parser.add_argument('recording', type=str)
recording_parser.add_argument('privacy', type=str)
