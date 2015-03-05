# Functions for getting a pre-authenticated session cookie for new Admin

import requests
from bs4 import BeautifulSoup as BS
from os.path import abspath, dirname
from simplejson import load as readjson
from urllib import urlencode
from urlparse import urlparse, urlunparse


# Hides the InsecureRequestWarning received on integration
requests.packages.urllib3.disable_warnings()


class PersistentSessionCookie(object):
    COOKIE = None


def build_url(root_url, path):
    parsed_root_url = urlparse(root_url)
    full_url = urlunparse((parsed_root_url.scheme, parsed_root_url.netloc, path, '', '', ''))
    # print("Built URL:", full_url)

    return full_url


def get_authenticity_token(response):
    soup = BS(response.content)
    element = soup.find('input', attrs={'name': 'authenticity_token'})

    return element['value']


def _build_login_page_request(root_url, path='admin_sessions/new'):
    url = build_url(root_url, path)
    request = requests.Request('GET', url)
    
    return request


def _build_login_request(user, passwd, authenticity_token, root_url, path='admin_sessions'):
    url = build_url(root_url, path)
    data = {'authenticity_token': authenticity_token,
            'user[email]': user,
            'user[password]': passwd}
    request = requests.Request('POST', url, data=urlencode(data))

    return request


def _build_update_venue_request(venue_id, authenticity_token, root_url, path='admin_sessions/update_venue'):
    url = build_url(root_url, path)
    data = {'authenticity_token': authenticity_token,
            'change_venue': venue_id}
    request = requests.Request('POST', url, data=urlencode(data))

    return request


def _get_selenium_style_cookie(session, root_url):
    cookie_name = "_session_id"
    cookie_domain = urlparse(root_url).netloc
    cookie_path = "/"
    # print(session.cookies)
    cookie_value = session.cookies[cookie_name]

    cookie = {'domain': cookie_domain,
              'name': cookie_name,
              'path': cookie_path,
              'value': cookie_value}

    return cookie


def _get_session_cookie(user, passwd, venue_id, root_url):
    session = requests.Session()
    
    # Get login page
    request = session.prepare_request(_build_login_page_request(root_url))
    response = session.send(request, verify=False)
    # print("Login Page Cookies:", response.cookies)

    # Perform login request
    authenticity_token = get_authenticity_token(response)
    request = session.prepare_request(_build_login_request(user, passwd, authenticity_token, root_url))
    response = session.send(request, verify=False)
    # print("Login Request Cookies:", response.cookies)

    # Perform update venue request
    authenticity_token = get_authenticity_token(response)
    request = session.prepare_request(_build_update_venue_request(venue_id, authenticity_token, root_url))
    response = session.send(request, verify=False)
    # print("Update Venue Cookies:", response.cookies)

    # print("Session Cookies:", session.cookies)

    cookie = _get_selenium_style_cookie(session, root_url)

    return cookie


def get_session_cookie(**kwargs):
    auth_file = kwargs.get("auth_file", './tests/data/auth.json')

    if PersistentSessionCookie.COOKIE is None:
        # with open(abspath(dirname(__file__) + '/../../tests/data/auth.json')) as f:
        with open(auth_file) as f:
            auth_info = readjson(f)

        user = kwargs.get('user', auth_info['user'])
        passwd = kwargs.get('passwd', auth_info['passwd'])
        venue = kwargs.get('venue', auth_info['default_venue'])
        root_url = kwargs.get('root_url', auth_info['root_url'])

        PersistentSessionCookie.COOKIE = _get_session_cookie(user, passwd, venue, root_url)

    return PersistentSessionCookie.COOKIE


def log_session_out(root_url, session_id):
    root_url = 'https://{}'.format(root_url) if not root_url.startswith('https://') else root_url
    requests.post('{}/admin_sessions'.format(root_url), cookies={'_session_id': session_id},
                  data={'_method': 'delete'}, verify=False)
    PersistentSessionCookie.COOKIE = None

