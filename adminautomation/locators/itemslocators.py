from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import css


class ItemsLocators(BaseLocatorGroup):
    NEW_ITEM_BUTTON = css('div.portlet-title '
                          'div.actions '
                          'a[href="/items/new"]')
    ITEMS_SEARCHBOX = css('input[name="Search"]')

    DATATABLE = css('div#items '
                    'div.portlet-body '
                    'table.dataTable')
    DATATABLE_HEADERS = css('th.header')
    DATATABLE_TABLE_ROWS = DATATABLE + css('tbody '
                                           'tr')
    DATATABLE_FOOTER = css('span.ng-table-counts')

    ITEMS_PER_PAGE_SELECTOR = css('span.ng-table-counts '
                                  'select')
    TOTAL_ITEMS_STRONG = css('span.ng-table-counts '
                             'strong')
    PAGINATION_BUTTONS = css('ul.pagination')

    EDIT_LINK_PARTIAL_HREF = css('a[href="/items/{0}/edit"]')
    ROW_ITEM_NAME_LINK = css('td[data-title-text="Name"] '
                             'a')
