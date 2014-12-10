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


    @property
    def CURRENT_TEST_DATA(self):
        return self.TEST_DATA[self._testMethodName]
