# The base test class to be inherited by all other test classes

import unittest

from selenium import webdriver

from adminautomation.utils import TestCaseDataReader
from adminautomation.utils import AdminSessionCookie
from adminautomation.utils.drivers import get_chrome_driver as ChromeDriver
from adminautomation.utils.drivers import get_phantomjs_driver as PhantomJSDriver


class BaseTest(unittest.TestCase):
    # Ideally this would be an Abstract Base Class but it works fine as is for now

    # AUTH_FILE = './data/auth.json'
    DATA_FILE = None
    TEST_DATA = None
    USE_HEADLESS_WEBDRIVER = False


    @property
    def CURRENT_TEST_DATA(self):
        return self.TEST_DATA[self._testMethodName]


    @classmethod
    def setUpClass(cls):
        cls.TEST_DATA = TestCaseDataReader(cls.DATA_FILE) if cls.DATA_FILE else None
        cls.AUTH_COOKIE = AdminSessionCookie()


    def setUp(self):
        if self.USE_HEADLESS_WEBDRIVER:
            self.driver = PhantomJSDriver()
        else:
            self.driver = ChromeDriver()


    def tearDown(self):
        # self.driver.save_screenshot('tests/img/{}.png'.format(self._testMethodName))
        self.driver.quit()

