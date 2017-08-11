from flask import Blueprint, abort

token = Blueprint('token', __name__)


@token.route('/')
def hello_token():
    return 'Hello'


@token.route('/error')
def return_error():
    abort(501)


@token.route('/<path:path>')
def other_path(path):
    return path

