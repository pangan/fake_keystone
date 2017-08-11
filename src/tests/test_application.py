"""
Test Cases for URL Shortening

Author : Amir Mofakhar <pangan@gmail.com>
"""
from src.app import keystone

from flask_testing import TestCase
from flask import Flask

from src.app import _settings


class WebAppFunctionsTestCase(TestCase):
    """
    Test class for web application test cases.
    """

    def create_app(self):
        #app2 = Flask(__name__)
        test_app = keystone.app
        test_app.config['TESTING'] =  True
        return test_app

    def setUp(self):
        #db.create_all()
        pass

    def tearDown(self):
        #db.session.remove()
        #db.drop_all()
        pass

    def test_get_token_response_is_correct(self):
        """Test response is correct"""
        resp = self.client.get('/v3/auth/tokens')

        self.assert_status(resp, 201)
        self.assertEquals(resp.content_type, 'application/json')

