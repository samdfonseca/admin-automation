
trclient = None
session_info = None


def read_session_info(auth_file='./tests/data/auth.json'):
    from json import loads as loadjson
    with open(auth_file) as f:
        content = loadjson(f.read())
    return content


def setup_package():
    from os import getenv
    from testrailwrapper.testrailclient import TestRailClient
    global trclient
    testrail_url = getenv('TESTRAIL_URL', 'https://bypassmobile.testrail.com')
    testrail_user = getenv('TESTRAIL_USER')
    testrail_password = getenv('TESTRAIL_PASSWORD')
    trclient = TestRailClient(testrail_url, testrail_user, testrail_password) if trclient is None else trclient

    global session_info
    session_info = read_session_info()
