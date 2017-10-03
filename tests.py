import app
from models import *
import unittest


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
        response = self.client.get('http://localhost:5000/users')
        payload = (response.data).decode('utf-8')
        print('Status Code = {}'.format(response.status_code))
        self.assertEqual(payload, '[]\n')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
