from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import css


class DataTableLocators(BaseLocatorGroup):
    BULK_ACTIONS_BUTTON = css('button.bulk-actions-btn')
    BULK_ACTIONS_MENU = css('ul#bulk-actions-menu')
    BULK_ACTIONS_OPTIONS = BULK_ACTIONS_MENU + 'li'

    DATATABLE = css('div.portlet-body '
                    'table')
    DATATABLE_HEADERS = DATATABLE + css('th.header')
    DATATABLE_HEADER_CHECKBOX = DATATABLE + css('input[type="checkbox"]')
    DATATABLE_FILTER_TOGGLE = DATATABLE + css('button.filter')
    DATATABLE_FILTER_ROW = DATATABLE + css('tr.ng-table-filters')
    DATATABLE_FILTERS = DATATABLE + css('thead:nth-of-type(1) th.filter')
    DATATABLE_CLEAR_FILTERS_BUTTON = DATATABLE_FILTER_ROW + css('button.filter')

    DATATABLE_TABLE_ROWS = DATATABLE + css('tbody '
                                           'tr')
    DATATABLE_FOOTER = css('span.ng-table-counts')

    ITEMS_PER_PAGE_SELECTOR = css('span.ng-table-counts '
                                  'select')
    TOTAL_ITEMS_STRONG = css('span.ng-table-counts '
                             'strong')
    PAGINATION_BUTTONS = css('ul.pagination')

    CHECKBOX_PARTIAL_TRACKED_ID = css('input[tracked-id="{0}"]')
    EDIT_LINK_PARTIAL_HREF = css('a[href="#/{0}/{1}/edit"]')

