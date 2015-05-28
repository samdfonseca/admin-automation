from selenium.webdriver.remote.webelement import WebElement
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
    SELECT = CONTAINER_CLASS + css('+ select')
    OPTIONS = css('option')


class Select2Exception(Exception):
    pass


class Select2(AdminElement):
    locators = DropDownLocators()

    def __init__(self, page, locator):
        super(Select2, self).__init__(page, locator)

    @property
    def container(self):
        return self.get_element(css(str(self.locator) + str(self.locators.CONTAINER_CLASS)))

    @property
    def options(self):
        return self.get_elements(self.locator + '>' + self.locators.SELECT + self.locators.OPTIONS)

    @property
    def items(self):
        return self.get_elements(self.locators.ITEMS)

    def search(self, query):
        elem = self.get_element(self.locators.SEARCH_INPUT)
        elem.clear()
        elem.send_keys(query)

    def select_by_visible_text(self, text):
        self.open_dropdown()
        candidates = filter(lambda i: i.text == text, self.options)
        if candidates:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", candidates[0])
            self.wait_for_element_visibility(timeout=60)
            candidates[0].click()
            return
        raise NoSuchElementException("Could not locate element with visible text: %s" % text)

    def toggle_dropdown(self):
        self.container.click()

    def open_dropdown(self):
        if 'select2-container-open' not in self.elem.get_attribute('class').split():
            self.container.click()
            self.driver.execute_script('$("#select2-drop-mask").remove();')

    def close_dropdown(self):
        if 'select2-container-open' in self.elem.get_attribute('class').split():
            self.toggle_dropdown()

