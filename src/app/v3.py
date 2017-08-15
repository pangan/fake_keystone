from flask import Blueprint, abort, jsonify, Response, request
from _settings import TOKEN
from datetime import datetime, timedelta
import json

v3 = Blueprint('v3',  __name__)


@v3.route('/')
def hello_token():
    return 'Hello'


@v3.route('/auth/tokens', methods=['POST'])
def get_token():
    password_body = {
        "token": {
            "is_domain": False,
            "methods": ["password"],
            "roles": [{"id": "123456", "name": "monasca-agent"}],
            "expires_at": _get_timestamp(feature_seconds=30),
            "project": {
                "domain": {
                    "id": "default",
                    "name": "Default"
                },
                "id": "123456",
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
                            "id": "123456"
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
            "issued_at": _get_timestamp()
        }
    }

    token_body = {
        "token": {
            "methods": [
                "token"
            ],
            "expires_at": _get_timestamp(feature_seconds=30),
            "extras": {},
            "user": {
                "domain": {
                    "id": "default",
                    "name": "Default"
                },
                "id": "123456",
                "name": "admin",
                "password_expires_at": None
            },
            "audit_ids": [
                "123456"
            ],
            "issued_at": _get_timestamp()
        }
    }
    token_body = {
        "token": {
            "is_domain": False,
            "methods": ["token", "password"],
            "roles": [
                {
                    "id": "123456",
                    "name": "monasca-agent"
                },
                {
                    "id": "123456",
                    "name": "monasca-user"
                }
            ],
            "expires_at": _get_timestamp(feature_seconds=30),
            "project": {
                "domain": {
                    "id": "default",
                    "name": "Default"
                },
                "id": "123456",
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
                            "id": "123456"
                        }
                    ],
                    "type": "compute_legacy",
                    "id": "123456",
                    "name": "nova_legacy"
                },
                {
                    "endpoints": [
                        {
                            "url": "http://10.5.0.112:8776/v3/3d73e17ed2114828900f548098e2c157",
                            "interface": "public",
                            "region": "RegionOne",
                            "region_id": "RegionOne",
                            "id": "123456"
                        }
                    ],
                    "type": "volumev3",
                    "id": "123456",
                    "name": "cinderv3"
                },
                {
                    "endpoints": [
                        {
                            "url": "http://10.5.0.112:9292",
                            "interface": "public",
                            "region": "RegionOne",
                            "region_id": "RegionOne",
                            "id": "123456"
                        }
                    ],
                    "type": "image",
                    "id": "123456",
                    "name": "glance"
                },
                {
                    "endpoints": [
                        {
                            "url": "http://10.5.0.112:8776/v1/3d73e17ed2114828900f548098e2c157",
                            "interface": "public",
                            "region": "RegionOne",
                            "region_id": "RegionOne",
                            "id": "123456"
                        }
                    ],
                    "type": "volume",
                    "id": "123456",
                    "name": "cinder"
                },
            ],
            "user": {
                "password_expires_at": None,
                "domain": {
                    "id": "default",
                    "name": "Default"
                },
                "id": "123456",
                "name": "monasca-agent"
            },
            "audit_ids": [
                "PrNbZZGMS8yKFW5X3AQtKg",
                "nuHKzNyVQJW3y5KmzkuyMA"
            ],
            "issued_at": _get_timestamp()
        }
    }



    request_body = json.loads(request.data)

    print ('AUTH::header-> {0}'.format(request.headers))
    print ('AUTH::body-> {0}'.format(request_body))

    if 'password' in request_body['auth']['identity']['methods']:
        response = Response.response = jsonify(password_body)
    if 'token' in request_body['auth']['identity']['methods']:
        response = Response.response = jsonify(token_body)
        print token_body
    response.content_type = 'application/json'
    response.headers['X-Subject-Token'] = TOKEN

    return response, 201
# '{"auth":{"identity":{"methods":["token"],"token":{"id":"123456"}},"scope":{"project":{"name":"mini-mon2","domain":{"name":"Default"}}}}}'

@v3.route('/auth/projects', methods=['GET'])
def get_projects():
    body = {
        "projects": [
            {
                "domain_id": "12346",
                "enabled": True,
                "id": "1234",
                "links": {
                    "self": "http://10.5.0.1:5000/identity/v3/projects/1234"
                },
                "name": "Default"
            }
        ],
        "links": {
            "self": "http://10.5.0.1:5000/identity/v3/auth/projects",
            "previous": None,
            "next": None

        }
    }

    body = {
        "links": {
            "self": "http://10.5.0.1/identity/v3/auth/projects",
            "previous": None,
            "next": None
        },
        "projects": [
            {
                "is_domain": False,
                "description": "",
                "links": {
                    "self": "http://10.5.0.1/identity/v3/projects/3d73e17ed2114828900f548098e2c157"
                },
                "enabled": True,
                "id": "3d73e17ed2114828900f548098e2c157",
                "parent_id": "default",
                "domain_id": "default",
                "name": "mini-mon"
            }
        ]
    }

    response = Response.response = jsonify(body)


    #request_body = json.loads(request.data)

    print ('PROJ::header-> {0}'.format(request.headers))
    print ('PROJ::body-> {0}'.format(request.date))

    response.content_type = 'application/json'
    return response, 200



@v3.route('/error')
def return_error():
    abort(501)


@v3.route('/<path:path>')
def other_path(path):

    return path

def _get_timestamp(feature_days=0, feature_hours=0, feature_seconds=0):
    time_stamp = datetime.now() + timedelta(days=feature_days, hours=feature_hours, seconds=feature_seconds)
    return time_stamp.strftime('%Y-%m-%dT%H:%M:%S.000000Z')
