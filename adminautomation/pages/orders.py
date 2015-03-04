# Page object for the Orders page

# import warnings
from adminautomation.pages import AdminPage, BasePage
from adminautomation.utils.locators import OrderLocators
from adminautomation.structures.genericstructs import PaginationButtons

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrdersPage(AdminPage, BasePage):

    PATH = "/orders"
    DATATABLE_COLUMN_MAP = {'ID': 0,
                            'Daily ID': 1,
                            'Created': 2,
                            'State': 3,
                            'Location': 4,
                            'Total': 5,
                            'Section': 6,
                            'Row': 7,
                            'Seat': 8,
                            'Name': 9,
                            'CC Last Four': 10,
                            'Order Taker': 11}

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
        return self.get_elements(OrderLocators.DATATABLE_HEADERS)

    @property
    def DATATABLE_FILTERS(self):
        return self.get_elements(OrderLocators.DATATABLE_FILTERS)

    @property
    def DATATABLE_ROWS(self):
        return self.get_elements(OrderLocators.DATATABLE_ROWS)

    @property
    def DATATABLE_ORDER_IDS(self):
        return self.get_elements(OrderLocators.DATATABLE_ROW_ORDER_ID)

    @property
    def DATATABLE_ORDER_DAILY_IDS(self):
        return self.get_elements(OrderLocators.DATATABLE_ROW_ORDER_DAILY_ID)

    @property
    def DATATABLE_CREATED(self):
        return self.get_elements(OrderLocators.DATATABLE_ROW_CREATED)

    @property
    def DATATABLE_STATES(self):
        return self.get_elements(OrderLocators.DATATABLE_ROW_STATE)

    @property
    def DATATABLE_LOCATIONS(self):
        return self.get_elements(OrderLocators.DATATABLE_ROW_LOCATION)

    @property
    def DATATABLE_TOTALS(self):
        return self.get_elements(OrderLocators.DATATABLE_ROW_TOTAL)

    @property
    def DATATABLE_SECTIONS(self):
        return self.get_elements(OrderLocators.DATATABLE_ROW_SECTION)

    @property
    def DATATABLE_ROWS(self):
        return self.get_elements(OrderLocators.DATATABLE_ROW_ROW)

    @property
    def DATATABLE_SEATS(self):
        return self.get_elements(OrderLocators.DATATABLE_ROW_SEAT)

    @property
    def DATATABLE_NAMES(self):
        return self.get_elements(OrderLocators.DATATABLE_ROW_NAME)

    @property
    def DATATABLE_CC_LAST_FOURS(self):
        return self.get_elements(OrderLocators.DATATABLE_ROW_CC_LAST_FOUR)

    @property
    def DATATABLE_ORDER_TAKERS(self):
        return self.get_elements(OrderLocators.DATATABLE_ROW_ORDER_TAKER)

    @property
    def DATATABLE_FOOTER(self):
        return self.get_element(OrderLocators.DATATABLE_FOOTER)

    @property
    def ITEMS_PER_PAGE_SELECTOR(self):
        elem = self.get_element(OrderLocators.ITEMS_PER_PAGE_SELECTOR)
        return Select(elem)

    @property
    def TOTAL_ITEMS_STRONG(self):
        return self.get_element(OrderLocators.TOTAL_ITEMS_STRONG)

    @property
    def PAGINATION_BUTTONS(self):
        return PaginationButtons(self.get_element(OrderLocators.PAGINATION_BUTTON_GROUP))

    def reload_table(self):
        self.RELOAD_TABLE_BUTTON.click()

    def open_new_order_virtual_terminal(self):
        self.NEW_ORDER_BUTTON.click()

    def change_items_per_page(self, target_option):
        self.ITEMS_PER_PAGE_SELECTOR.select_by_visible_text(str(target_option))

    def sort_by_header_ascending(self, header_text):
        header = filter(lambda elem: elem.text == str(header_text), self.DATATABLE_HEADERS)[0]
        header_class = header.get_attribute('class')
        if 'sortable' not in header_class:
            raise Exception('Column is not sortable.')

        if 'sort-desc' in header_class:
            # If header is already sorted descending, one click will switch to ascending
            header.click()
        elif 'sort-desc' not in header_class and 'sort-asc' not in header_class:
            # If header is not sorted either direction, two clicks will switch to ascending
            header.click()
            header.click()
        elif 'sort-asc' in header_class:
            # If header is already sorted ascending, do nothing
            pass

    def sort_by_header_descending(self, header_text):
        header = filter(lambda elem: elem.text == str(header_text), self.DATATABLE_HEADERS)[0]
        header_class = header.get_attribute('class')
        if 'sortable' not in header_class:
            raise Exception('Column is not sortable.')

        if 'sort-asc' in header_class:
            # If header is already sorted ascending, one click will switch to descending
            header.click()
        elif 'sort-desc' not in header_class and 'sort-asc' not in header_class:
            # If header is not sorted either direction, one click will switch to descending
            header.click()
        elif 'sort-desc' in header_class:
            # If header is already sorted descending, do nothin
            pass
        
    def select_pagination_button_by_text(self, button_text):
        self.PAGINATION_BUTTONS.get_button_by_text(button_text).click()

    def filter_by(self, column_title, filter_value):
        filter_elem = self.DATATABLE_FILTERS[self.DATATABLE_COLUMN_MAP[column_title]]
        if filter_elem.find_elements_by_tag_name('select'):
            input_elem = Select(filter_elem.find_element_by_tag_name('select')).select_by_visible_text(filter_value)
            try:
                input_elem.select_by_visible_text(filter_value)
            except NoSuchElementException:
                # warnings.warn('Filter option not available.', UserWarning)
                pass
        else:
            input_elem = filter_elem.find_element_by_tag_name('input')
            input_elem.send_keys(str(filter_value))
        # Click somewhere outside the filter to remove focus from the input
        self.PORTLET_TITLE.click()

    def get_order_id_links_by_link_text(self, order_id):
        return self.get_elements(('link text', str(order_id)))

    def get_daily_id_links_by_link_text(self, daily_id):
        return self.get_elements(('link text', str(daily_id)))

    def get_table_rows_by_order_id(self, order_id):
        return filter(lambda row: bool(row.find_elements('css selector', 'a[href="/orders/{}"]'.format(order_id))),
                      self.DATATABLE_ROWS)


