# The base test class to be inherited by all other test classes

import unittest

from os import remove as delete_file
from selenium import webdriver

from adminautomation.utils import TestCaseDataReader
from adminautomation.utils import AdminSessionCookie
from adminautomation.utils.drivers import get_chrome_driver as ChromeDriver


class BaseTest(unittest.TestCase):

    AUTH_FILE = './data/auth.json'
    DATA_FILE = None

    TEST_DATA = None


    @property
    def CURRENT_TEST_DATA(self):
        return self.TEST_DATA[self._testMethodName]


    @classmethod
    def setUpClass(cls):
        cls.TEST_DATA = TestCaseDataReader(cls.DATA_FILE) if cls.DATA_FILE else None
        cls.AUTH_COOKIE = AdminSessionCookie()


    def setUp(self):
        self.driver = ChromeDriver()


    def tearDown(self):
        self.driver.quit()

