# The base page object to be inherited by all other page objects

from __future__ import print_function

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from adminautomation.utils import AdminSessionCookie


class BasePage(object):

    ROOT_URL = "https://admin-integration.bypasslane.com"


    def __init__(self, driver, **kwargs):
        """
        Constructor for a BasePage object.

        :param driver: a webdriver object
        :return: a BasePage object
        """

        self.driver = driver
        self.ROOT_URL = kwargs.get("root_url", self.ROOT_URL)
        self.URL = kwargs.get("url", self.ROOT_URL + self.PATH)


    def attach_session_cookie(self):
        """
        Replaces the current _bypass_admin_session cookie with a pre-authenticated one to avoid
        having to login on every test.
        """

        self.driver.delete_cookie(name=AdminSessionCookie()['name'])
        self.driver.add_cookie(AdminSessionCookie())


    def refresh_page(self):
        """
        Refreshes the current page.

        """

        self.driver.refresh()


    def get_element(self, locator):
        """
        A generic element retriever function.

        :param locator: a locator tuple
        :return: a WebElement object
        """

        return self.driver.find_element(*locator)


    def get_elements(self, locator, custom_message=None):
        """
        A generic elements retriever function.

        :param locator: a locator tuple
        :return: a list of WebElement objects
        """

        return self.driver.find_elements(*locator)


    def check_value(self, check_value_name, found_value, custom_message=None):
        if custom_message is not None:
            displayed_message = custom_message
        else:
            displayed_message = "'{0}' is incorrect. Expected: '{1}', Found: '{2}'".format(
                check_value_name, self.CHECK_VALUES[check_value_name], found_value
            )

        try:
            assert self.CHECK_VALUES == found_value, displayed_message
        except KeyError:
            print("No expected value for {}".format(check_value_name))


    def check_exists(self, locator):
        try:
            target_item = self.get_element(locator)
        except (NoSuchElementException, StaleElementReferenceException):
            return False

        return True


    def is_title_match(self, custom_message):
        """
        Checks that the page title matches the expected value.

        :param custom_message: a custom message to throw if the assertion fails
        """

        found_title = self.driver.title
        self.check_value("page_title", found_title, custom_message=custom_message)


    # def attach_authenticated_session(self, user, passwd, **kwargs):
    #     """
    #     Replaces the _bypass_admin_session cookie with a pre-authenticated session cookie.
    #
    #     :param cookie:
    #     """
    #
    #     try:
    #         if not modules.get("AdminAuthCookie"):
    #             from adminautomation.utils import AdminAuthCookie
    #     except ImportError:
    #         pass
    #
    #     session_cookie_name = kwargs.get('session_cookie_name', '_bypass_admin_session')
    #
    #     authed_cookie = AdminAuthCookie(user, passwd, **kwargs)
    #
    #     self.driver.delete_cookie(session_cookie_name)
    #     self.driver.add_cookie(authed_cookie)

