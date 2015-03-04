from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.select import Select

from adminautomation.utils.locators import BaseLocator


class DataTableRow(object):
    def __init__(self, row, headers, locators):
        self.row = row
        self.headers = headers
        self.locators = locators

    def __setattr__(self, key, value):
        if isinstance(value, BaseLocator):
            object.__setattr__(self, key, object.__getattribute__('row').find_element(*value))
        else:
            object.__setattr__(self, key, value)

class DropDownSelector(object):

    def __init__(self, element):
        self.element = element
        #self.TEXT =


class PaginationButtons(object):
    def __init__(self, driver, button_group_locator=('css selector', 'ul.pagination'), buttons_locator=('css selector', 'li a')):
        """A generic set of pagination buttons, usually seen at the bottom of a datatable.
        :param ele
        :param buttons_locator: The selector used to search for the individual buttons. Formated as a 2-item tuple
        containing a selector type, from the By class, and match value.
        """
        self.driver = driver
        self.button_group_locator = button_group_locator
        self.buttons_locator = buttons_locator

    @property
    def BUTTON_GROUP(self):
        return self.driver.find_element(*self.button_group_locator)

    @property
    def BUTTONS(self):
        return self.BUTTON_GROUP.find_elements(*self.buttons_locator)

    def get_last_page_button(self, last_page_button_locator=('css selector', 'a[ng-switch-when="last"]')):
        return self.BUTTON_GROUP.find_element(*last_page_button_locator)

    def get_next_page_button(self, next_page_button_locator=('css selector', 'a[ng-switch-when="next"]')):
        return self.BUTTON_GROUP.find_element(*next_page_button_locator)

    def get_previous_page_button(self, previous_page_button_locator=('css selector', 'a[ng-switch-when="prev"]')):
        return self.BUTTON_GROUP.find_element(*previous_page_button_locator)


