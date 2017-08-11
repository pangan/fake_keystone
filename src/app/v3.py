from flask import Blueprint, abort, jsonify
from _settings import TOKEN

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
                {
                    "endpoints": [
                        {
                            "url": "http://10.5.0.112:9292",
                            "interface": "public",
                            "region": "RegionOne",
                            "region_id": "RegionOne",
                            "id": "e24d6e0821054939b3cfb73a07e8e1da"
                        }
                    ],
                    "type": "image",
                    "id": "4d63735eac504c2096e90f4c518496a0",
                    "name": "glance"
                },
                {
                    "endpoints": [
                        {
                            "url": "http://10.5.0.112:8776/v1/3d73e17ed2114828900f548098e2c157",
                            "interface": "public",
                            "region": "RegionOne",
                            "region_id": "RegionOne",
                            "id": "b614b0f106d646d1b4a1fb8dd35b50fc"
                        }
                    ],
                    "type": "volume",
                    "id": "5743bee349be4da496fb661f061cb219",
                    "name": "cinder"
                }
                , {"endpoints": [{"url": "http://10.5.0.112:8070/v2.0", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "1af0ce39d4d7463fb3d4f1578c57683c"}, {"url": "http://10.5.0.112:8070/v2.0", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "1dd6fe7739bf4394912bb29cbca36318"}, {"url": "http://10.5.0.112:8070/v2.0", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "67ceb893b4cf441e83ee583442020ccd"}], "type": "monitoring", "id": "634cb38e744d4b18a1d70cfad25401f4", "name": "monasca"}, {"endpoints": [{"url": "http://10.5.0.112:8776/v2/3d73e17ed2114828900f548098e2c157", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "7acb625f6b3f4371928408f078ee1b00"}], "type": "volumev2", "id": "8826c1a2d823427eab5ebc25b359185d", "name": "cinderv2"}, {"endpoints": [{"url": "http://10.5.0.112/placement", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "0c111211c2c34122a187f39305cf7530"}], "type": "placement", "id": "9342c2fe564b47589e9f6a6ba36f1d96", "name": "placement"}, {"endpoints": [{"url": "http://10.5.0.112:8774/v2.1", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "f7266271446a43009b3aeada1cafaacb"}], "type": "compute", "id": "c32df799039a4a63a4a3b11f980a386e", "name": "nova"}, {"endpoints": [{"url": "http://10.5.0.112/identity_admin", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "59137b7bc1654b3fb322ce3ae209ce0c"}, {"url": "http://10.5.0.112/identity", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "faa11e4d8a184647849d1f2d41e157a1"}], "type": "identity", "id": "d138fbe3dcfd474d9fd88747a34b5d1a", "name": "keystone"}, {"endpoints": [{"url": "http://10.5.0.112:9696/", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "08622c34c3be4d3e8ef26945b0b30a05"}], "type": "network", "id": "efbea9b1c4014302bb84bd7369bf76ec", "name": "neutron"}], "user": {"password_expires_at": None, "domain": {"id": "default", "name": "Default"}, "id": "079630c2e28444de94e89ec049ed561f", "name": "monasca-agent"}, "audit_ids": ["F7NiXuosQrmyjlA0-4-s4A"], "issued_at": "2017-08-11T08:42:22.000000Z"}}
    #headers = {'Content-Length': '3731',
    #           'X-Subject-Token': TOKEN,
    #           'Vary': 'X-Auth-Token',
    #           'Keep-Alive': 'timeout=5, max=100',
    #           'Server': 'Apache/2.4.18 (Ubuntu)',
    #           'Connection': 'Keep-Alive',
    #           'Date': 'Fri, 11 Aug 2017 08:43:42 GMT',
    #           'Content-Type': 'application/json',
    #           'x-openstack-request-id': 'req-73d1ad44-51ce-4b57-a1e9-609e7a72d6aa'}

    return jsonify(body), 201

@v3.route('/error')
def return_error():
    abort(501)


@v3.route('/<path:path>')
def other_path(path):

    return

