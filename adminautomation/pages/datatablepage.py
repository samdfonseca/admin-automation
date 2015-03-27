from selenium.webdriver.support.select import Select


class DataTablePage(object):

    @property
    def DATATABLE(self):
        return self.get_element(self.locators.DATATABLE)

    @property
    def DATATABLE_HEADERS(self):
        return self.get_elements(self.locators.DATATABLE_HEADERS)

    @property
    def DATATABLE_ROWS(self):
        return self.get_elements(self.locators.DATATABLE_ROWS)

    @property
    def DATATABLE_FOOTER(self):
        return self.get_element(self.locators.DATATABLE_FOOTER)

    @property
    def PAGINATION_BUTTONS(self):
        return self.get_elements(self.locators.PAGINATION_BUTTONS)

    @property
    def ITEMS_PER_PAGE_SELECTOR(self):
        return Select(self.get_element(self.locators.ITEMS_PER_PAGE_SELECTOR))
