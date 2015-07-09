# Tests for selecting a venue in Admin

from hamcrest import *
from adminautomation.pages import LoginPage, ChooseVenuePage, DashboardPage
import pytest
# import unittest
# from basetest import BaseTest
# from bypassqatesting.adminsession import log_session_out
from bypassqatesting.logger import get_module_logger


mlog = get_module_logger()

@pytest.fixture
def page(request, driver):
    page = ChooseVenuePage(driver)
    page.TIMEOUT_LENGTH = 5
    page.go_to_page_url()
    def fin():
        mlog.debug('Test ended at URL: '+page.url())
    request.addfinalizer(fin)
    mlog.debug('Page created at URL: '+page.url())
    return page

def test_select_venue_by_name(page, testdata):
    """@type page: ChooseVenuePage"""
    venue_name = testdata['test_choosevenue']['venue_name']
    page.select_venue_from_list_by_name(venue_name)
    page.wait_for_page_title('Dashboard - Index')
    page = DashboardPage(page.driver, skip_init=True)
    assert_that(page.CURRENT_VENUE_NAME, is_(venue_name))

def test_search_for_venue_full_match(page, testdata):
    """@type page: ChooseVenuePage"""
    venue_name = testdata['test_choosevenue']['venue_name']
    page.search_for_venue(venue_name)
    search_results = page.get_current_list_items_text()
    assert_that(search_results, has_item(venue_name))

def test_search_for_venue_partial_name_full_starting_word_match(page, testdata):
    """@type page: ChooseVenuePage"""
    venue_name = testdata['test_choosevenue']['venue_name']
    search_query = venue_name.split(' ')[0]
    page.search_for_venue(search_query)
    search_results = page.get_current_list_items_text()
    assert_that(search_results, has_item(venue_name))

def test_search_for_venue_partial_name_full_nonstarting_word_match(page, testdata):
    """@type page: ChooseVenuePage"""
    venue_name = testdata['test_choosevenue']['venue_name']
    search_query = venue_name.split(' ')[1]
    page.search_for_venue(search_query)
    search_results = page.get_current_list_items_text()
    assert_that(search_results, has_item(venue_name))

def test_search_for_venue_partial_name_partial_starting_word_match(page, testdata):
    """@type page: ChooseVenuePage"""
    venue_name = testdata['test_choosevenue']['venue_name']
    search_query = venue_name.split(' ')[0][:-1]
    page.search_for_venue(search_query)
    search_results = page.get_current_list_items_text()
    assert_that(search_results, has_item(venue_name))

def test_search_for_venue_partial_name_partial_nonstarting_word_match(page, testdata):
    """@type page: ChooseVenuePage"""
    venue_name = testdata['test_choosevenue']['venue_name']
    search_query = venue_name.split(' ')[1][:-1]
    page.search_for_venue(search_query)
    search_results = page.get_current_list_items_text()
    assert_that(search_results, has_item(venue_name))

# class ChooseVenueTest(BaseTest):
#
#     DATA_FILE = './tests/data/choosevenuetest.json'
#
#     @classmethod
#     def tearDownClass(cls):
#         session_id = cls.AUTH_COOKIE['value']
#         root_url = cls.AUTH_COOKIE['domain']
#         log_session_out(root_url, session_id)
#         super(ChooseVenueTest, cls).tearDownClass()
#
#
#     def test_select_venue_by_name(self):
#         """Select Venue by Name"""
#         # Simulates a user clicking the venues drop down box then selecting a venue by name.
#         #
#         # NEEDS TESTRAIL CASE
#
#         test_data = self.CURRENT_TEST_DATA
#
#         admin = LoginPage(self.driver)
#         admin.driver.get(admin.URL)
#         admin.attach_session_cookie()
#         admin = ChooseVenuePage(self.driver)
#         admin.driver.get(admin.URL)
#
#         admin.select_venue_from_list_by_name(test_data.venue_name)
#
#         self.assertEqual(admin.driver.title, test_data.end_page_title)
#
#     def test_search_for_venue_full_match(self):
#         """Search for a Venue - Full Match"""
#         # Simulates the user entering a query into the searchbox from the venue list dropdown.
#         #
#         # NEEDS TESTRAIL CASE
#
#         test_data = self.CURRENT_TEST_DATA
#
#         admin = LoginPage(self.driver)
#         admin.driver.get(admin.URL)
#         admin.attach_session_cookie()
#         admin = ChooseVenuePage(self.driver)
#         admin.driver.get(admin.URL)
#
#         admin.search_for_venue(test_data.search_query)
#         search_results = [item.text for item in admin.VENUE_LIST_ITEMS]
#
#         self.assertIn(test_data.search_query, search_results)
#
#     def test_search_for_venue_partial_match(self):
#         """Search for a Venue - Partial Match"""
#         # Simulates the user entering a query into the searchbox from the venue list dropdown.
#         #
#         # NEEDS TESTRAIL CASE
#
#         test_data = self.CURRENT_TEST_DATA
#
#         admin = LoginPage(self.driver)
#         admin.driver.get(admin.URL)
#         admin.attach_session_cookie()
#         admin = ChooseVenuePage(self.driver)
#         admin.driver.get(admin.URL)
#
#         admin.search_for_venue(test_data.search_query)
#         search_results = [item.text for item in admin.VENUE_LIST_ITEMS]
#
#         self.assertIn(test_data.search_target, search_results)
#
#
# if __name__ == "__main__":
#     unittest.main()
