import unittest

from flask import json

import app
from models import *

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
        response = self.client.post(users_url, data=json.dumps(data), headers=json_header)
        json_data = json.loads(response.data)
        code = response.status_code
        return json_data, code

    def create_recording(self, owner_id, storage_url, password):
        data = {'owner_id': owner_id, 'storage_url': storage_url, 'password': password}
        response = self.client.post(recordings_url, data=json.dumps(data), headers=json_header)
        json_data = json.loads(response.data)
        code = response.status_code
        return json_data, code

    def test_create_user(self):
        data, code = self.create_user(name='Flavio', email='flaviosilvestre89@gmail.com')
        self.assertEqual(code, 201)
        self.assertEqual(data['name'], 'Flavio')
        self.assertEqual(data['email'], 'flaviosilvestre89@gmail.com')

    def test_create_same_email(self):
        data, code= self.create_user(name='Flavio', email='flaviosilvestre89@gmail.com')
        self.assertEqual(code, 201)
        data, code= self.create_user(name='Flavio', email='flaviosilvestre89@gmail.com')
        self.assertEqual(code, 404)

    def test_create_recording(self):
        password='secret'
        url = 'https://s3.amazonaws.com/recording/393217'
        data, code = self.create_user(name='Flavio', email='flaviosilvestre89@gmail.com')
        flavio_id = data['id']
        data, code = self.create_recording(owner_id=flavio_id,storage_url=url,password=password)
        self.assertEqual(code, 201)
        self.assertEqual(data['owner_id'], str(flavio_id))
        self.assertEqual(data['storage_url'], url)
        self.assertEqual(data['password'], password)
        data, code = self.create_user(name='Flavio', email='flaviosilvestre89@gmail.com') ## try to create duplicated recording
        self.assertEqual(code, 404)




if __name__ == '__main__':
    unittest.main()
