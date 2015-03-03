#

from adminautomation.pages import AdminPage, BasePage
from adminautomation.utils.locators import OrderLocators

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert


class OrdersPage(AdminPage, BasePage):

    PATH = "/orders"

    @property
    def RELOAD_TABLE_BUTTON(self):
        return self.get_element(OrderLocators.RELOAD_TABLE_BUTTON)

    @property
    def NEW_ORDER_BUTTON(self):
        return self.get_element(OrderLocators.NEW_ORDER_BUTTON)

    @property
    def DATATABLE(self):
        return self.get_element(OrderLocators.DATATABLE)

    @property
    def DATATABLE_HEADERS(self):
        return self.get_element(OrderLocators.DATATABLE_HEADERS)

    @property
    def DATATABLE_FILTERS(self):
        return self.get_element(OrderLocators.DATATABLE_FILTERS)

    @property
    def DATATABLE_ROWS(self):
        return self.get_element(OrderLocators.DATATABLE_ROWS)

    @property
    def DATATABLE_ROW_ORDER_ID(self):
        return self.get_element(OrderLocators.DATATABLE_ROW_ORDER_ID)

    @property
    def DATATABLE_ROW_ORDER_DAILY_ID(self):
        return self.get_element(OrderLocators.DATATABLE_ROW_ORDER_DAILY_ID)

    @property
    def DATATABLE_ROW_CREATED(self):
        return self.get_element(OrderLocators.DATATABLE_ROW_CREATED)

    @property
    def DATATABLE_ROW_STATE(self):
        return self.get_element(OrderLocators.DATATABLE_ROW_STATE)

    @property
    def DATATABLE_ROW_LOCATION(self):
        return self.get_element(OrderLocators.DATATABLE_ROW_LOCATION)

    @property
    def DATATABLE_ROW_TOTAL(self):
        return self.get_element(OrderLocators.DATATABLE_ROW_TOTAL)

    @property
    def DATATABLE_ROW_SECTION(self):
        return self.get_element(OrderLocators.DATATABLE_ROW_SECTION)

    @property
    def DATATABLE_ROW_ROW(self):
        return self.get_element(OrderLocators.DATATABLE_ROW_ROW)

    @property
    def DATATABLE_ROW_SEAT(self):
        return self.get_element(OrderLocators.DATATABLE_ROW_SEAT)

    @property
    def DATATABLE_ROW_NAME(self):
        return self.get_element(OrderLocators.DATATABLE_ROW_NAME)

    @property
    def DATATABLE_ROW_CC_LAST_FOUR(self):
        return self.get_element(OrderLocators.DATATABLE_ROW_CC_LAST_FOUR)

    @property
    def DATATABLE_ROW_ORDER_TAKER(self):
        return self.get_element(OrderLocators.DATATABLE_ROW_ORDER_TAKER)

    @property
    def DATATABLE_FOOTER(self):
        return self.get_element(OrderLocators.DATATABLE_FOOTER)

    @property
    def ITEMS_PER_PAGE_SELECTOR(self):
        return self.get_element(OrderLocators.ITEMS_PER_PAGE_SELECTOR)

    @property
    def TOTAL_ITEMS_STRONG(self):
        return self.get_element(OrderLocators.TOTAL_ITEMS_STRONG)

    @property
    def PAGINATION_BUTTONS(self):
        return self.get_element(OrderLocators.PAGINATION_BUTTONS)

