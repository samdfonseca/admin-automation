# Locator BaseLocators used by the webdriver to find page elements
# For info on CSS Selectors see:
# https://saucelabs.com/resources/selenium/css-selectors
# http://www.w3.org/TR/CSS21/selector.html
# https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Getting_started/Selectors

from selenium.webdriver.common.by import By
from adminautomation.locators.by import css


class BaseLocatorGroup(object):
    pass


class LoginPageLocators(BaseLocatorGroup):
    EMAIL_TEXTBOX = css('input#user_email')
    PASSWORD_TEXTBOX = css('input#user_password')
    LOGIN_BUTTON = css('button.btn')
    FORM_TITLE = css('h3.form-title')
    INVALID_LOGIN_TOAST = css('div#toast-container')
    INVALID_LOGIN_TOAST_MESSAGE = css('div.toast-message')


class ChooseVenueLocators(BaseLocatorGroup):
    VENUES_LISTBOX = css('div#s2id_change_venue')
    VENUE_LIST_SEARCHBOX = css('input.select2-input')
    VENUE_LIST = css('ul.select2-results')
    VENUE_LIST_ITEMS = css('li.select2-result')
    VENUE_OPTIONS = css('select#change_venue option')
    GO_BUTTON = css('button.btn')
    FORM_TITLE = css('h3.form-title')


class NavBarLocators(BaseLocatorGroup):
    LOGO_HOME_BUTTON = css('a.navbar-brand[href="/"]')

    VENUES_LISTBOX = css('div#s2id_change_venue')
    VENUE_LIST_DROPDOWN = css('div#select2-drop')
    VENUE_LIST_SEARCHBOX = css('input.select2-input')
    VENUE_LIST = css('ul.select2-results')
    VENUE_LIST_ITEMS = css('li.select2-result')
    CURRENT_VENUE_ITEM = css('span.select2-chosen')

    PUSH_UPDATES_NOTIFICATION = css('li#push-menus span.notification')
    PUSH_UPDATES_BUTTON = css('a[href="/menu_push"]')

    LOGOUT_BUTTON = css('a[href="/admin_sessions"]')


class SidebarLocators(BaseLocatorGroup):
    DASHBOARD = css('li.dashboard')

    LOCATION_CONTROL = css('li.locations')
    CATEGORIES = css('li.categories')
    ITEM_CATEGORIES = css('li.locations li.categories a[href="/categories"]')
    MODIFIER_CATEGORIES = css('li.locations li.categories a[href="/modifier_categories"]')
    GROUPS = css('li.locations a[href="/groups"]')
    ITEMS = css('li.locations a[href="/items"]')
    MENUS = css('li.locations a[href="/menus"]')
    LOCATIONS = css('li.locations a[href="/locations"]')
    SECTIONS = css('li.locations a[href="/sections"]')
    TABLES = css('li.locations a[href="/tables"]')
    VARIANT_SETS = css('li.locations a[href="/option_types"]')
    MODIFIERS = css('li.locations a[href="/modifiers"]')
    ADDON_GROUPS = css('li.locations a[href="/addon_groups"]')

    SUITES = css('li.suites')
    SUITES_ACCOUNTS = css('li.suites a[href="/suite_accounts"]')
    SUITES_SETUP = css('li.suites a[href="/suites"]')
    SUITES_PREORDER = css('li.suites a[href="/pre_orders"]')

    EVENTS = css('li.events')
    EVENTS_CALENDAR = css('li.events a[href="/events"]')
    EVENTS_TEMPLATES = css('li.events a[href="/event_templates"]')
    ORDERS = css('li.events a[href="/orders"]')
    TIPS = css('li.events a[href="/tips"]')
    CASHROOM = css('li.events a[href="/cashroom"]')

    INVENTORY = css('li.inventory')
    STATUS = css('li.inventory a[href="/inventory"]')
    INVENTORY_CATEGORIES = css('li.inventory a[href="/inventory_categories"]')
    INVENTORY_TRANSFERS = css('li.inventory a[href="/inventory_transfers"]')
    INVENTORY_MOVEMENTS = css('li.inventory a[href="/inventory_movements"]')
    STANDSHEETS = css('li.inventory a[href="/standsheets"]')
    STOCK_ITEMS = css('li.inventory a[href="/stock_items"]')
    RECIPES = css('li.inventory a[href="/recipes"]')
    VENDORS = css('li.inventory a[href="/vendors"]')
    INVENTORY_AUDITS = css('li.inventory a[href="/inventory_audits"]')
    PURCHASE_AND_RECEIVING = css('li.inventory a[href="/purchase_orders"]')
    WAREHOUSES = css('li.inventory a[href="/warehouses"]')

    REPORTING = css('li.reports')
    REPORTS = css('li.reports a[href="/reports"]')
    REPORT_TEMPLATES = css('li.reports a[href="/report_templates"]')

    ORDER_TAKERS = css('li.order-takers')
    DEVICES = css('li.terminals')
    ALERTS = css('li.alerts')

    BUCKS = css('li.bucks')
    BUCKS_CARD_SEARCH = css('li.bucks a[href="/bucks#/"]')
    BUCKS_ADD_NEW_CARD = css('li.bucks a[href="/bucks#/add_card"]')
    BUCKS_ALLOCATE_CARDS = css('li.bucks a[href="/bucks#/allocate"]')
    BUCKS_IMPORT_EXPORT = css('li.bucks a[href="/bucks#/import"]')


