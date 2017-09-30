from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import Table, ForeignKey, MetaData, Column, String, Integer, create_engine
from json import dumps
import os

app = Flask(__name__)
api = Api(app)

current_dir = os.path.dirname(os.path.abspath(__file__))
db = create_engine('sqlite:///' + current_dir + '/main.db')

metadata = MetaData()

users = Table('users', metadata,
    Column('user_id', Integer, primary_key=True,  autoincrement=True),
    Column('user_name', String(16), nullable=False),
    Column('email_address', String(60), key='email'),
)

meetings = Table('meetings', metadata,
    Column('meeting_id', Integer, primary_key=True, autoincrement=True),
    Column('owner', Integer, ForeignKey("users.user_id"), nullable=False),
    Column('url', String(40), nullable=False),
    Column('privacy', String(100)) ## TODO
)

metadata.create_all(db)


class Users(Resource):
    def get(self):
        conn = db.connect()
        query = conn.execute("select distinct user_name from users")
        return {'users': [i[0] for i in query.cursor.fetchall()]}

class User(Resource):
    def get(self, user_id):
        conn = db.connect()
        query = conn.execute("select * from users where user_id='%d'"%user_id)
        result = {'user': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result



api.add_resource(User, '/user/<int:user_id>')
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(debug=True)