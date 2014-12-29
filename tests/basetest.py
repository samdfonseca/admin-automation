# The base test class to be inherited by all other test classes

import logging
import unittest

from selenium import webdriver

from adminautomation.utils import TestCaseDataReader
from adminautomation.utils import attachAuthenticatedSessionToDriver


class BaseTest(unittest.TestCase):

    TEST_DATA = None


    @classmethod
    def setUpClass(cls):
        cls.TEST_DATA = TestCaseDataReader(cls.DATA_FILE)


    def setUp(self):

        # self.TEST_DATA = TestCaseDataReader(self.DATA_FILE)
        self.log = logging.getLogger("TestCaseLogger")
        self.driver = webdriver.Chrome()


    def tearDown(self):
        self.driver.quit()


    @property
    def CURRENT_TEST_DATA(self):
        return self.TEST_DATA[self._testMethodName]


    def attach_authenticated_session_to_driver(self, session_cookie=None, **kwargs):
        attachAuthenticatedSessionToDriver(self.driver, session_cookie, **kwargs)
