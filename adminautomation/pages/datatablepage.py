import re
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from adminautomation.locators.datatablelocators import DataTableLocators
from adminautomation.locators.by import css
from adminautomation.structures.genericstructs import PaginationButtons


class DataTablePage(object):
    @property
    def DATATABLE(self):
        return self.get_element(DataTableLocators.DATATABLE)

    @property
    def DATATABLE_HEADERS(self):
        return self.get_elements(DataTableLocators.DATATABLE_HEADERS)

    @property
    def DATATABLE_HEADER_CHECKBOX(self):
        return self.get_element(DataTableLocators.DATATABLE_HEADER_CHECKBOX)

    @property
    def DATATABLE_FILTER_ROW(self):
        return self.get_element(DataTableLocators.DATATABLE_FILTER_ROW)

    @property
    def DATATABLE_FILTER_TOGGLE(self):
        return self.get_element(DataTableLocators.DATATABLE_FILTER_TOGGLE)

    @property
    def DATATABLE_FILTERS(self):
        return self.get_elements(DataTableLocators.DATATABLE_FILTERS)

    @property
    def DATATABLE_CLEAR_FILTERS_BUTTON(self):
        return self.get_element(DataTableLocators.DATATABLE_CLEAR_FILTERS_BUTTON)

    @property
    def DATATABLE_TABLE_ROWS(self):
        return self.get_elements(DataTableLocators.DATATABLE_TABLE_ROWS)

    @property
    def DATATABLE_FOOTER(self):
        return self.get_element(DataTableLocators.DATATABLE_FOOTER)

    @property
    def PAGINATION_BUTTONS(self):
        return PaginationButtons(DataTableLocators.PAGINATION_BUTTONS)

    @property
    def TOTAL_ITEMS_STRONG(self):
        try:
            return self.get_element(DataTableLocators.TOTAL_ITEMS_STRONG)
        except AttributeError:
            return None

    @property
    def BULK_ACTIONS_BUTTON(self):
        return self.get_element(self.locators.BULK_ACTIONS_BUTTON)

    @property
    def BULK_ACTIONS_MENU(self):
        return self.get_element(self.locators.BULK_ACTIONS_MENU)

    @property
    def BULK_ACTIONS_OPTIONS(self):
        return self.get_elements(self.locators.BULK_ACTIONS_OPTIONS)

    @property
    def ITEMS_PER_PAGE_SELECTOR(self):
        try:
            return Select(self.get_element(DataTableLocators.ITEMS_PER_PAGE_SELECTOR))
        except AttributeError:
            return None

    @property
    def total_items_count(self):
        total_items_full_text = self.TOTAL_ITEMS_STRONG.text
        if total_items_full_text is None:
            return None
        regex = re.compile('[0-9]+')
        try:
            return regex.search(total_items_full_text).group(0)
        except AttributeError:
            return None

    def get_column_by_header_text(self, header_text):
        try:
            elems = self.get_elements(DataTableLocators.DATATABLE + css('td[data-title-text="{0}"]'.format(header_text)))
        except TimeoutException:
            return []
        return elems

    def get_column_items_text_by_header_text(self, header_text):
        elems = self.DATATABLE.find_element_by_css_selector('tbody').find_elements_by_css_selector('td[data-title-text="{0}"]'.format(header_text))
        return map(lambda e: e.text, elems)

    def toggle_filters(self):
        self.DATATABLE_FILTER_TOGGLE.click()

    def show_filters(self):
        if 'ng-hide' in self.DATATABLE_FILTER_ROW.get_attribute('class').split():
            self.toggle_filters()

    def hide_filters(self):
        if 'ng-hide' not in self.DATATABLE_FILTER_ROW.get_attribute('class').split():
            self.toggle_filters()

    def get_filter_input_by_column_header_text(self, header_text):
        filter_index = map(lambda i: i.text, self.DATATABLE_HEADERS).index(header_text)
        return self.DATATABLE_FILTERS[filter_index]

    def clear_all_filters(self):
        self.show_filters()
        self.DATATABLE_CLEAR_FILTERS_BUTTON.click()

    def toggle_header_checkbox(self):
        self.DATATABLE_HEADER_CHECKBOX.click()

    def check_header_checkbox(self):
        if not self.DATATABLE_HEADER_CHECKBOX.is_selected():
            self.toggle_header_checkbox()

    def uncheck_header_checkbox(self):
        if self.DATATABLE_HEADER_CHECKBOX.is_selected():
            self.toggle_header_checkbox()

    def filter_table(self, header_text, filter_value):
        self.show_filters()
        filter_elem = self.get_filter_input_by_column_header_text(header_text)
        filter_elem.clear()
        filter_elem.send_keys(filter_value)

    def filter_rows_by_value(self, header_text, filter_value):
        elems = self.get_column_by_header_text(header_text)
        return filter(lambda i: i.text == filter_value, elems)

    def wait_for_table_load_after_filter(self):
        while True:
            try:
                map(lambda e: e.text, self.DATATABLE_TABLE_ROWS)
            except StaleElementReferenceException:
                break
        return

    def toggle_take_bulk_actions_menu(self):
        self.BULK_ACTIONS_BUTTON.click()

    def open_take_bulk_actions_menu(self):
        if not self.BULK_ACTIONS_MENU.is_displayed():
            self.toggle_take_bulk_actions_menu()

    def close_take_bulk_actions_menu(self):
        if self.BULK_ACTIONS_MENU.is_displayed():
            self.toggle_take_bulk_actions_menu()
