import app
from models import *
import unittest
from flask import json, jsonify
users_url = 'http://localhost:5000/users'
recordings_url = 'http://localhost:5000/recordings'
json_header = {'Content-type': 'application/json'}

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.create_app()
        self.client = self.app.test_client()
        self.db = create_engine(DB_URI)
        Base.metadata.drop_all(self.db)
        Base.metadata.create_all(self.db)

    def tearDown(self):
        pass

    def create_user(self, name='User1', email='dummy@email.com'):
        data = {'name': name, 'email': email}
        return self.client.post(users_url, data=json.dumps(data), headers=json_header)


    def test_create_user(self):
        response =  self.create_user(name='Flavio',email='flaviosilvestre89@gmail.com')
        json_data = json.loads(response.data)
        self.assertEqual(json_data['name'], 'Flavio')
        self.assertEqual(json_data['email'], 'flaviosilvestre89@gmail.com')




if __name__ == '__main__':
    unittest.main()


