# The base test class to be inherited by all other test classes

import unittest
import os

from tests import trclient, read_session_info

from adminautomation.utils import TestCaseDataReader
from adminautomation.utils import AdminSessionCookie
from adminautomation.utils.drivers import get_chrome_driver
from adminautomation.utils.drivers import get_phantomjs_driver
from adminautomation.utils.api.auth import get_session_token


class BaseTest(unittest.TestCase):
    # Ideally this would be an Abstract Base Class but it works fine as is for now

    # AUTH_FILE = './data/auth.json'
    DATA_FILE = None
    TEST_DATA = None
    AUTH_COOKIE = None
    USE_HEADLESS_WEBDRIVER = False
    TESTRAIL_CLIENT = None
    SESSION_TOKEN = None

    @property
    def CURRENT_TEST_DATA(self):
        return self.TEST_DATA[self._testMethodName]

    @classmethod
    def setUpClass(cls):
        cls.TEST_DATA = TestCaseDataReader(cls.DATA_FILE) if cls.DATA_FILE else None
        cls.AUTH_COOKIE = AdminSessionCookie() if cls.AUTH_COOKIE is None else cls.AUTH_COOKIE
        cls.TESTRAIL_CLIENT = trclient if cls.TESTRAIL_CLIENT is None else cls.TESTRAIL_CLIENT
        cls.SESSION_INFO = read_session_info()
        cls.SESSION_TOKEN = get_session_token(user=os.environ['ADMIN_USER'], password=os.environ['ADMIN_PASSWORD']) \
            if cls.SESSION_TOKEN is None else cls.SESSION_TOKEN

    def setUp(self):
        if self.USE_HEADLESS_WEBDRIVER:
            self.driver = get_phantomjs_driver()
        else:
            self.driver = get_chrome_driver()

    def tearDown(self):
        # self.driver.save_screenshot('tests/img/{}.png'.format(self._testMethodName))
        self.driver.quit()


class BaseLoginTest(BaseTest):
    @classmethod
    def setupClass(cls):
        cls.TEST_DATA = TestCaseDataReader(cls.DATA_FILE) if cls.DATA_FILE else None
        cls.TESTRAIL_CLIENT = trclient
