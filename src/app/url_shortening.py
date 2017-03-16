"""
URL Shortening Web application

Author : Amir Mofakhar <pangan@gmail.com>
"""
from flask import Flask, render_template, request, redirect

from . import _settings
from .utils import assign_word_to_url, get_original_url

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = _settings.DATABASE


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
                                   url_root=_settings.SERVER_BASE_ADDRESS)
        else:
            return render_template('error_page.html',
                                   error_message=2)


@app.route('/<path:path>')
def redirect_short_url(path):
    original_url = get_original_url(path)
    if original_url:
        return redirect(original_url)

    return render_template('error_page.html', error_message=1)
