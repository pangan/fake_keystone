from flask import Blueprint, abort, jsonify, Response
from _settings import TOKEN
import json

v3 = Blueprint('v3',  __name__)


@v3.route('/')
def hello_token():
    return 'Hello'


@v3.route('/auth/tokens')
def get_token():
    body = {
        "token": {
            "is_domain": False,
            "methods": ["password"],
            "roles": [{"id": "0a10a3d4c5234014a059e9161941fe36", "name": "monasca-agent"},
                      {"id": "74f1cd55623344bea3aaa924930b94f3", "name": "monasca-user"}],
            "expires_at": "2017-08-11T09:42:22.000000Z",
            "project": {
                "domain": {
                    "id": "default",
                    "name": "Default"
                },
                "id": "3d73e17ed2114828900f548098e2c157",
                "name": "mini-mon"
            },
            "catalog": [
                {
                    "endpoints": [
                        {
                            "url": "http://10.5.0.112:8774/v2/3d73e17ed2114828900f548098e2c157",
                            "interface": "public",
                            "region": "RegionOne",
                            "region_id": "RegionOne",
                            "id": "3536eb9cc27e477994281c9c6910cde5"
                        }
                    ],
                    "type": "compute_legacy",
                    "id": "1a7474387b7040118565085743a54d2f",
                    "name": "nova_legacy"
                },
                {
                    "endpoints": [
                        {
                            "url": "http://10.5.0.112:8776/v3/3d73e17ed2114828900f548098e2c157",
                            "interface": "public",
                            "region": "RegionOne",
                            "region_id": "RegionOne",
                            "id": "0204826371904380a055f6819427e4ed"
                        }
                    ],
                    "type": "volumev3",
                    "id": "1dd893b5a9984336a50c5b9c3688ae95",
                    "name": "cinderv3"
                },
            ],
            "user": {
                "password_expires_at": None,
                "domain": {
                    "id": "default",
                    "name": "Default"
                },
                "id": "079630c2e28444de94e89ec049ed561f",
                "name": "monasca-agent"
            },
            "audit_ids": ["F7NiXuosQrmyjlA0-4-s4A"],
            "issued_at": "2017-08-11T08:42:22.000000Z"
        }
    }

    response = Response.response = jsonify(body)

    response.content_type = 'application/json'
    response.headers['X-Subject-Token'] = TOKEN
    return response, 201


@v3.route('/error')
def return_error():
    abort(501)


@v3.route('/<path:path>')
def other_path(path):

    return

