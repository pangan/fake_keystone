"""
utility functions for using in web application

Author : Amir Mofakhar <pangan@gmail.com>
"""
import random
import string
import time

from . import _settings
from .database_table import ShortURL
from .models import db


def get_original_url(short_address):
    original_address = ShortURL.query.filter_by(word=short_address).first()
    if original_address:
        return original_address.url

    return None


def assign_word_to_url(long_url):
    word = _get_a_word_that_is_not_used_already()
    new_short_address = ShortURL(word, long_url, time.time())
    db.session.add(new_short_address)
    db.session.commit()
    return word


def _get_a_word_that_is_not_used_already():
    """
    1. cleans all old records from database.
    2. generate a new short address.
    3. returns the generated short address if it is not used already.
    4. returns None if can not find a free address after many attempts.
    """
    number_of_tries = 0
    while number_of_tries < _settings.MAX_NUMBER_OF_TRIES_TO_FIND_UNASSIGNED_SHORT_ADDRESS:
        _clean_old_addresses_from_database()
        new_word = _generate_random_string(_settings.SHORT_ADDRESS_LENGTH)
        if not ShortURL.query.filter_by(word=new_word).first():
            return new_word
        number_of_tries += 1
    return None


def _clean_old_addresses_from_database():
    ShortURL.query.filter(ShortURL.time_stamp<time.time() - _settings.SHORT_ADDRESS_LIFE_TIME_IN_SECOND).delete()


def _generate_random_string(length):
    return ''.join(random.choice(string.lowercase) for _ in range(length))
