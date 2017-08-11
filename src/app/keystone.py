"""
URL Shortening Web application

Author : Amir Mofakhar <pangan@gmail.com>
"""
from flask import Flask, request

from . import _settings
from token import token

app = Flask(__name__)

app.register_blueprint(token)


@app.route('/')
def index():
    return 'index'





