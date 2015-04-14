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

    def filter_rows_by_value(self, header_text, filter_value):
        locator = css('td[data-title-text="{0}"]'.format(header_text))
        return filter(lambda row: row.find_element(*locator).text == filter_value, self.DATATABLE_TABLE_ROWS)

