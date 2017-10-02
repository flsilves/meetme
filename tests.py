import app
from models import *
import unittest, requests

class BasicTestCase(unittest.TestCase):
        def setUp(self):
            self.app = app.create_app()
            self.client = self.app.test_client()
            self.db = create_engine(DB_URI)

        def tearDown(self):
            pass

        def test_create_user(self):
            response = self.client.get('http://localhost:5000/users')
            print((response.data).decode('utf-8'))
            print("Status Code = {}".format(response.status_code))
            #self.assertEqual(response.json(), { '': ''})


if __name__ == '__main__':
    unittest.main()
