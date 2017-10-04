from flask_restful import fields, reqparse

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
    'storage_url': fields.String,
    'password': fields.String,
    'uri': fields.Url('recording', absolute=True)
}

recording_parser = reqparse.RequestParser()
recording_parser.add_argument('owner_id', type=str)
recording_parser.add_argument('storage_url', type=str)
recording_parser.add_argument('password', type=str)

permission_fields = {
    'user_id': fields.Integer,
    'recording_id': fields.Integer,
}

permission_parser = reqparse.RequestParser()
permission_parser.add_argument('user_id', type=str)
permission_parser.add_argument('recording_id', type=str)
