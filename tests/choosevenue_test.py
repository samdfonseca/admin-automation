#!./runtest

# Tests for selecting a venue in Admin

import unittest
from basetest import BaseTest
from adminautomation.pages import LoginPage
from adminautomation.pages import ChooseVenuePage


class ChooseVenueTest(BaseTest):

    DATA_FILE = './tests/data/choosevenuetest.json'


    def test_select_venue_by_name(self):
        """Select Venue by Name"""
        # Simulates a user clicking the venues drop down box then selecting a venue by name.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = LoginPage(self.driver)
        admin.driver.get(admin.URL)
        admin.attach_session_cookie()
        admin = ChooseVenuePage(self.driver)
        admin.driver.get(admin.URL)

        admin.select_venue_from_list_by_name(test_data.venue_name)

        self.assertEqual(admin.driver.title, test_data.end_page_title)


    # def test_select_venue_by_venue_id(self):
    #     # NEEDS TESTRAIL CASE
    #
    #     test_data = self.CURRENT_TEST_DATA
    #
    #     admin = LoginPage(self.driver)
    #     admin.driver.get(admin.URL)
    #     admin.attach_session_cookie()
    #     admin = ChooseVenuePage(self.driver)
    #     admin.driver.get(admin.URL)
    #
    #     admin.select_venue_by_venue_id()
    #     admin.login(*self.AUTH_CREDENTIALS)
    #
    #     admin = ChooseVenuePage(self.driver)
    #     admin.select_venue_by_venue_id(test_data.venue_id)
    #
    #     self.assertEqual(admin.driver.title, test_data.end_page_title)


    def test_search_for_venue_full_match(self):
        """Search for a Venue - Full Match"""
        # Simulates the user entering a query into the searchbox from the venue list dropdown.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = LoginPage(self.driver)
        admin.driver.get(admin.URL)
        admin.attach_session_cookie()
        admin = ChooseVenuePage(self.driver)
        admin.driver.get(admin.URL)

        admin.search_for_venue(test_data.search_query)
        search_results = [item.text for item in admin.VENUE_LIST_ITEMS]

        self.assertIn(test_data.search_query, search_results)


    def test_search_for_venue_partial_match(self):
        """Search for a Venue - Partial Match"""
        # Simulates the user entering a query into the searchbox from the venue list dropdown.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = LoginPage(self.driver)
        admin.driver.get(admin.URL)
        admin.attach_session_cookie()
        admin = ChooseVenuePage(self.driver)
        admin.driver.get(admin.URL)

        admin.search_for_venue(test_data.search_query)
        search_results = [item.text for item in admin.VENUE_LIST_ITEMS]

        self.assertIn(test_data.search_target, search_results)



if __name__ == "__main__":
    unittest.main()
