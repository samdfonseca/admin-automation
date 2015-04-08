import requests
import os
import json
from uuid import uuid4 as uuid
from urlparse import urljoin

from adminautomation.utils.api.auth import get_session_token


def new_cash_order(**kwargs):
    base_url = kwargs.get('base_url', 'http://integration.bypasslane.com')
    auth_server = kwargs.get('auth_server', 'http://auth-integration.bypasslane.com')
    user = kwargs.get('user', os.getenv('ADMIN_USER'))
    password = kwargs.get('password', os.getenv('ADMIN_PASSWORD'))
    session_token = kwargs.get('session_token', get_session_token(user=user,
                                                                  password=password,
                                                                  auth_server=auth_server))
    venue_id = kwargs.get('venue_id', '86')
    order_taker_id = kwargs.get('order_taker_id', '8097')
    location_id = kwargs.get('location_id', '2554')
    item_id = kwargs.get('item_id', '23888')
    unit_price = kwargs.get('unit_price', 10)
    quantity = kwargs.get('quantity', 1)

    request_data = dict(
        order_taker_id=str(order_taker_id),
        location_id=str(location_id),
        name="NO NAME",
        device="admin",
        device_serial_number="bypass-admin-virtual-terminal{0}".format(venue_id),
        service_location_id="",
        adjustments=[dict(uuid=str(uuid()),
                          amount=0,
                          adjustment_type="surcharge",
                          adjustment_percentage=0,
                          line_item_uuid="null")],
        payments=[dict(uuid=str(uuid()),
                       amount=str((quantity * unit_price)),
                       tip_amount=0,
                       payment_type="cash")],
        line_items=[dict(uuid=str(uuid()),
                         count=quantity,
                         unit_price=unit_price,
                         item_id=str(item_id))])

    headers = {
        'X-SESSION-TOKEN': session_token,
        'X-BYPASS-ADMIN-VENUE': venue_id
    }
    url = urljoin(base_url, 'api/venue/concessions/{0}/orders.json'.format(location_id))
    resp = requests.post(url, json=request_data, headers=headers)
    # Raises HTTPError, if one occurred.
    resp.raise_for_status()
    order = json.loads(resp.content)
    return order

