from hamcrest import *
from adminautomation.pages import LocationsPage, EditLocationPage, NewLocationPage
import pytest
from bypassqatesting.api import locations


@pytest.fixture()
def page(authenticated_driver):
    return LocationsPage(authenticated_driver, skip_login=True)

@pytest.fixture()
def location_data(testdata):
    return testdata['test_locations']

def test_filter_by_location_name_full_match(page, location_data):
    """@type page: LocationsPage"""
    location_name = location_data['location_name']
    page.show_filters()
    page.clear_all_filters()
    page.search_for_location(location_name)
    names = page.get_column_items_text_by_header_text('Name')
    assert_that(location_name, is_in(names))

def test_filter_by_location_name_partial_starting_match(page, location_data):
    """@type page: LocationsPage"""
    location_name = location_data['location_name']
    query = location_name[:len(location_name)/2]
    page.show_filters()
    page.clear_all_filters()
    page.search_for_location(query)
    names = page.get_column_items_text_by_header_text('Name')
    assert_that(location_name, is_in(names))

def test_filter_by_location_name_partial_non_starting_match(page, location_data):
    """@type page: LocationsPage"""
    location_name = location_data['location_name']
    query = location_name[len(location_name)/2:]
    page.show_filters()
    page.clear_all_filters()
    page.search_for_location(query)
    names = page.get_column_items_text_by_header_text('Name')
    assert_that(location_name, is_in(names))

def test_edit_location_link(page, location_data):
    """@type page: LocationsPage"""
    location_name = location_data['location_name']
    page.click_edit_location_link_by_name(location_name)
    page = EditLocationPage(page.driver)
    """@type page: EditLocationPage"""
    assert_that(page.name, is_(location_name))

def test_delete_location_link(page, location_data):
    """@type page: LocationsPage"""
    data = location_data['basic_location_data']
    locations.create_location(data=data)
    page.refresh_page()
    page.click_delete_location_link_by_name(data['location[name]'])
    page.accept_alert()
    names = page.get_column_items_text_by_header_text('Name')
    assert_that(data['location[name]'], not_(is_in(names)))

def test_filter_by_location_type_concession(page):
    """@type page: LocationsPage"""
    page.show_filters()
    page.filter_table_by_type('Concession')
    # This is gonna take a while...
    types = page.get_column_items_text_by_header_text('Type')
    map(lambda i: assert_that(i, is_('Concession')), types)

def test_filter_by_location_type_commissary(page):
    """@type page: LocationsPage"""
    page.show_filters()
    page.filter_table_by_type('Commissary')
    # This is gonna take a while...
    types = page.get_column_items_text_by_header_text('Type')
    map(lambda i: assert_that(i, is_('Commissary')), types)

def test_filter_by_location_type_vending_room(page):
    """@type page: LocationsPage"""
    page.show_filters()
    page.filter_table_by_type('Vending Room')
    # This is gonna take a while...
    types = page.get_column_items_text_by_header_text('Type')
    map(lambda i: assert_that(i, is_('Vending Room')), types)

def test_filter_by_location_type_restaurant(page):
    """@type page: LocationsPage"""
    page.show_filters()
    page.filter_table_by_type('Restaurant')
    # This is gonna take a while...
    types = page.get_column_items_text_by_header_text('Type')
    map(lambda i: assert_that(i, is_('Restaurant')), types)

def test_filter_by_name_and_type(page, location_data):
    """@type page: LocationsPage"""
    location_name = location_data['location_name']
    query = location_name[0]
    location_type = location_data['location_type']
    page.show_filters()
    page.search_for_location(query)
    page.filter_table_by_type(location_type)
    names = page.get_column_items_text_by_header_text('Name')
    assert_that(location_name, is_in(names))

def test_clear_filters(page, location_data):
    """@type page: LocationsPage"""
    location_name = location_data['location_name'][0]
    query = location_name[0]
    location_type = location_data['location_type']
    names_pre = page.get_column_items_text_by_header_text('Name')
    page.show_filters()
    page.search_for_location(query)
    page.filter_table_by_type(location_type)
    page.clear_all_filters()
    names_post = page.get_column_items_text_by_header_text('Name')
    for name in names_pre:
        assert_that(name, is_in(names_post))

