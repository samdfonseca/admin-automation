#!./runtest

# Tests for logging into Admin

import unittest
from tests import BaseTest
from adminautomation.pages import LoginPage


class LoginTest(BaseTest):

    DATA_FILE = './tests/data/logintest.json'


    def test_root_url_unauthenticated(self):
        """Root URL Unauthenticated"""
        # Browser is redirected from the Admin root URL to a login URL,
        # if user does have an active session.

        # https://bypassmobile.testrail.com/index.php?/cases/view/5933


        test_data = self.CURRENT_TEST_DATA

        admin = LoginPage(self.driver, url=test_data.start_url)

        self.assertEqual(admin.driver.current_url, test_data.end_url)


    def test_root_url_authenticated(self):
        """Root URL Authenticated"""
        # Browser is allowed to access the Admin dashboard at the root url, if user has
        # an active session stored.
        #
        # https://bypassmobile.testrail.com/index.php?/cases/view/5939
    
        test_data = self.CURRENT_TEST_DATA
    
        admin = LoginPage(self.driver)
        admin.driver.get(admin.URL)
        admin.attach_session_cookie()
        admin.driver.get(admin.ROOT_URL)
    
        admin.driver.get(test_data.end_url)
    
        self.assertEqual(admin.driver.title, test_data.end_page_title)


    def test_login_with_valid_credentials(self):
        """Login with Valid Credentials"""
        # Login with valid user credentials.
        # Checks if the browser proceeds to the Choose Venue page.
        #
        # https://bypassmobile.testrail.com/index.php?/cases/view/5934

        test_data = self.CURRENT_TEST_DATA

        admin = LoginPage(self.driver)
        admin.login(test_data.user, test_data.passwd)

        self.assertEqual(admin.driver.current_url, test_data.end_url)


    def test_login_with_invalid_username(self):
        """Login with Invalid Username"""
        # Login with invalid username.
        # Checks that the user is returned to the login screen.
        #
        # https://bypassmobile.testrail.com/index.php?/cases/view/5935

        test_data = self.CURRENT_TEST_DATA

        admin = LoginPage(self.driver)
        admin.login(test_data.user, test_data.passwd)

        self.assertEqual(admin.driver.current_url, test_data.end_url)


    def test_login_with_invalid_password(self):
        """Login with Invalid Password"""
        # Login with invalid password.
        # Checks that the user is returned to the login screen.
        #
        # https://bypassmobile.testrail.com/index.php?/cases/view/5937

        test_data = self.CURRENT_TEST_DATA

        admin = LoginPage(self.driver)
        admin.login(test_data.user, test_data.passwd)

        self.assertEqual(admin.driver.current_url, test_data.end_url)


    def test_invalid_login_toast(self):
        """Invalid Login Toast"""
        # Login with invalid user credentials.
        # Checks that the error toast is displayed.
        #
        # https://bypassmobile.testrail.com/index.php?/cases/view/6883

        test_data = self.CURRENT_TEST_DATA

        admin = LoginPage(self.driver)
        admin.login(test_data.user, test_data.passwd)

        self.assertTrue(admin.check_for_invalid_login_toast())


    def test_login_with_all_caps_username(self):
        """Login with All Caps Username"""
        # Login with a valid username but replace all lowercase letters with capitalized ones
        # Checks if the browser proceeds to the Choose Venue page.
        #
        # https://bypassmobile.testrail.com/index.php?/cases/view/5938

        test_data = self.CURRENT_TEST_DATA

        admin = LoginPage(self.driver)
        admin.login(test_data.user, test_data.passwd)

        self.assertTrue(admin.check_for_invalid_login_toast())


if __name__ == "__main__":
    unittest.main()
