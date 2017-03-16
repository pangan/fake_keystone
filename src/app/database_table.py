"""
Table of database used for URL Shortening

Author : Amir Mofakhar <pangan@gmail.com>
"""
from src.app import _settings
from src.app.models import db


class ShortURL(db.Model):

    __tablename__ = 'short_url'
    word = db.Column(db.String(_settings.SHORT_ADDRESS_LENGTH), primary_key=True)
    url = db.Column(db.Text)
    time_stamp = db.Column(db.Float)

    def __init__(self, word, url, time_stamp):
        self.word = word
        self.url = url
        self.time_stamp = time_stamp
