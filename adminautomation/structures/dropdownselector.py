from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, UnexpectedTagNameException

from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import *


class DropDownLocators(BaseLocatorGroup):
    DROP_DIV = css('div#select2-drop')
    DROP_MASK = css('div#select2-drop-mask')
    SEARCH_INPUT = DROP_DIV + css('input.select2-input')
    ITEMS = DROP_DIV + css('li.select2-result')

class Select2(object):
    locators = DropDownLocators

    def __init__(self, webelement):
        if webelement.tag_name() != 'div' and 'select2-container' not in webelement.get_attribute('class').split():
            raise UnexpectedTabNameException('Select2 only work on <div class="select2-container"> elements, not on {0}'.format(webelement.tag_name))
        self._elem = webelement
        self._drop = webelement.parent.find_element(self.locators.DROP_DIV)

    @property
    def options(self):
        return self._drop.find_elements(*DropDownLocators.ITEMS)

    def search(self, query):
        elem = self._elem.find_element(*DropDownLocators.SEARCH_INPUT)
        elem.clear()
        elem.send_keys(query)

    def select_by_visible_text(self, text):
        self.open_dropdown()
        candidates = filter(lambda i: i.text == text, self.dropdown.options)
        if candidates:
            candidates[0].click()
            return
        raise NoSuchElementException("Could not locate element with visible text: %s" % text)

    def toggle_dropdown(self):
        self.field.click()

    def open_dropdown(self):
        if 'select2-container-open' not in self.dropdown._el.get_attribute('class').split():
            self.toggle_dropdown()

    def close_dropdown(self):
        if 'select2-container-open' in self.dropdown._el.get_attribute('class').split():
            self.toggle_dropdown()

