# Functions for getting a pre-authenticated session cookie for new Admin

import requests
from bs4 import BeautifulSoup as BS
from os.path import abspath, dirname
from simplejson import load as readjson
from urllib import urlencode
from urlparse import urlparse, urlunparse


ADMIN_SCHEME = 'https'
ADMIN_NETLOC = 'admin-integration.bypasslane.com'
SESSION_COOKIE_NAME = '_bypass_admin_session'

class PersistentSessionCookie(object):
    COOKIE = None


def build_url(path):
    return urlunparse((ADMIN_SCHEME, ADMIN_NETLOC, path, '', '', ''))


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
    cookie = {'domain': urlparse(response.url).netloc,
              'name': SESSION_COOKIE_NAME,
              'path': response.headers['set-cookie'].split('; ')[1].split('=')[1],
              'secure': False if response.headers['set-cookie'].split('; ')[2] is 'HttpOnly' else True,
              'value': response.cookies[SESSION_COOKIE_NAME]}

    return cookie


def _get_session_cookie(user, passwd, venue_id):
    session = requests.Session()
    
    # Get login page
    request = session.prepare_request(_build_login_page_request())
    response = session.send(request, verify=False)

    # Perform login request
    authenticity_token = get_authenticity_token(response)
    request = session.prepare_request(_build_login_request(user, passwd, authenticity_token))
    response = session.send(request, verify=False)

    # Perform update venue request
    authenticity_token = get_authenticity_token(response)
    request = session.prepare_request(_build_update_venue_request(venue_id, authenticity_token))
    response = session.send(request, verify=False)

    cookie = _get_selenium_style_cookie(response)

    return cookie


def get_session_cookie():
    if PersistentSessionCookie.COOKIE is None:
        with open(abspath(dirname(__file__) + '/../../tests/data/auth.json')) as f:
            auth_info = readjson(f)

        PersistentSessionCookie.COOKIE = _get_session_cookie(auth_info['user'],
                                                      auth_info['passwd'],
                                                      auth_info['default_venue'])

    return PersistentSessionCookie.COOKIE



