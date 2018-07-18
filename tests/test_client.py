import unittest
from flask import url_for
from app import create_app, db

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app.test_request_context().push()
        db.create_all()
        # test_client provide related context for testing
        self.client = self.app.test_client(use_cookies=True)
        self.app.config['SERVER_NAME'] = '127.0.0.1:5555'
        
    def tearDown(self):
        db.drop_all()
        db.session.remove()
        self.app_context.pop()
        #self.app.test_request_context().pop()


    def test_home_page(self):
        response = self.client.get(url_for('main.index'))
        self.assertTrue('Stranger' in response.get_data(as_text=True))