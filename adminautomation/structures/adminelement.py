from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from adminautomation.pages import BasePage


class AdminElement(BasePage):
    def __init__(self, page, locator):
        """
        :type locator: BaseLocator
        :return:
        """
        self.driver = page.driver if isinstance(page, BasePage) else page
        self.locator = locator
        self.elem = page.get_element(locator)

    def get_element(self, locator, **kwargs):
        self.driver, d = self.elem, self.driver
        super(AdminElement, self).get_element(locator, **kwargs)
        self.driver = d

    def get_elements(self, locator, **kwargs):
        self.driver, d = self.elem, self.driver
        super(AdminElement, self).get_elements(locator, **kwargs)
        self.driver = d
