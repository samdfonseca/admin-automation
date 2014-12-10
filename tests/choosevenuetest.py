#!./runtest

import logging
import sys
import unittest
from tests import BaseTest
from adminautomation.pages import ChooseVenuePage


class ChooseVenueTest(BaseTest):

    DATA_FILE = './data/choosevenuetest.json'

    def test_select_venue_by_name(self):
        # Simulates a user clicking the venues drop down box then selecting a venue by name.
        #
        # NEEDS TESTRAIL CASE

        self
        choose_venue_page = ChooseVenuePage(self.driver)
        # choose_venue_page.expand_venues_listbox()
        choose_venue_page.select_venue_from_list_by_name("QA Kingdom")
        choose_venue_page.click_go_button()
        el = self.driver.find_element_by_class_name("select2-chosen")
        assert el.text == "QA Kingdom"


if __name__ == "__main__":
    unittest.main()