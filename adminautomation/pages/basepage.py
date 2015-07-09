# The base page object to be inherited by all other page objects

from __future__ import print_function
from contextlib import contextmanager
from urlparse import urljoin, urlparse
from time import sleep, time
import logging

from selenium.webdriver import Remote as WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from twisted.python import log

from bypassqatesting import ModuleLogger
from bypassqatesting.adminsession import get_session_cookie
from bypassqatesting.datetimeutil import now, seconds


mlog = ModuleLogger()

class UnableToGetElementException(Exception):
    def __init__(self, locator):
        msg = """Unable to get element with locator:
                               Type: {0}
                               Locator: {1}""".format(locator[0], locator[1])
        super(UnableToGetElementException, self).__init__(msg)

class BasePage(object):

    ROOT_URL = "https://admin-integration.bypasslane.com"
    TIMEOUT_LENGTH = 10

    def __init__(self, driver, **kwargs):
        """
        Constructor for a BasePage object.

        :param driver: a webdriver object
        :return: a BasePage object
        """

        self.driver = driver
        """@type : WebDriver"""

        self.ROOT_URL = kwargs.get("root_url", self.ROOT_URL)
        p_url = '://'.join(urlparse(self.url())[:2])
        if not self.ROOT_URL.startswith(p_url):
            self.ROOT_URL = p_url
        self.URL = kwargs.get("url", urljoin(self.ROOT_URL, self.PATH))

        # if kwargs.has_key('log_file'):
        #     from twisted.python import logfile
        #     log_output = logfile.LogFile(kwargs.get('log_file', '{0}.log'.format(__file__)))
        # else:
        #     from sys import stdin
        #     log_output = stdin
        # from twisted.python import logfile
        # default_log_file = kwargs.get('log_file', '{0}.log'.format(__file__))
        # log_output = logfile.LogFile(kwargs.get('log_file', default_log_file), '.')
        # log.startLogging(log_output)

    def url(self):
        return self.driver.current_url

    def replace_cookie(self, cookie):
        self.driver.delete_cookie(name=cookie['name'])
        self.driver.add_cookie(cookie)

    def attach_session_cookie(self):
        """
        Replaces the current _bypass_admin_session cookie with a pre-authenticated one to avoid
        having to login on every test.
        """

        cookie = get_session_cookie()
        self.driver.delete_cookie(name=cookie['name'])
        self.driver.add_cookie(cookie)

    def go_to_page_url(self):
        """
        Go to the url assigned to the pages URL attribute.
        """

        mlog.debug('Going to URL: '+self.URL)
        self.driver.get(self.URL)

    def go_to_page_url_if_not_already_there(self):
        """
        Go to the url assigned to the pages URL attribute, if not already on that page.
        """

        if self.url() != self.URL:
            self.go_to_page_url()

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
        A generic element retriever method.

        :param locator: a locator tuple
        :return: a WebElement object
        :rtype: WebElement
        """

        do_wait = kwargs.pop('wait', True)
        try:
            if do_wait:
                return self.wait_for_element(locator)
            return self.driver.find_element(*locator)
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
            raise UnableToGetElementException(locator)

    def get_elements(self, locator, **kwargs):
        """
        A generic elements retriever method.

        :param locator: a locator tuple
        :return: a list of WebElement objects
        :rtype: WebElement
        """

        do_wait = kwargs.pop('wait', True)
        try:
            if do_wait:
                return self.wait_for_elements(locator)
            return self.driver.find_elements(*locator)
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
            raise UnableToGetElementException(locator)

    @contextmanager
    def wait_for(self, wait_function, *args):
        # def _wait_for(condition_function, *args, **kwargs):
        #     start = now()
        #     while now() < start + seconds(self.TIMEOUT_LENGTH):
        #         if condition_function(*args, **kwargs):
        #             return True
        #         else:
        #             self.sleep(0.1)
        #     raise TimeoutException
        yield wait_function(*args)

    @contextmanager
    def wait_for_webdriver(self, until_function, condition_function, *args):
        yield self._wait_until(until_function, condition_function, *args)

    def _wait_until(self, until_function, condition_function, *args):
        _args = ', '.join(args) if len(args) > 1 else args[0]
        mlog.debug('Starting wait (Until function: {0}, Condition function: {1}, Args: {2})'.format(until_function.__name__, condition_function.__name__, _args))
        elem = until_function(condition_function(*args))
        # elem = WebDriverWait(self.driver, timeout).until(
        #     until_function(locator)
        # )
        mlog.debug('Finished waiting')
        return elem

    @property
    def _until(self):
        return WebDriverWait(self.driver, self.TIMEOUT_LENGTH).until

    @property
    def _until_not(self):
        return WebDriverWait(self.driver, self.TIMEOUT_LENGTH).until_not

    # @contextmanager
    def wait_for_element(self, locator):
        return self._wait_until(self._until, EC.presence_of_element_located, locator)

    def wait_for_element_to_not_exist(self, locator):
        return self._wait_until(self._until_not, EC.presence_of_element_located, locator)

    def wait_for_element_invisibility(self, *args):
        return self._wait_until(self._until, EC.invisibility_of_element_located, *args)

    def wait_for_elements(self, locator):
        return self._wait_until(self._until, EC.presence_of_all_elements_located, locator)

    def wait_for_elements_to_not_exist(self, locator):
        return self._wait_until(self._until_not, EC.presence_of_all_elements_located, locator)

    def wait_for_text_in_element(self, locator, text):
        return self._wait_until(self._until, EC.text_to_be_present_in_element, locator, text)

    def wait_for_page_title(self, title):
        return self._wait_until(self._until, EC.title_is, title)

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

    # def log(self, *args, **kwargs):
    #     log.msg(*args, **kwargs)

    @staticmethod
    def sleep(seconds):
        sleep(seconds)
