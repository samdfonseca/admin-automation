import os
from hamcrest import *
from requests import HTTPError
from adminautomation.utils.api.orders import new_cash_order


def set_up():
    with open('.testauth') as f:
        user, password = f.readlines()
    os.environ['ADMIN_USER'] = user.strip()
    os.environ['ADMIN_PASSWORD'] = password.strip()


def test_new_cash_order_default_args():
    try:
        order = new_cash_order()
    except HTTPError:
        order = None
    assert_that(order, is_(dict))
    assert_that(order, has_entry('state', 'closed'))
    assert_that(order, has_key('line_items'))
    assert_that(order['line_items'][0], has_entry('item_id', 23888))


def test_new_cash_order_invalid_user_error_response():
    bad_data = {
        'user': 'notarealuser@bypassmobile.com',
        'password': 'fakepass'
    }
    assert_that(calling(new_cash_order).with_args(**bad_data), raises(HTTPError))


def test_new_cash_order_nondefault_item():
    try:
        order = new_cash_order(item_id='24996')
    except HTTPError:
        order = None
    assert_that(order, is_(dict))
    assert_that(order, has_entry('state', 'closed'))
    assert_that(order, has_key('line_items'))
    assert_that(order['line_items'][0], has_entry('item_id', 24996))
