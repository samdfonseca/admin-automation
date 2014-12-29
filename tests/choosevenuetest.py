#!./runtest

# Tests for selecting a venue in Admin

import unittest
from tests import BaseTest
from adminautomation.pages import ChooseVenuePage


class ChooseVenueTest(BaseTest):

    DATA_FILE = './data/choosevenuetest.json'


    def test_select_venue_by_name(self):
        # Simulates a user clicking the venues drop down box then selecting a venue by name.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = ChooseVenuePage(self.driver)
        admin.select_venue_from_list_by_name(test_data.venue_name)
        admin.click_go_button()

        self.assertEqual(admin.driver.title, test_data.end_page_title)


    def test_select_venue_by_venue_id(self):
        test_data = self.CURRENT_TEST_DATA

        admin = ChooseVenuePage(self.driver)
        admin.select_venue_by_venue_id(test_data.venue_id)
        admin.click_go_button()


        self.assertEqual(admin.driver.title, test_data.end_page_title)


if __name__ == "__main__":
    unittest.main()
