from __future__ import print_function

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class BasePage(object):
    def __init__(self, driver):
        """
        Constructor for a BasePage object.

        :param driver: a webdriver object
        :return: a BasePage object
        """

        self.driver = driver


    def get_element(self, locator, custom_message=None):
        """
        A generic element retriever function.

        :param locator: a locator tuple
        :return: a WebElement object
        """

        try:
            return self.driver.find_element(*locator)
        except (NoSuchElementException, StaleElementReferenceException):
            if isinstance(custom_message, basestring):
                print(custom_message)
            return None


    def get_elements(self, locator, custom_message=None):
        """
        A generic elements retriever function.

        :param locator: a locator tuple
        :return: a list of WebElement objects
        """

        try:
            return self.driver.find_elements(*locator)
        except (NoSuchElementException, StaleElementReferenceException):
            if isinstance(custom_message, basestring):
                print(custom_message)
            return None


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


    def is_title_match(self, custom_message):
        """
        Checks that the page title matches the expected value.

        :param custom_message: a custom message to throw if the assertion fails
        """

        found_title = self.driver.title
        self.check_value("page_title", found_title, custom_message=custom_message)
