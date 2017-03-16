"""
Test Cases for URL Shortening

Author : Amir Mofakhar <pangan@gmail.com>
"""

from random import randint

import time

from mock import patch
from flask_testing import TestCase
from testfixtures import TempDirectory
from flask import Flask

from src.app import _settings
from src.app.models import db
from src.app.database_table import ShortURL
from src.app.utils import _generate_random_string, _clean_old_addresses_from_database, get_original_url, \
    _get_a_word_that_is_not_used_already
from src.app import utils


def _get_string(size):
    """This function is used for mocking _get_random_string method"""
    return 'test'

class WebAppFunctionsTestCase(TestCase):
    """
    Test class for web application test cases.
    """


    def create_app(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        app.config['TESTING'] = True
        db.app = app
        db.init_app(app)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_original_url_return_none_if_address_not_exists(self):
        """Test function return none if short address is not in database"""
        _settings.SHORT_ADDRESS_LIFE_TIME_IN_SECOND = 1000
        test_record = ShortURL('aa', 'bb', time.time())
        db.session.add(test_record)
        db.session.commit()
        self.assertIsNone(get_original_url('dd'))

    def test_get_original_url_return_correct_long_address(self):
        """Test function return correct long address"""
        _settings.SHORT_ADDRESS_LIFE_TIME_IN_SECOND = 1000
        test_record = ShortURL('aa', 'bb', time.time())
        db.session.add(test_record)
        db.session.commit()
        self.assertEqual(get_original_url('aa'), 'bb')

    def test_generate_random_string(self):
        """Test _generate_random_string function"""
        test_length = randint(1,10)
        generated_string = _generate_random_string(test_length)
        self.assertEquals(len(generated_string),test_length)

    def test_old_records_are_deleted_from_database(self):
        """Test function deletes old records from database"""
        test_record = ShortURL('aa','bb', 123)
        db.session.add(test_record)
        db.session.commit()
        _settings.SHORT_ADDRESS_LIFE_TIME_IN_SECOND = 1
        _clean_old_addresses_from_database()
        ShortURL.query.filter_by(word='aa').first()
        self.assertFalse(ShortURL.query.filter_by(word='aa').first())

    def test_get_a_word_that_is_not_used_already(self):
        """Test get_a_word_that_is_not_used_already returns correct short address"""
        with patch.object(utils, '_generate_random_string', _get_string):
            self.assertEqual('test', _get_a_word_that_is_not_used_already())

    def test_get_a_word_that_is_not_used_already_returns_none(self):
        """Test get_a_word_that_is_not_used_already returns none if can not find unused address"""
        test_record = ShortURL('test', 'bb', time.time())
        db.session.add(test_record)
        db.session.commit()
        with patch.object(utils, '_generate_random_string', _get_string):
            self.assertIsNone( _get_a_word_that_is_not_used_already())
