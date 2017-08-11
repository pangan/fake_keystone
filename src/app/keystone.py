"""
URL Shortening Web application

Author : Amir Mofakhar <pangan@gmail.com>
"""
from flask import Flask, request


from v3 import v3
from v2 import v2

app = Flask(__name__)

app.register_blueprint(v3, url_prefix='/v3')
app.register_blueprint(v2, url_prefix='/v2')




