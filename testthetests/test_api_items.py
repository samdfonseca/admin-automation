import os
from hamcrest import *
from random import randrange
from adminautomation.utils.api.items import get_items_list, get_item_count


def set_up():
    with open('.testauth') as f:
        user, password = f.readlines()
    os.environ['ADMIN_USER'] = user.strip()
    os.environ['ADMIN_PASSWORD'] = password.strip()


def test_get_items_default_args_length():
    items = get_items_list()
    item_count = get_item_count()
    assert(items, has_length(item_count))


def test_get_items_default_args_keys():
    items = get_items_list()
    assert(items[randrange(0, len(items))], has_key('tax_rate'))
    assert(items[randrange(0, len(items))], has_key('id'))
    assert(items[randrange(0, len(items))], has_key('recipe_id'))
    assert(items[randrange(0, len(items))], has_key('category_name'))
    assert(items[randrange(0, len(items))], has_key('base_price'))
    assert(items[randrange(0, len(items))], has_key('name'))
    assert(items[randrange(0, len(items))], has_key('reporting_group_name'))


def test_get_items_nondefault_venue():
    items = get_items_list(venue_id=187)
    item_count = get_item_count(venue_id=187)
    assert(items, has_length(item_count))
    assert(items[randrange(0, item_count)], has_key('tax_rate'))
    assert(items[randrange(0, item_count)], has_key('id'))
    assert(items[randrange(0, item_count)], has_key('recipe_id'))
    assert(items[randrange(0, item_count)], has_key('category_name'))
    assert(items[randrange(0, item_count)], has_key('base_price'))
    assert(items[randrange(0, item_count)], has_key('name'))
    assert(items[randrange(0, item_count)], has_key('reporting_group_name'))


def test_get_items_nondefault_user():
    items = get_items_list(user='qatestuser@bypassmobile.com', password='bypassqa')
    item_count = get_item_count(user='qatestuser@bypassmobile.com', password='bypassqa')
    assert(items, has_length(item_count))
    assert(items[randrange(0, item_count)], has_key('tax_rate'))
    assert(items[randrange(0, item_count)], has_key('id'))
    assert(items[randrange(0, item_count)], has_key('recipe_id'))
    assert(items[randrange(0, item_count)], has_key('category_name'))
    assert(items[randrange(0, item_count)], has_key('base_price'))
    assert(items[randrange(0, item_count)], has_key('name'))
    assert(items[randrange(0, item_count)], has_key('reporting_group_name'))
