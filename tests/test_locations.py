from hamcrest import *
from tinydb import TinyDB, where
from adminautomation.pages.locations import LocationsPage
import pytest
import simplejson as json


@pytest.fixture()
def page(authenticated_driver):
    return LocationsPage(authenticated_driver)

@pytest.fixture()
def testdata(testdata):
    return testdata

get_testdata = lambda db, key: db.get(where('test_locations'))['test_locations'][key]

@pytest.mark.usefixtures('page', 'testdata')
class TestLocationIndex:
    # @classmethod
    # def setup_class(cls):
    #     cls.driver = authenticated_driver
    #     cls.testdata = testdata

    # @classmethod
    # def teardown_class(cls):
    #     cls.driver.close()
    #     cls.testdata.close()

    def test_filter_by_location_name_full_match(self):
        location_name = get_testdata(testdata(), 'location_name')
        page.show_filters()
        page.clear_all_filters()
        page.search_for_location(location_name)
        names = page.get_column_items_text_by_header_text('Name')
        assert_that(location_name, is_in(names))
    
    def test_filter_by_location_name_partial_starting_match(self, page, testdata):
        location_name = get_testdata(testdata, 'location_name')
        query = location_name[:len(location_name)/2]
        page.show_filters()
        page.clear_all_filters()
        page.search_for_location(query)
        names = page.get_column_items_text_by_header_text('Name')
        assert_that(location_name, is_in(names))
        
    def test_filter_by_location_name_partial_non_starting_match(self, page, testdata):
        location_name = get_testdata(testdata, 'location_name')
        query = location_name[len(location_name)/2:]
        page.show_filters()
        page.clear_all_filters()
        page.search_for_location(query)
        names = page.get_column_items_text_by_header_text('Name')
        assert_that(location_name, is_in(names))
