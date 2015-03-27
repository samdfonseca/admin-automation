from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import css


class InventoryStatusLocators(BaseLocatorGroup):
    VIEW_STOCK_ITEMS_BUTTON = css('a[ui-sref="status.stock_items_list"]')

    DATATABLE = css('div#inventory-status'
                    'table')

    DATATABLE_HEADERS = css('th.header')
    DATATABLE_FILTERS_TOGGLE_BUTTON = css('i.icon-filter')
    DATATABLE_FILTERS = css('th.filter')
    DATATABLE_TABLE_ROWS = css('div#inventory-status'
                               'table'
                               'tbody'
                               'tr')
    DATATABLE_LOCATIONS = DATATABLE + ' td[data-title-text="Location"]'
    DATATABLE_STATUS = DATATABLE + ' td[data-title-text="Status"]'
    DATATABLE_LOCATION_TYPES = DATATABLE + ' td[data-title-text="Location Type"]'
    DATATABLE_CURRENT_COUNTS = DATATABLE + ' td[data-title-text="Current Count"]'
    DATATABLE_PAR_TOTAL = DATATABLE + ' td[data-title-text="PAR Totals"]'
    DATATABLE_ROW_ACTION_CELLS = DATATABLE + ' td[data-title-text=" "]'

    DATATABLE_FOOTER = css('.ng-table-counts')
    ITEMS_PER_PAGE_SELECTOR = css('.ng-table-counts'
                                  'select')
    TOTAL_ITEMS_STRONG = css('.ng-table-counts'
                             'strong')
    PAGINATION_BUTTON_GROUP = css('ul.pagination')
