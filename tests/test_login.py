# Tests for logging into Admin
# https://bypassmobile.testrail.com/index.php?/suites/view/19&group_id=742

from hamcrest import *
from tinydb import where
from adminautomation.pages import LoginPage
import pytest
from bypassqatesting.logger import get_module_logger


mlog = get_module_logger()

@pytest.fixture
def page(driver):
    return LoginPage(driver)


def setup_module(module):
    mlog.debug('Switching to prod')
    mlog.debug(dir(module.pytest))
    # module.globals testdata.update({'baseurl':'https://admin.bypassmobile.com'})
    
def test_root_url_unauthenticated(page):
    assert_that(page.url, has_string(ends_with(page.PATH)))

def test_root_url_authenticated(authenticated_driver, testdata):
    base_url = testdata['baseurl']
    authenticated_driver.get(base_url)
    assert_that(authenticated_driver.current_url, has_string(base_url))

def test_login_non_superuser(page, testdata):
    base_url = testdata['baseurl']
    user = testdata['test_login']['normaluser']
    password = testdata['test_login']['normalpassword']
    page.login(user, password)
    assert_that(page.url, is_(base_url))

def test_login_superuser(page, testdata):
    login_data = testdata['test_login']
    base_url = testdata['baseurl']
    user = login_data['superuser']
    password = login_data['superpassword']
    page.login(user, password)
    assert_that(page.url, is_(base_url+'admin_sessions/choose_venue'))

def test_login_invalid_user(page, testdata):
    login_data = testdata['test_login']
    base_url = testdata.get(where('baseurl'))['baseurl']
    user = login_data['baduser']
    password = login_data['badpassword']
    page.login(user, password)
    assert_that(page.url, is_(base_url+'admin_sessions/new'))

def test_login_no_credentials(page):
    page.click_login_button()
    assert_that(page.url, has_string(ends_with('admin_sessions/new')))

def test_login_caps_username(page, testdata):
    login_data = testdata['test_login']
    base_url = testdata['baseurl']
    user = login_data['normaluser'].upper()
    password = login_data['normalpassword']
    page.login(user, password)
    assert_that(page.url, is_(base_url))

def test_invalid_login_error_message(page):
    page.click_login_button()
    assert_that(page.check_for_invalid_login_toast(), is_(True))


# class LoginTest(BaseLoginTest):
#
#     DATA_FILE = './tests/data/logintest.json'
#
#     def test_root_url_unauthenticated(self, testdata):
#         """Root URL Unauthenticated - 5933"""
#         # Browser is redirected from the Admin root URL to a login URL,
#         # if user does have an active session.
#         #
#         # https://bypassmobile.testrail.com/index.php?/cases/view/5933
#
#         test_case_id = 5933
#         # test_data = self.CURRENT_TEST_DATA
#
#         admin = LoginPage(self.driver)
#         # admin = LoginPage(self.driver, url=test_data.start_url)
#
#         url = testdata.get(where('baseurl'))['baseurl']
#         assert_that(admin.driver.current_url, is_(url))
#         # assert_that(admin.driver.current_url, is_(''.join([self.get_test_data('baseurl'), admin.PATH])))
#         # self.assertEqual(admin.driver.current_url, test_data.end_url)
#
#     def test_root_url_authenticated(self):
#         """Root URL Authenticated - 5939"""
#         # Browser is allowed to access the Admin dashboard at the root url, if user has
#         # an active session stored.
#         #
#         # https://bypassmobile.testrail.com/index.php?/cases/view/5939
#
#         test_case_id = 5939
#         test_data = self.CURRENT_TEST_DATA
#     
#         admin = LoginPage(self.driver)
#         admin.driver.get(admin.URL)
#         admin.attach_session_cookie()
#         admin.driver.get(admin.ROOT_URL)
#     
#         admin.driver.get(test_data.end_url)
#
#         self.assertEqual(admin.driver.title, test_data.end_page_title)
#
#     def test_login_with_valid_credentials(self):
#         """Login with Valid Credentials - 5934"""
#         # Login with valid user credentials.
#         # Checks if the browser proceeds to the Choose Venue page.
#         #
#         # https://bypassmobile.testrail.com/index.php?/cases/view/5934
#
#         test_case_id = 5934
#         test_data = self.CURRENT_TEST_DATA
#
#         admin = LoginPage(self.driver)
#         admin.login(test_data.user, test_data.passwd)
#
#         self.assertEqual(admin.driver.current_url, test_data.end_url)
#
#     def test_login_with_invalid_username(self):
#         """Login with Invalid Username - 5935"""
#         # Login with invalid username.
#         # Checks that the user is returned to the login screen.
#         #
#         # https://bypassmobile.testrail.com/index.php?/cases/view/5935
#
#         test_case_id = 5935
#         test_data = self.CURRENT_TEST_DATA
#
#         admin = LoginPage(self.driver)
#         admin.login(test_data.user, test_data.passwd)
#
#         self.assertEqual(admin.driver.current_url, test_data.end_url)
#
#     def test_login_with_invalid_password(self):
#         """Login with Invalid Password - 5937"""
#         # Login with invalid password.
#         # Checks that the user is returned to the login screen.
#         #
#         # https://bypassmobile.testrail.com/index.php?/cases/view/5937
#
#         test_case_id = 5937
#         test_data = self.CURRENT_TEST_DATA
#
#         admin = LoginPage(self.driver)
#         admin.login(test_data.user, test_data.passwd)
#
#         self.assertEqual(admin.driver.current_url, test_data.end_url)
#
#     def test_invalid_login_toast(self):
#         """Invalid Login Toast - 6883"""
#         # Login with invalid user credentials.
#         # Checks that the error toast is displayed.
#         #
#         # https://bypassmobile.testrail.com/index.php?/cases/view/6883
#
#         test_case_id = 6883
#         test_data = self.CURRENT_TEST_DATA
#
#         admin = LoginPage(self.driver)
#         admin.login(test_data.user, test_data.passwd)
#         admin.sleep(1)
#
#         self.assertTrue(admin.check_for_invalid_login_toast())
#
#     def test_login_with_all_caps_username(self):
#         """Login with All Caps Username - 5938"""
#         # Login with a valid username but replace all lowercase letters with capitalized ones
#         # Checks if the browser proceeds to the Choose Venue page.
#         #
#         # https://bypassmobile.testrail.com/index.php?/cases/view/5938
#
#         test_case_id = 5938
#         test_data = self.CURRENT_TEST_DATA
#
#         admin = LoginPage(self.driver)
#         admin.login(test_data.user, test_data.passwd)
#
#         self.assertEqual(admin.driver.current_url, test_data.end_url)
#
#     def test_login_with_no_credentials(self):
#         """Login with Empty Credentials - 8198"""
#         # Attempt to login without entering any credentials
#         #
#         # https://bypassmobile.testrail.com/index.php?/cases/view/8198
#
#         test_case_id = 8198
#         test_data = self.CURRENT_TEST_DATA
#
#         admin = LoginPage(self.driver)
#         admin.login("", "")
#
#         self.assertEqual(admin.driver.current_url, test_data.end_url)
#
#
# if __name__ == "__main__":
#     unittest.main()
