# Functions for getting a pre-authenticated session cookie for new Admin

import requests
from bs4 import BeautifulSoup as BS
from os.path import abspath, dirname
from os.path import join as joinpath
from simplejson import load as readjson
from urllib import urlencode
from urlparse import urlparse, urljoin
import logging


class PersistentAuthInfo(object):
    _DATA_FILE = "./data/auth.json"
    AUTH_INFO = {"session_cookie_name": "_session_id",
                 "root_url": "https://admin-integration.bypasslane.com",
                 "default_venue": 86,
                 "user": None,
                 "passwd": None}

    COOKIE = None


requests.packages.urllib3.disable_warnings()
logger = logging.getLogger("adminautomation.utils.adminsession")
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(ch)

logger.info("Using auth data from file: {}".format(PersistentAuthInfo._DATA_FILE))


def build_url(path):
    return urljoin(PersistentAuthInfo.AUTH_INFO["root_url"], path)


def get_authenticity_token(response):
    soup = BS(response.content)
    element = soup.find('input', attrs={'name': 'authenticity_token'})

    return element['value']


def _build_login_page_request(path='admin_sessions/new'):
    url = build_url(path)
    request = requests.Request('GET', url)
    
    return request


def _build_login_request(user, passwd, authenticity_token, path='admin_sessions'):
    url = build_url(path)
    data = {'authenticity_token': authenticity_token,
            'user[email]': user,
            'user[password]': passwd}
    request = requests.Request('POST', url, data=urlencode(data))

    return request


def _build_update_venue_request(venue_id, authenticity_token, path='admin_sessions/update_venue'):
    url = build_url(path)
    data = {'authenticity_token': authenticity_token,
            'change_venue': venue_id}
    request = requests.Request('POST', url, data=urlencode(data))

    return request


def _get_selenium_style_cookie(response):
    cookie = {}
    cookie['domain'] = urlparse(response.url).netloc
    cookie['name'] = PersistentAuthInfo.AUTH_INFO["session_cookie_name"]
    cookie['path'] = '/'
    cookie['secure'] = False
    cookie['value'] = response.cookies.get(PersistentAuthInfo.AUTH_INFO["session_cookie_name"])

    return cookie


def _get_session_cookie(user, passwd, venue_id):
    session = requests.Session()

    # Get login page
    request = session.prepare_request(_build_login_page_request())
    logger.info("Getting _session_id cookie. Login page: {}".format(request.url))
    response = session.send(request, verify=False)

    # Perform login request
    authenticity_token = get_authenticity_token(response)
    request = session.prepare_request(_build_login_request(user, passwd, authenticity_token))
    logger.info("Getting _session_id cookie. Choose venue page: {}".format(request.url))
    response = session.send(request, verify=False)

    # Perform update venue request
    authenticity_token = get_authenticity_token(response)
    request = session.prepare_request(_build_update_venue_request(venue_id, authenticity_token))
    logger.info("Getting _session_id cookie. Main page: {}".format(request.url))
    response = session.send(request, verify=False)

    cookie = _get_selenium_style_cookie(response)

    return cookie


def get_session_cookie():
    ps = PersistentAuthInfo
    if ps.COOKIE is None:
        with open(ps._DATA_FILE) as f:
            ps.AUTH_INFO = readjson(f)
        logger.info("Session cookie is None. Getting new session cookie.")
        ps.COOKIE = _get_session_cookie(ps.AUTH_INFO["user"], ps.AUTH_INFO["passwd"], ps.AUTH_INFO["default_venue"])

    return ps.COOKIE



