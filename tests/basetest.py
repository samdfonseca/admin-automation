import logging
import unittest

from selenium import webdriver

from adminautomation.utils import TestCaseDataReader

class BaseTest(unittest.TestCase):

    TEST_DATA = None

    def setUp(self):
        self.TEST_DATA = TestCaseDataReader(self.DATA_FILE)
        self.log = logging.getLogger("TestCaseLogger")
        self.driver = webdriver.Chrome()


    def tearDown(self):
        self.driver.close()


    def current_test_data(self, test_name):
        # Returns the data for the current test case in a dict.

        return self.TEST_DATA[test_name]

