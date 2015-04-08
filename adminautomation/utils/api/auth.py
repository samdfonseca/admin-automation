import requests
import json
from urlparse import urljoin


def get_session_token(user, password, auth_server='http://auth-integration.bypasslane.com'):
    auth_server = urljoin(auth_server, 'auth.json') if not auth_server.endswith('auth.json') else auth_server
    resp = requests.post(auth_server, auth=(user, password))
    resp.raise_for_status()
    token = json.loads(resp.content)['session_token']
    return token
