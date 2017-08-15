"""
Test Cases for URL Shortening

Author : Amir Mofakhar <pangan@gmail.com>
"""
from src.app import keystone

from flask_testing import TestCase
from src.app.v3 import _get_timestamp
from mock import Mock, patch
from datetime import datetime
import time

mock_time = Mock()
mock_time.return_value = time.mktime(datetime(2022, 2, 14, 10, 12).timetuple())

class WebAppFunctionsTestCase(TestCase):
    """
    Test class for web application test cases.
    """

    def create_app(self):

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


    def test_get_time_stamp(self):
        with patch('time.time') as mock_time:
            a = datetime.now()
            b = time.time()
            self.assertEqual(_get_timestamp(), '2016-02-14T10:11:12.000000Z')
