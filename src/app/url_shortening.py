import random
import string
import time

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from src.app import _settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = _settings.DATABASE

db = SQLAlchemy(app)


class ShortURL(db.Model):
    """Table of database used for URL Shortening"""
    word = db.Column(db.String(4), primary_key=True)
    url = db.Column(db.Text)
    time_stamp = db.Column(db.Float)

    def __init__(self, word, url, time_stamp):
        self.word = word
        self.url = url
        self.time_stamp = time_stamp


def assign_word_to_url(long_url):
    word = get_a_word_that_is_not_used_already()
    new_short_address = ShortURL(word, long_url, time.time())
    db.session.add(new_short_address)
    db.session.commit()
    return word


def _clean_old_addresses_from_database():
    ShortURL.query.filter(ShortURL.time_stamp<time.time()-_settings.SHORT_ADDRESS_LIFE_TIME_IN_SECOND).delete()


def get_a_word_that_is_not_used_already():
    while True:
        _clean_old_addresses_from_database()
        new_word = _generate_random_string()
        if not ShortURL.query.filter_by(word=new_word).first():
            break
    return new_word


def _generate_random_string():
    return ''.join(random.choice(string.lowercase) for _ in range(4))


def get_original_url(short_address):
    original_address = ShortURL.query.filter_by(word=short_address).first()
    if original_address:
        return original_address.url

    return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_short_url', methods=['POST'])
def get_short_url():
    if request.form['long_url']:
        assigned_word = assign_word_to_url(request.form['long_url'])
        if assigned_word:
            return render_template('short_address.html',
                                   short_url=assigned_word,
                                   url_root=_settings.SERVER_NAME)
        else:
            return render_template('error_page.html',
                                   error_message=2)


@app.route('/<path:path>')
def redirect_short_url(path):
    original_url = get_original_url(path)
    if original_url:
        return redirect(original_url)

    return render_template('error_page.html', error_message=1)


if __name__ == '__main__':
    db.create_all()
    app.run()