class AdminPageLocators(BaseLocatorGroup):
    PAGE_TITLE = css('h3.page-title')
    BREADCRUMB_LINKS = css('ul.breadcrumb a')
    PORTLET_TITLE = css('div.portlet-title div.caption')


class SuiteAccountsLocators(BaseLocatorGroup):
    NEW_SUITE_ACCOUNT_BUTTON = css('a.new-suite-account')
    ITEMS_PER_PAGE_SELECTOR = css('select[name="suite-accounts-list_length"]')
    ITEMS_PER_PAGE_OPTIONS = css('select[name="suite-accounts-list_length"] option')
    SUITE_ACCOUNTS_SEARCHBOX = css('div#suite-accounts-list_filter input[type="search"]')

    DATATABLE = css('table#suite-accounts-list')
    DATATABLE_HEADERS = css('table#suite-accounts-list thead td')
    # Remove unused selectors
    # DATATABLE_ACCOUNT_NAME_HEADER = css('table#suite-accounts-list thead td:contains("Account Name")')
    # DATATABLE_SUITE_HEADER = css('table#suite-accounts-list thead td:contains("Suite")')
    # DATATABLE_SUITE_HOLDER_HEADER = css('table#suite-accounts-list thead td:contains("Suite Holder")')
    # DATATABLE_PHONE_HEADER = css('table#suite-accounts-list thead td:contains("Phone")')
    # DATATABLE_EMAIL_HEADER = css('table#suite-accounts-list thead td:contains("Email")')
    # DATATABLE_EDIT_HEADER = css('table#suite-accounts-list thead td:contains("Edit")')
    DATATABLE_ROWS = css('table#suite-accounts-list tbody tr')
    DATATABLE_ROW_ACCOUNT_NAME = css('td:nth-of-type(1)')
    DATATABLE_ROW_SUITE = css('td:nth-of-type(2)')
    DATATABLE_ROW_SUITE_HOLDER = css('td:nth-of-type(3)')
    DATATABLE_ROW_PHONE = css('td:nth-of-type(4)')
    DATATABLE_ROW_EMAIL = css('td:nth-of-type(5)')
    DATATABLE_ROW_EDIT = css('td:nth-of-type(6) a.edit')
    DATATABLE_ROW_DELETE = css('td:nth-of-type(6) a.destroy')

    DATATABLE_FOOTER = css('div#suite-accounts-list_info')
    PAGINATION_BUTTONS = css('.pagination'
                             'li')


