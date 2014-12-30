# The base test class to be inherited by all other test classes

import unittest

from selenium import webdriver

from adminautomation.utils import TestCaseDataReader, TestCaseAuthReader
from adminautomation.utils import attach_auth_session_to_driver
from adminautomation.utils import AdminSessionCookie

_CHROMEDRIVER_LOCATION = '../bin/chromedriver'
_ADMIN_ROOT_URL = "https://admin-integration.bypasslane.com"
_ADMIN_ROOT_URL_PROD = "https://admin.bypassmobile.com"
_ADMIN_SESSION_COOKIE_NAME = "_bypass_admin_session"


class BaseTest(unittest.TestCase):

    AUTH_FILE = './data/auth.json'
    TEST_DATA = None
    AUTH_CREDENTIALS = None
    AUTH_COOKIE = None
    # __AUTO_AUTH = True


    @classmethod
    def setUpClass(cls):
        cls.TEST_DATA = TestCaseDataReader(cls.DATA_FILE)
        cls.AUTH_CREDENTIALS = TestCaseAuthReader(cls.AUTH_FILE)
        cls.AUTH_COOKIE = AdminSessionCookie(cls.AUTH_CREDENTIALS["user"], cls.AUTH_CREDENTIALS["passwd"],
                                             force_new_session=True)


    def setUp(self):
        #self.driver = webdriver.Remote(command_executor='http://127.0.0.1:9515',
        #                               desired_capabilities=webdriver.DesiredCapabilities.CHROME)
        self.driver = webdriver.Chrome(executable_path=_CHROMEDRIVER_LOCATION,
                                       service_args=["--verbose", "--log-path=chromedriver.log"])
        self.driver.get(_ADMIN_ROOT_URL)
        # if self.__AUTO_AUTH:
        #     self.attach_authenticated_session_to_driver(self.driver, session_cookie=self.AUTH_COOKIE)


    def tearDown(self):
        while True:
            if self.driver.get_cookie(_ADMIN_SESSION_COOKIE_NAME) is None:
                break
            self.driver.delete_cookie(_ADMIN_SESSION_COOKIE_NAME)
        self.driver.quit()


    @property
    def CURRENT_TEST_DATA(self):
        return self.TEST_DATA[self._testMethodName]


    def attach_auth_cookie(self, driver, **kwargs):
        session_cookie = kwargs.get("session_cookie", self.AUTH_COOKIE)
        attach_auth_session_to_driver(driver, session_cookie, **kwargs)
