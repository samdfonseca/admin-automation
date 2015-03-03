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
