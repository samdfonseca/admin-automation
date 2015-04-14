import operator
import os
import requests
import json
from urlparse import urljoin

from adminautomation.utils.api.auth import get_session_token


def get_item_count(**kwargs):
    base_url = kwargs.get('base_url', 'https://secure-integration.bypassmobile.com')
    api_path = 'api/admin/venue/items.json'
    auth_server = kwargs.get('auth_server', 'http://auth-integration.bypasslane.com')
    user = kwargs.get('user', os.getenv('ADMIN_USER'))
    password = kwargs.get('password', os.getenv('ADMIN_PASSWORD'))
    session_token = kwargs.get('session_token', get_session_token(user=user,
                                                                  password=password,
                                                                  auth_server=auth_server))
    venue_id = str(kwargs.get('venue_id', '86'))
    url = urljoin(base_url, api_path)
    headers = {
        'X-SESSION-TOKEN': session_token,
        'X-BYPASS-ADMIN-VENUE': venue_id
    }
    resp = requests.get(url, headers=headers, verify=False)
    resp.raise_for_status()
    items = json.loads(resp.content)
    return int(items['meta']['count'])


def get_items_list(**kwargs):
    base_url = kwargs.get('base_url', 'https://secure-integration.bypassmobile.com')
    api_path = 'api/admin/venue/items.json'
    auth_server = kwargs.get('auth_server', 'http://auth-integration.bypasslane.com')
    user = kwargs.get('user', os.getenv('ADMIN_USER'))
    password = kwargs.get('password', os.getenv('ADMIN_PASSWORD'))
    session_token = kwargs.get('session_token', get_session_token(user=user,
                                                                  password=password,
                                                                  auth_server=auth_server))
    venue_id = str(kwargs.get('venue_id', '86'))
    headers = {
        'X-SESSION-TOKEN': session_token,
        'X-BYPASS-ADMIN-VENUE': venue_id
    }
    item_count = get_item_count(**kwargs)
    url = urljoin(base_url, api_path)
    url += '?per_page={0}'.format(item_count)
    resp = requests.get(url, headers=headers, verify=False)
    resp.raise_for_status()
    all_items = json.loads(resp.content)
    return sorted(all_items['items'], key=operator.itemgetter('name'))
