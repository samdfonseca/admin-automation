# The base page object to be inherited by all other page objects

from __future__ import print_function
from urlparse import urljoin
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from adminautomation.utils import AdminSessionCookie


class BasePage(object):
    # Ideally this would be an Abstract Base Class but it works fine as is for now

    ROOT_URL = "https://admin-integration.bypasslane.com"


    def __init__(self, driver, **kwargs):
        """
        Constructor for a BasePage object.

        :param driver: a webdriver object
        :return: a BasePage object
        """

        self.driver = driver
        self.driver.maximize_window()

        self.ROOT_URL = kwargs.get("root_url", self.ROOT_URL)
        self.URL = kwargs.get("url", urljoin(self.ROOT_URL, self.PATH))


    def attach_session_cookie(self):
        """
        Replaces the current _bypass_admin_session cookie with a pre-authenticated one to avoid
        having to login on every test.
        """

        cookie = AdminSessionCookie()
        self.driver.delete_cookie(name=cookie['name'])
        self.driver.add_cookie(cookie)


    def go_to_page_url(self):
        """
        Go to the url assigned to the pages URL attribute.
        """

        self.driver.get(self.URL)


    def refresh_page(self):
        """
        Refreshes the current page.

        """

        self.driver.refresh()


    def go_to_url(self, *args):
        """
        Navigates the driver to a given url. Params match urlparse.urljoin.
        :param base: The base url as a string
        :param url: The optional relative url as a string
        :param allow_fragments: Optional boolean to allow url fragments
        """
        url = urljoin(*args)
        self.driver.get(url)


    def get_element(self, locator, **kwargs):
        """
        A generic element retriever function.

        :param locator: a locator tuple
        :return: a WebElement object
        """

        try:
            self.wait_for_element(locator)
            return self.driver.find_element(*locator, **kwargs)
        except (NoSuchElementException, StaleElementReferenceException):
            raise Warning('Unable to get element. (Locator: {})'.format(locator[1]))
        return None


    def get_elements(self, locator, **kwargs):
        """
        A generic elements retriever function.

        :param locator: a locator tuple
        :return: a list of WebElement objects
        """

        try:
            self.wait_for_elements(locator)
            return self.driver.find_elements(*locator, **kwargs)
        except (NoSuchElementException, StaleElementReferenceException):
            raise Warning('Unable to get elements. (Locator: {})'.format(locator[1]))
        return None


    def _wait_until(self, until_function, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(
            until_function(locator)
        )


    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )


    def wait_for_element_to_not_exist(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until_not(
            EC.presence_of_element_located(locator)
        )


    def wait_for_element_invisibility(self, *args):
        return self._wait_until(EC.invisibility_of_element_located, *args)


    def wait_for_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )


    def wait_for_elements_to_not_exist(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until_not(
            EC.presence_of_all_elements_located(locator)
        )


    def wait_for_text_in_element(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )


    def wait_for_page_title(self, title, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.title_is(title)
        )


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


    def check_element_exists(self, locator):
        try:
            target_item = self.get_element(locator)
        except (NoSuchElementException, StaleElementReferenceException):
            return False

        return True


    def check_elements_exist(self, locator):
        try:
            target_item = self.get_elements(locator)
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


    @staticmethod
    def sleep(seconds):
        sleep(seconds)


