from flask import Blueprint, abort

v2 = Blueprint('v2',  __name__)


@v2.route('/', defaults={'path': 'index'})
@v2.route('/<path:path>')
def hello_version_2(path):
    return 'Version 2 is not supported yet!'
