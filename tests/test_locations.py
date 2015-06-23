from hamcrest import *
from adminautomation.pages import LocationsPage, EditLocationPage, NewLocationPage
import pytest
import bypassqatesting.api.locations


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
    bypassqatesting.api.locations.create_location(data=data)
    page.refresh_page()
    page.click_delete_location_link_by_name(data['location[name]'])
    page.accept_alert()
    names = page.get_column_items_text_by_header_text('Name')
    assert_that(data['location[name]'], not_(is_in(names)))
