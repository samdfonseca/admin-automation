from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, UnexpectedTagNameException, \
    StaleElementReferenceException

from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import *
from adminautomation.structures import AdminElement


class DropDownLocators(BaseLocatorGroup):
    DROP_DIV = css('div#select2-drop')
    DROP_MASK = css('div#select2-drop-mask')
    SEARCH_INPUT = DROP_DIV + css('input.select2-input')
    ITEMS = DROP_DIV + css('li.select2-result')
    CONTAINER_CLASS = css('.select2-container')
    SELECT = css('select')
    OPTIONS = css('option')


class Select2Exception(Exception):
    pass


class Select2(AdminElement):
    locators = DropDownLocators()

    def __init__(self, webelement):
        self.elem = webelement
        self.driver = self.elem.parent
        self.select = Select(self.get_element(self.locators.SELECT))

    @property
    def container(self):
        return self.get_element(self.locators.CONTAINER_CLASS)

    @property
    def options(self):
        return self.get_elements(self.locators.OPTIONS)

    @property
    def items(self):
        return self.get_elements(self.locators.ITEMS)

    def search(self, query):
        elem = self.get_element(self.locators.SEARCH_INPUT)
        elem.clear()
        elem.send_keys(query)

    def select_by_visible_text(self, text):
        self.select.select_by_visible_text(text)

    def select_by_value(self, value):
        self.select.select_by_value(value)

    def select_by_index(self, index):
        self.select.select_by_index(index)

    def toggle_dropdown(self):
        self.container.click()

    def open_dropdown(self):
        if 'select2-container-open' not in self.elem.get_attribute('class').split():
            self.container.click()
            self.driver.execute_script('$("#select2-drop-mask").remove();')

    def close_dropdown(self):
        if 'select2-container-open' in self.elem.get_attribute('class').split():
            self.toggle_dropdown()

