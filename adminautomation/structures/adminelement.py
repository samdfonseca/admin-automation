from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminElement(object):
    def __init__(self, page, locator):
        """
        :type locator: BaseLocator
        :return:
        """

        self.driver = page.driver
        self.locator = locator
        self.elem = page.get_element(locator)

    def get_element(self, locator, **kwargs):
        """
        A generic element retriever method.

        :param locator: a locator tuple
        :return: a WebElement object
        """

        do_wait = kwargs.pop('wait', True)
        try:
            if do_wait:
                self.wait_for_element(locator)
            return self.driver.find_element(*locator, **kwargs)
        except (NoSuchElementException, StaleElementReferenceException):
            raise Warning('Unable to get element. (Locator: {})'.format(locator[1]))

    def get_elements(self, locator, **kwargs):
        """
        A generic elements retriever method.

        :param locator: a locator tuple
        :return: a list of WebElement objects
        """

        do_wait = kwargs.pop('wait', True)
        try:
            if do_wait:
                self.wait_for_elements(locator)
            return self.driver.find_elements(*locator, **kwargs)
        except (NoSuchElementException, StaleElementReferenceException):
            raise Warning('Unable to get elements. (Locator: {})'.format(locator[1]))

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

    def wait_for_element_visibility(self, *args):
        return self._wait_until(EC.visibility_of_element_located, *args)

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