class ModifySuiteAccountLocators(BaseLocatorGroup):
    PORTLET_TITLE = css('div.portlet-title '
                        'div.caption')
    FORM = css('div#suite-account')
    CANCEL_BUTTON = css('a#cancel')
    SAVE_BUTTON = css('div#save')

    SUITE_ACCOUNT_NAME_INPUT = css('input[ng-model="suite_account.name"]')
    SUITE_TYPE_INPUT = css('input[ng-model="suite_account.suite_type"]')
    BILLING_ADDRESS_INPUT = css('textarea[ng-model="suite_account.address"]')
    NOTES_INPUT = css('textarea[ng-model="suite_account.notes"]')

    SUITE_INPUT_LABEL = (By.XPATH, '//div[@id="suite-account"]//form//label[text()="Suite"]')
    SUITE_INPUT = css('div#suite-account '
                      'form div.form-group:nth-of-type(3) '
                      'a.select2-choice')
    SUITE_SELECTOR = css('select[ng-model="suite_account.suite_id"]')
    SUITE_DROPDOWN = css('body '
                         '> div#select2-drop')
    SUITE_DROPDOWN_SEARCHBOX = css('body '
                                   '> div#select2-drop '
                                   '> div.select2-search '
                                   '> input')
    SUITE_DROPDOWN_ITEMS = css('body '
                               '> div#select2-drop '
                               'ul.select2-results '
                               'div.select2-result-label')

    SUITE_HOLDER_LABEL = css('div.suite-holder'
                             'h4')
    SUITE_HOLDER_NEW_CUSTOMER_BUTTON = css('div.suite-holder > '
                                           'div[ng-hide="suite_account.suite_holder"] '
                                           '> button')
    SUITE_HOLDER_INPUT = css('div.suite-holder '
                             'a.select2-choice')
    SUITE_HOLDER_SELECTOR = css('div.suite-holder '
                                'span[ng-show="suiteOwners"] '
                                'select[ng-model="suite_account.suite_holder"]')
    SUITE_HOLDER_DROPDOWN = css('body '
                                '> div#select2-drop')
    SUITE_HOLDER_DROPDOWN_SEARCHBOX = css('body '
                                          '> div#select2-drop '
                                          'div.select2-search '
                                          '> input')
    SUITE_HOLDER_DROPDOWN_ITEMS = css('body '
                                      '> div#select2-drop '
                                      'ul.select2-results '
                                      'div.select2-result-label '
                                      'span.select2-match')

    SUITE_ADMIN_LABEL = css('div.suite-admin '
                            'h4')
    SUITE_ADMIN_NEW_CUSTOMER_BUTTON = css('div.suite-admin '
                                          'div[ng-hide="suite_account.suite_admin"] '
                                          '> button')
    SUITE_ADMIN_INPUT = css('div.suite-admin '
                            'div[ng-hide="suite_account.suite_admin"] '
                            'a.select2-choice')
    SUITE_ADMIN_SELECTOR = css('div.suite-admin '
                               'div[ng-show="suiteOwners"] '
                               'select[ng-model="suite_account.suite_admin"]')
    SUITE_ADMIN_DROPDOWN = css('body '
                               '> div#select2-drop')
    SUITE_ADMIN_DROPDOWN_SEARCHBOX = css('body '
                                         '> div#select2-drop '
                                         'div.select2-search '
                                         '> input')
    SUITE_ADMIN_DROPDOWN_ITEMS = css('body '
                                     '> div#select2-drop '
                                     'ul.select2-results '
                                     'div.select2-result-label '
                                     'span.select2-match')

    AUTHORIZED_SIGNERS_LABEL = css('div.authorized-signers '
                                   'h4')
    AUTHORIZED_SIGNERS_INPUT = css('div.authorized-signers '
                                   'input[ng-model="signer"]')
    AUTHORIZED_SIGNERS_ADD_SIGNERS_BUTTON = css('div.authorized-signers '
                                                'div#add.btn')

    NEW_CUSTOMER_DIALOG = css('body '
                              '> div.modal.fade.in '
                              'div.modal-dialog')
    NEW_CUSTOMER_NAME_LABEL = css('label:contains("Name")')
    NEW_CUSTOMER_NAME_INPUT = css('input[ng-model="customer.name"]')
    NEW_CUSTOMER_EMAIL_LABEL = css('label:contains("Email")')
    NEW_CUSTOMER_EMAIL_INPUT = css('input[ng-model="customer.email"]')
    NEW_CUSTOMER_PHONE_LABEL = css('label:contains("Phone Number")')
    NEW_CUSTOMER_PHONE_INPUT = css('input[ng-model="customer.phone_number"]')
    NEW_CUSTOMER_OFFICE_PHONE_LABEL = css('label:contains("Office Phone")')
    NEW_CUSTOMER_OFFICE_PHONE_INPUT = css('input[ng-model="customer.office_phone"]')
    NEW_CUSTOMER_CANCEL_BUTTON = css('footer.modal-footer '
                                     'div.btn:contains("Cancel")')
    NEW_CUSTOMER_SAVE_CHANGES_BUTTON = css('footer.modal-footer '
                                           'div.btn:contains("Save Changes")')


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

    DATATABLE_FOOTER = css('.ng-table-counts')
    ITEMS_PER_PAGE_SELECTOR = css('.ng-table-counts '
                                  'select')
    TOTAL_ITEMS_STRONG = css('.ng-table-counts '
                             'strong')
    PAGINATION_BUTTON_GROUP = css('ul.pagination')



