from hamcrest import *
from adminautomation.pages.locations import LocationsPage
import pytest


@pytest.fixture()
def page(authenticated_driver):
    return LocationsPage(authenticated_driver, skip_login=True)

@pytest.fixture()
def location_data(testdata):
    return testdata['test_locations']

def test_filter_by_location_name_full_match(page, location_data):
    location_name = location_data['location_name']
    page.show_filters()
    page.clear_all_filters()
    page.search_for_location(location_name)
    names = page.get_column_items_text_by_header_text('Name')
    assert_that(location_name, is_in(names))

def test_filter_by_location_name_partial_starting_match(page, location_data):
    location_name = location_data['location_name']
    query = location_name[:len(location_name)/2]
    page.show_filters()
    page.clear_all_filters()
    page.search_for_location(query)
    names = page.get_column_items_text_by_header_text('Name')
    assert_that(location_name, is_in(names))

def test_filter_by_location_name_partial_non_starting_match(page, testdata):
    location_name = location_data['location_name']
    query = location_name[len(location_name)/2:]
    page.show_filters()
    page.clear_all_filters()
    page.search_for_location(query)
    names = page.get_column_items_text_by_header_text('Name')
    assert_that(location_name, is_in(names))
