import requests
import json
from urlparse import urljoin
from os import getenv


def get_session_token(**kwargs):
    user = kwargs.get('user', getenv('ADMIN_USER'))
    password = kwargs.get('password', getenv('ADMIN_PASSWORD'))
    auth_server = kwargs.get('auth_server', 'http://auth-integration.bypasslane.com')
    url = urljoin(auth_server, 'auth.json') if not auth_server.endswith('auth.json') else auth_server
    resp = requests.post(url, auth=(user, password))
    resp.raise_for_status()
    token = json.loads(resp.content)['session_token']
    return token
