#!./runtest

import unittest
from tests import BaseTest
from adminautomation.pages import LoginPage


class LoginTest(BaseTest):

    TEST_INDEX = 0
    DATA_FILE = './data/logintest.json'


    def test_root_url_unauthenticated(self):
        # Browser is redirected from the Admin app's root URL to a login URL,
        # if user does have an active session.
        #
        # https://bypassmobile.testrail.com/index.php?/cases/view/5933

        test_data = LoginTest.CURRENT_TEST_DATA

        login_page = LoginPage(self.driver, url=test_data.start_url)
        self.assertTrue(login_page.driver.current_url == test_data.end_url)


    # TODO: Figure out how to pass a pre-authenticated session to the driver
    # def test_root_url_authenticated(self):
    #     # Browser is allowed to access the Admin apps's root url, if user has
    #     # an active session stored.
    #     #
    #     # https://bypassmobile.testrail.com/index.php?/cases/view/5939
    #
    #     start_url = "https://admin-integration.bypasslane.com"
    #     end_url = "https://admin-integration.bypasslane.com"
    #
    #     login_page = LoginPage(self.driver, url=start_url)
    #     self.assertTrue(login_page.driver.current_url == end_url)


    def test_login_with_valid_credentials(self):
        # Login with valid user credentials.
        # Checks if the browser has proceeded to a certain URL.
        #
        # https://bypassmobile.testrail.com/index.php?/cases/view/5934

        test_data = LoginTest.CURRENT_TEST_DATA

        login_page = LoginPage(self.driver)
        login_page.login(test_data.user, test_data.passwd)
        self.assertTrue(login_page.driver.current_url == test_data.end_url)

    def test_login_with_invalid_credentials(self):
        # Login with invalid user credentials.
        # Checks that the user is returned to the login screen.

        test_data = LoginTest.CURRENT_TEST_DATA

        login_page = LoginPage(self.driver)
        login_page.login(test_data.user, test_data.passwd)
        self.assertTrue(login_page.driver.current_url == test_data.end_url)

    def test_invalid_login_toast(self):
        # Login with invalid user credentials.
        # Checks that the error toast is displayed.

        test_data = LoginTest.CURRENT_TEST_DATA

        login_page = LoginPage(self.driver)
        login_page.login(test_data.user, test_data.passwd)
        self.assertTrue(login_page.check_for_invalid_login_toast())


if __name__ == "__main__":
    unittest.main()
