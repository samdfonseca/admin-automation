
trclient = None


def setup_package():
    from os import getenv
    from testrailwrapper.testrailclient import TestRailClient
    global trclient
    testrail_url = getenv('TESTRAIL_URL', 'https://bypassmobile.testrail.com')
    testrail_user = getenv('TESTRAIL_USER')
    testrail_password = getenv('TESTRAIL_PASSWORD')
    trclient = TestRailClient(testrail_url, testrail_user, testrail_password)
