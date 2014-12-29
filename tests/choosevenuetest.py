#!./runtest

# Tests for selecting a venue in Admin

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

        test_data = self.CURRENT_TEST_DATA

        admin = ChooseVenuePage


if __name__ == "__main__":
    unittest.main()
