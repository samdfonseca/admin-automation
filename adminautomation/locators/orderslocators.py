from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import css


class OrdersLocators(BaseLocatorGroup):
    RELOAD_TABLE_BUTTON = css('div.icon-refresh')
    NEW_ORDER_BUTTON = css('div.orders-buttons'
                           'div.btn:nth-child(2)')

    DATATABLE = css('table#order_list')
    DATATABLE_HEADERS = css('table#order_list '
                            'th.header')
    DATATABLE_FILTERS = css('table#order_list '
                            'th.filter')
    DATATABLE_TABLE_ROWS = css('table#order_list '
                               'tbody '
                               'tr')
    DATATABLE_ORDER_IDS = css('td[data-title-text="ID"]')
    DATATABLE_ORDER_DAILY_IDS = css('td[data-title-text="Daily ID"]')
    DATATABLE_CREATEDS = css('td[data-title-text="Created"]')
    DATATABLE_STATES = css('td[data-title-text="State"]')
    DATATABLE_LOCATIONS = css('td[data-title-text="Location"]')
    DATATABLE_TOTALS = css('td[data-title-text="Total"]')
    DATATABLE_SECTIONS = css('td[data-title-text="Section"]')
    DATATABLE_ROWS = css('td[data-title-text="Row"]')
    DATATABLE_SEATS = css('td[data-title-text="Seat"]')
    DATATABLE_NAMES = css('td[data-title-text="Name"]')
    DATATABLE_CC_LAST_FOURS = css('td[data-title-text="CC Last Four"]')
    DATATABLE_ORDER_TAKERS = css('td[data-title-text="Order Taker"]')

    DATATABLE_FOOTER = css('span.ng-table-counts')
    ITEMS_PER_PAGE_SELECTOR = css('span.ng-table-counts '
                                  'select')
    TOTAL_ITEMS_STRONG = css('span.ng-table-counts '
                             'strong')
    PAGINATION_BUTTON_GROUP = css('ul.pagination')

    LOADING_TOAST = css('div#toast-container')
