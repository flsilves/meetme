import app
from models import *
import unittest
import json

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

    def test_create_user(self):
        data = {'name': 'Flavio', 'email': 'flaviosilvestre89@gmail.com'}
        response = self.client.post(users_url, data=json.dumps(data), headers=json_header)
        response = json.loads((response.data).decode('utf-8'))
        self.assertEqual(response['name'],'Flavio')
        self.assertEqual(response['email'],'flaviosilvestre89@gmail.com')

    def test_get_users(self):
        response = self.client.get(users_url)
        #payload = (response.data).decode('utf-8')
        #print('Status Code = {}'.format(response.status_code))
        #self.assertEqual(payload, '[]\n')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()


