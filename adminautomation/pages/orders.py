# Page object for the Orders page

# import warnings
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

from adminautomation.pages import AdminPage, BasePage
from adminautomation.locators import OrdersLocators
from adminautomation.structures.genericstructs import PaginationButtons


class OrdersPage(AdminPage, BasePage):

    PATH = "/orders"
    locators = OrdersLocators

    @property
    def RELOAD_TABLE_BUTTON(self):
        return self.get_element(self.locators.RELOAD_TABLE_BUTTON)

    @property
    def NEW_ORDER_BUTTON(self):
        return self.get_element(self.locators.NEW_ORDER_BUTTON)

    @property
    def DATATABLE(self):
        return self.get_element(self.locators.DATATABLE)

    @property
    def DATATABLE_HEADERS(self):
        return self.get_elements(self.locators.DATATABLE_HEADERS)

    @property
    def DATATABLE_FILTERS(self):
        return self.get_elements(self.locators.DATATABLE_FILTERS)

    @property
    def DATATABLE_TABLE_ROWS(self):
        return self.get_elements(self.locators.DATATABLE_TABLE_ROWS)

    @property
    def DATATABLE_ORDER_IDS(self):
        return self.get_elements(self.locators.DATATABLE_ORDER_IDS)

    @property
    def DATATABLE_ORDER_DAILY_IDS(self):
        return self.get_elements(self.locators.DATATABLE_ORDER_DAILY_IDS)

    @property
    def DATATABLE_CREATEDS(self):
        return self.get_elements(self.locators.DATATABLE_CREATEDS)

    @property
    def DATATABLE_STATES(self):
        return self.get_elements(self.locators.DATATABLE_STATES)

    @property
    def DATATABLE_LOCATIONS(self):
        return self.get_elements(self.locators.DATATABLE_LOCATIONS)

    @property
    def DATATABLE_TOTALS(self):
        return self.get_elements(self.locators.DATATABLE_TOTALS)

    @property
    def DATATABLE_SECTIONS(self):
        return self.get_elements(self.locators.DATATABLE_SECTIONS)

    @property
    def DATATABLE_ROWS(self):
        return self.get_elements(self.locators.DATATABLE_ROWS)

    @property
    def DATATABLE_SEATS(self):
        return self.get_elements(self.locators.DATATABLE_SEATS)

    @property
    def DATATABLE_NAMES(self):
        return self.get_elements(self.locators.DATATABLE_NAMES)

    @property
    def DATATABLE_CC_LAST_FOURS(self):
        return self.get_elements(self.locators.DATATABLE_CC_LAST_FOURS)

    @property
    def DATATABLE_ORDER_TAKERS(self):
        return self.get_elements(self.locators.DATATABLE_ORDER_TAKERS)

    @property
    def DATATABLE_FOOTER(self):
        return self.get_element(self.locators.DATATABLE_FOOTER)

    @property
    def ITEMS_PER_PAGE_SELECTOR(self):
        elem = self.get_element(self.locators.ITEMS_PER_PAGE_SELECTOR)
        return Select(elem)

    @property
    def TOTAL_ITEMS_STRONG(self):
        return self.get_element(self.locators.TOTAL_ITEMS_STRONG)

    @property
    def PAGINATION_BUTTONS(self):
        return PaginationButtons(self.get_element(self.locators.PAGINATION_BUTTON_GROUP))

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
        datatable_column_map = map(lambda header: header.text, self.DATATABLE_HEADERS)
        filter_elem = self.DATATABLE_FILTERS[datatable_column_map.index(column_title)]
        input_elem = filter_elem.find_elements('css selector', 'input,select')[0]
        if input_elem.tag_name == 'select':
            try:
                Select(input_elem).select_by_visible_text(filter_value)
            except NoSuchElementException:
                pass
        else:
            input_elem.send_keys(str(filter_value))
        self.PORTLET_TITLE.click()  # Click somewhere outside the filter to remove focus from the input

    def get_order_id_links_by_link_text(self, order_id):
        return self.get_elements(('link text', str(order_id)))

    def get_daily_id_links_by_link_text(self, daily_id):
        return self.get_elements(('link text', str(daily_id)))

    def get_table_rows_by_order_id(self, order_id):
        return filter(lambda row: bool(row.find_elements('css selector', 'a[href="/orders/{}"]'.format(order_id))),
                      self.DATATABLE_ROWS)


