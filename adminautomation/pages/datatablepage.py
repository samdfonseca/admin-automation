import re
from selenium.webdriver.support.select import Select
from adminautomation.locators.by import css
from adminautomation.structures.genericstructs import PaginationButtons


class DataTablePage(object):
    @property
    def DATATABLE(self):
        return self.get_element(self.locators.DATATABLE)

    @property
    def DATATABLE_HEADERS(self):
        return self.get_elements(self.locators.DATATABLE_HEADERS)

    @property
    def DATATABLE_HEADER_CHECKBOX(self):
        return self.get_element(self.locators.DATATABLE_HEADER_CHECKBOX)

    @property
    def DATATABLE_FILTER_ROW(self):
        return self.get_element(self.locators.DATATABLE_FILTER_ROW)

    @property
    def DATATABLE_FILTER_TOGGLE(self):
        return self.get_element(self.locators.DATATABLE_FILTER_TOGGLE)

    @property
    def DATATABLE_FILTERS(self):
        return self.get_elements(self.locators.DATATABLE_FILTERS)

    @property
    def DATATABLE_CLEAR_FILTERS_BUTTON(self):
        return self.get_element(self.locators.DATATABLE_CLEAR_FILTERS_BUTTON)

    @property
    def DATATABLE_TABLE_ROWS(self):
        return self.get_elements(self.locators.DATATABLE_TABLE_ROWS)

    @property
    def DATATABLE_FOOTER(self):
        return self.get_element(self.locators.DATATABLE_FOOTER)

    @property
    def PAGINATION_BUTTONS(self):
        return PaginationButtons(self.locators.PAGINATION_BUTTONS)

    @property
    def TOTAL_ITEMS_STRONG(self):
        try:
            return self.get_element(self.locators.TOTAL_ITEMS_STRONG)
        except AttributeError:
            return None

    @property
    def ITEMS_PER_PAGE_SELECTOR(self):
        try:
            return Select(self.get_element(self.locators.ITEMS_PER_PAGE_SELECTOR))
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
        return self.get_elements(self.locators.DATATABLE + css('td[data-title-text="{0}"]'.format(header_text)))

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
        return self.DATATABLE_FILTERS[filter_index - 1]

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
        locator = css('td[data-title-text="{0}"]'.format(header_text))
        return filter(lambda row: row.find_element(*locator).text == filter_value, self.DATATABLE_TABLE_ROWS)

