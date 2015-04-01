# Locator BaseLocators used by the webdriver to find page elements
# For info on CSS Selectors see:
# https://saucelabs.com/resources/selenium/css-selectors
# http://www.w3.org/TR/CSS21/selector.html
# https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Getting_started/Selectors

from selenium.webdriver.common.by import By


class BaseLocatorGroup(object):
    pass


class LoginPageLocators(BaseLocatorGroup):
    EMAIL_TEXTBOX = (By.CSS_SELECTOR, 'input#user_email')
    PASSWORD_TEXTBOX = (By.CSS_SELECTOR, 'input#user_password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.btn')
    FORM_TITLE = (By.CSS_SELECTOR, 'h3.form-title')
    INVALID_LOGIN_TOAST = (By.CSS_SELECTOR, 'div#toast-container')
    INVALID_LOGIN_TOAST_MESSAGE = (By.CSS_SELECTOR, 'div.toast-message')


class ChooseVenueLocators(BaseLocatorGroup):
    VENUES_LISTBOX = (By.CSS_SELECTOR, 'div#s2id_change_venue')
    VENUE_LIST_SEARCHBOX = (By.CSS_SELECTOR, 'input.select2-input')
    VENUE_LIST = (By.CSS_SELECTOR, 'ul.select2-results')
    VENUE_LIST_ITEMS = (By.CSS_SELECTOR, 'li.select2-result')
    VENUE_OPTIONS = (By.CSS_SELECTOR, 'select#change_venue option')
    GO_BUTTON = (By.CSS_SELECTOR, 'button.btn')
    FORM_TITLE = (By.CSS_SELECTOR, 'h3.form-title')


class NavBarLocators(BaseLocatorGroup):
    LOGO_HOME_BUTTON = (By.CSS_SELECTOR, 'a.navbar-brand[href="/"]')

    VENUES_LISTBOX = (By.CSS_SELECTOR, 'div#s2id_change_venue')
    VENUE_LIST_DROPDOWN = (By.CSS_SELECTOR, 'div#select2-drop')
    VENUE_LIST_SEARCHBOX = (By.CSS_SELECTOR, 'input.select2-input')
    VENUE_LIST = (By.CSS_SELECTOR, 'ul.select2-results')
    VENUE_LIST_ITEMS = (By.CSS_SELECTOR, 'li.select2-result')
    CURRENT_VENUE_ITEM = (By.CSS_SELECTOR, 'span.select2-chosen')

    PUSH_UPDATES_NOTIFICATION = (By.CSS_SELECTOR, 'li#push-menus span.notification')
    PUSH_UPDATES_BUTTON = (By.CSS_SELECTOR, 'a[href="/menu_push"]')

    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a[href="/admin_sessions"]')


class SidebarLocators(BaseLocatorGroup):
    DASHBOARD = (By.CSS_SELECTOR, 'li.dashboard')

    LOCATION_CONTROL = (By.CSS_SELECTOR, 'li.locations')
    CATEGORIES = (By.CSS_SELECTOR, 'li.categories')
    ITEM_CATEGORIES = (By.CSS_SELECTOR, 'li.locations li.categories a[href="/categories"]')
    MODIFIER_CATEGORIES = (By.CSS_SELECTOR, 'li.locations li.categories a[href="/modifier_categories"]')
    GROUPS = (By.CSS_SELECTOR, 'li.locations a[href="/groups"]')
    ITEMS = (By.CSS_SELECTOR, 'li.locations a[href="/items"]')
    MENUS = (By.CSS_SELECTOR, 'li.locations a[href="/menus"]')
    LOCATIONS = (By.CSS_SELECTOR, 'li.locations a[href="/locations"]')
    SECTIONS = (By.CSS_SELECTOR, 'li.locations a[href="/sections"]')
    TABLES = (By.CSS_SELECTOR, 'li.locations a[href="/tables"]')
    VARIANT_SETS = (By.CSS_SELECTOR, 'li.locations a[href="/option_types"]')
    MODIFIERS = (By.CSS_SELECTOR, 'li.locations a[href="/modifiers"]')
    ADDON_GROUPS = (By.CSS_SELECTOR, 'li.locations a[href="/addon_groups"]')

    SUITES = (By.CSS_SELECTOR, 'li.suites')
    SUITES_ACCOUNTS = (By.CSS_SELECTOR, 'li.suites a[href="/suite_accounts"]')
    SUITES_SETUP = (By.CSS_SELECTOR, 'li.suites a[href="/suites"]')
    SUITES_PREORDER = (By.CSS_SELECTOR, 'li.suites a[href="/pre_orders"]')

    EVENTS = (By.CSS_SELECTOR, 'li.events')
    EVENTS_CALENDAR = (By.CSS_SELECTOR, 'li.events a[href="/events"]')
    EVENTS_TEMPLATES = (By.CSS_SELECTOR, 'li.events a[href="/event_templates"]')
    ORDERS = (By.CSS_SELECTOR, 'li.events a[href="/orders"]')
    TIPS = (By.CSS_SELECTOR, 'li.events a[href="/tips"]')
    CASHROOM = (By.CSS_SELECTOR, 'li.events a[href="/cashroom"]')

    INVENTORY = (By.CSS_SELECTOR, 'li.inventory')
    STATUS = (By.CSS_SELECTOR, 'li.inventory a[href="/inventory"]')
    INVENTORY_CATEGORIES = (By.CSS_SELECTOR, 'li.inventory a[href="/inventory_categories"]')
    INVENTORY_TRANSFERS = (By.CSS_SELECTOR, 'li.inventory a[href="/inventory_transfers"]')
    INVENTORY_MOVEMENTS = (By.CSS_SELECTOR, 'li.inventory a[href="/inventory_movements"]')
    STANDSHEETS = (By.CSS_SELECTOR, 'li.inventory a[href="/standsheets"]')
    STOCK_ITEMS = (By.CSS_SELECTOR, 'li.inventory a[href="/stock_items"]')
    RECIPES = (By.CSS_SELECTOR, 'li.inventory a[href="/recipes"]')
    VENDORS = (By.CSS_SELECTOR, 'li.inventory a[href="/vendors"]')
    INVENTORY_AUDITS = (By.CSS_SELECTOR, 'li.inventory a[href="/inventory_audits"]')
    PURCHASE_AND_RECEIVING = (By.CSS_SELECTOR, 'li.inventory a[href="/purchase_orders"]')
    WAREHOUSES = (By.CSS_SELECTOR, 'li.inventory a[href="/warehouses"]')

    REPORTING = (By.CSS_SELECTOR, 'li.reports')
    REPORTS = (By.CSS_SELECTOR, 'li.reports a[href="/reports"]')
    REPORT_TEMPLATES = (By.CSS_SELECTOR, 'li.reports a[href="/report_templates"]')

    ORDER_TAKERS = (By.CSS_SELECTOR, 'li.order-takers')
    DEVICES = (By.CSS_SELECTOR, 'li.terminals')
    ALERTS = (By.CSS_SELECTOR, 'li.alerts')

    BUCKS = (By.CSS_SELECTOR, 'li.bucks')
    BUCKS_CARD_SEARCH = (By.CSS_SELECTOR, 'li.bucks a[href="/bucks#/"]')
    BUCKS_ADD_NEW_CARD = (By.CSS_SELECTOR, 'li.bucks a[href="/bucks#/add_card"]')
    BUCKS_ALLOCATE_CARDS = (By.CSS_SELECTOR, 'li.bucks a[href="/bucks#/allocate"]')
    BUCKS_IMPORT_EXPORT = (By.CSS_SELECTOR, 'li.bucks a[href="/bucks#/import"]')


class AdminPageLocators(BaseLocatorGroup):
    PAGE_TITLE = (By.CSS_SELECTOR, 'h3.page-title')
    BREADCRUMB_LINKS = (By.CSS_SELECTOR, 'ul.breadcrumb a')
    PORTLET_TITLE = (By.CSS_SELECTOR, 'div.portlet-title div.caption')


class SuiteAccountsLocators(BaseLocatorGroup):
    NEW_SUITE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'a.new-suite-account')
    ITEMS_PER_PAGE_SELECTOR = (By.CSS_SELECTOR, 'select[name="suite-accounts-list_length"]')
    ITEMS_PER_PAGE_OPTIONS = (By.CSS_SELECTOR, 'select[name="suite-accounts-list_length"] option')
    SUITE_ACCOUNTS_SEARCHBOX = (By.CSS_SELECTOR, 'div#suite-accounts-list_filter input[type="search"]')

    DATATABLE = (By.CSS_SELECTOR, 'table#suite-accounts-list')
    DATATABLE_HEADERS = (By.CSS_SELECTOR, 'table#suite-accounts-list thead td')
    # Remove unused selectors
    # DATATABLE_ACCOUNT_NAME_HEADER = (By.CSS_SELECTOR, 'table#suite-accounts-list thead td:contains("Account Name")')
    # DATATABLE_SUITE_HEADER = (By.CSS_SELECTOR, 'table#suite-accounts-list thead td:contains("Suite")')
    # DATATABLE_SUITE_HOLDER_HEADER = (By.CSS_SELECTOR, 'table#suite-accounts-list thead td:contains("Suite Holder")')
    # DATATABLE_PHONE_HEADER = (By.CSS_SELECTOR, 'table#suite-accounts-list thead td:contains("Phone")')
    # DATATABLE_EMAIL_HEADER = (By.CSS_SELECTOR, 'table#suite-accounts-list thead td:contains("Email")')
    # DATATABLE_EDIT_HEADER = (By.CSS_SELECTOR, 'table#suite-accounts-list thead td:contains("Edit")')
    DATATABLE_ROWS = (By.CSS_SELECTOR, 'table#suite-accounts-list tbody tr')
    DATATABLE_ROW_ACCOUNT_NAME = (By.CSS_SELECTOR, 'td:nth-of-type(1)')
    DATATABLE_ROW_SUITE = (By.CSS_SELECTOR, 'td:nth-of-type(2)')
    DATATABLE_ROW_SUITE_HOLDER = (By.CSS_SELECTOR, 'td:nth-of-type(3)')
    DATATABLE_ROW_PHONE = (By.CSS_SELECTOR, 'td:nth-of-type(4)')
    DATATABLE_ROW_EMAIL = (By.CSS_SELECTOR, 'td:nth-of-type(5)')
    DATATABLE_ROW_EDIT = (By.CSS_SELECTOR, 'td:nth-of-type(6) a.edit')
    DATATABLE_ROW_DELETE = (By.CSS_SELECTOR, 'td:nth-of-type(6) a.destroy')

    DATATABLE_FOOTER = (By.CSS_SELECTOR, 'div#suite-accounts-list_info')
    PAGINATION_BUTTONS = (By.CSS_SELECTOR, '.pagination'
                                           'li')


class ModifySuiteAccountLocators(BaseLocatorGroup):
    PORTLET_TITLE = (By.CSS_SELECTOR, 'div.portlet-title '
                                      'div.caption')
    FORM = (By.CSS_SELECTOR, 'div#suite-account')
    CANCEL_BUTTON = (By.CSS_SELECTOR, 'a#cancel')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'div#save')

    SUITE_ACCOUNT_NAME_INPUT = (By.CSS_SELECTOR, 'input[ng-model="suite_account.name"]')
    SUITE_TYPE_INPUT = (By.CSS_SELECTOR, 'input[ng-model="suite_account.suite_type"]')
    BILLING_ADDRESS_INPUT = (By.CSS_SELECTOR, 'textarea[ng-model="suite_account.address"]')
    NOTES_INPUT = (By.CSS_SELECTOR, 'textarea[ng-model="suite_account.notes"]')

    SUITE_INPUT_LABEL = (By.XPATH, '//div[@id="suite-account"]//form//label[text()="Suite"]')
    SUITE_INPUT = (By.CSS_SELECTOR, 'div#suite-account '
                                    'form div.form-group:nth-of-type(3) '
                                    'a.select2-choice')
    SUITE_SELECTOR = (By.CSS_SELECTOR, 'select[ng-model="suite_account.suite_id"]')
    SUITE_DROPDOWN = (By.CSS_SELECTOR, 'body '
                                       '> div#select2-drop')
    SUITE_DROPDOWN_SEARCHBOX = (By.CSS_SELECTOR, 'body '
                                                 '> div#select2-drop '
                                                 '> div.select2-search '
                                                 '> input')
    SUITE_DROPDOWN_ITEMS = (By.CSS_SELECTOR, 'body '
                                             '> div#select2-drop '
                                             'ul.select2-results '
                                             'div.select2-result-label')

    SUITE_HOLDER_LABEL = (By.CSS_SELECTOR, 'div.suite-holder'
                                           'h4')
    SUITE_HOLDER_NEW_CUSTOMER_BUTTON = (By.CSS_SELECTOR, 'div.suite-holder > '
                                                         'div[ng-hide="suite_account.suite_holder"] '
                                                         '> button')
    SUITE_HOLDER_INPUT = (By.CSS_SELECTOR, 'div.suite-holder '
                                           'a.select2-choice')
    SUITE_HOLDER_SELECTOR = (By.CSS_SELECTOR, 'div.suite-holder '
                                              'span[ng-show="suiteOwners"] '
                                              'select[ng-model="suite_account.suite_holder"]')
    SUITE_HOLDER_DROPDOWN = (By.CSS_SELECTOR, 'body '
                                              '> div#select2-drop')
    SUITE_HOLDER_DROPDOWN_SEARCHBOX = (By.CSS_SELECTOR, 'body '
                                                        '> div#select2-drop '
                                                        'div.select2-search '
                                                        '> input')
    SUITE_HOLDER_DROPDOWN_ITEMS = (By.CSS_SELECTOR, 'body '
                                                    '> div#select2-drop '
                                                    'ul.select2-results '
                                                    'div.select2-result-label '
                                                    'span.select2-match')

    SUITE_ADMIN_LABEL = (By.CSS_SELECTOR, 'div.suite-admin '
                                          'h4')
    SUITE_ADMIN_NEW_CUSTOMER_BUTTON = (By.CSS_SELECTOR, 'div.suite-admin '
                                                        'div[ng-hide="suite_account.suite_admin"] '
                                                        '> button')
    SUITE_ADMIN_INPUT = (By.CSS_SELECTOR, 'div.suite-admin '
                                          'div[ng-hide="suite_account.suite_admin"] '
                                          'a.select2-choice')
    SUITE_ADMIN_SELECTOR = (By.CSS_SELECTOR, 'div.suite-admin '
                                             'div[ng-show="suiteOwners"] '
                                             'select[ng-model="suite_account.suite_admin"]')
    SUITE_ADMIN_DROPDOWN = (By.CSS_SELECTOR, 'body '
                                             '> div#select2-drop')
    SUITE_ADMIN_DROPDOWN_SEARCHBOX = (By.CSS_SELECTOR, 'body '
                                                       '> div#select2-drop '
                                                       'div.select2-search '
                                                       '> input')
    SUITE_ADMIN_DROPDOWN_ITEMS = (By.CSS_SELECTOR, 'body '
                                                   '> div#select2-drop '
                                                   'ul.select2-results '
                                                   'div.select2-result-label '
                                                   'span.select2-match')

    AUTHORIZED_SIGNERS_LABEL = (By.CSS_SELECTOR, 'div.authorized-signers '
                                                 'h4')
    AUTHORIZED_SIGNERS_INPUT = (By.CSS_SELECTOR, 'div.authorized-signers '
                                                 'input[ng-model="signer"]')
    AUTHORIZED_SIGNERS_ADD_SIGNERS_BUTTON = (By.CSS_SELECTOR, 'div.authorized-signers '
                                                              'div#add.btn')

    NEW_CUSTOMER_DIALOG = (By.CSS_SELECTOR, 'body '
                                            '> div.modal.fade.in '
                                            '> div.modal-dialog')
    NEW_CUSTOMER_NAME_LABEL = (By.CSS_SELECTOR, 'label:contains("Name")')
    NEW_CUSTOMER_NAME_INPUT = (By.CSS_SELECTOR, 'input[ng-model="customer.name"]')
    NEW_CUSTOMER_EMAIL_LABEL = (By.CSS_SELECTOR, 'label:contains("Email")')
    NEW_CUSTOMER_EMAIL_INPUT = (By.CSS_SELECTOR, 'input[ng-model="customer.email"]')
    NEW_CUSTOMER_PHONE_LABEL = (By.CSS_SELECTOR, 'label:contains("Phone Number")')
    NEW_CUSTOMER_PHONE_INPUT = (By.CSS_SELECTOR, 'input[ng-model="customer.phone_number"]')
    NEW_CUSTOMER_OFFICE_PHONE_LABEL = (By.CSS_SELECTOR, 'label:contains("Office Phone")')
    NEW_CUSTOMER_OFFICE_PHONE_INPUT = (By.CSS_SELECTOR, 'input[ng-model="customer.office_phone"]')
    NEW_CUSTOMER_CANCEL_BUTTON = (By.CSS_SELECTOR, 'footer.modal-footer '
                                                   'div.btn:contains("Cancel")')
    NEW_CUSTOMER_SAVE_CHANGES_BUTTON = (By.CSS_SELECTOR, 'footer.modal-footer '
                                                         'div.btn:contains("Save Changes")')


class OrdersLocators(BaseLocatorGroup):
    RELOAD_TABLE_BUTTON = (By.CSS_SELECTOR, 'div.icon-refresh')
    NEW_ORDER_BUTTON = (By.CSS_SELECTOR, 'div.orders-buttons'
                                         'div.btn:nth-child(2)')

    DATATABLE = (By.CSS_SELECTOR, 'table#order_list')
    DATATABLE_HEADERS = (By.CSS_SELECTOR, 'table#order_list'
                                          'th.header')
    DATATABLE_FILTERS = (By.CSS_SELECTOR, 'table#order_list'
                                          'th.filter')
    DATATABLE_TABLE_ROWS = (By.CSS_SELECTOR, 'table#order_list'
                                       'tbody'
                                       'tr')
    DATATABLE_ORDER_IDS = (By.CSS_SELECTOR, 'td[data-title-text="ID"]')
    DATATABLE_ORDER_DAILY_IDS = (By.CSS_SELECTOR, 'td[data-title-text="Daily ID"]')
    DATATABLE_CREATEDS = (By.CSS_SELECTOR, 'td[data-title-text="Created"]')
    DATATABLE_STATES = (By.CSS_SELECTOR, 'td[data-title-text="State"]')
    DATATABLE_LOCATIONS = (By.CSS_SELECTOR, 'td[data-title-text="Location"]')
    DATATABLE_TOTALS = (By.CSS_SELECTOR, 'td[data-title-text="Total"]')
    DATATABLE_SECTIONS = (By.CSS_SELECTOR, 'td[data-title-text="Section"]')
    DATATABLE_ROWS = (By.CSS_SELECTOR, 'td[data-title-text="Row"]')
    DATATABLE_SEATS = (By.CSS_SELECTOR, 'td[data-title-text="Seat"]')
    DATATABLE_NAMES = (By.CSS_SELECTOR, 'td[data-title-text="Name"]')
    DATATABLE_CC_LAST_FOURS = (By.CSS_SELECTOR, 'td[data-title-text="CC Last Four"]')
    DATATABLE_ORDER_TAKERS = (By.CSS_SELECTOR, 'td[data-title-text="Order Taker"]')

    DATATABLE_FOOTER = (By.CSS_SELECTOR, '.ng-table-counts')
    ITEMS_PER_PAGE_SELECTOR = (By.CSS_SELECTOR, '.ng-table-counts'
                                                'select')
    TOTAL_ITEMS_STRONG = (By.CSS_SELECTOR, '.ng-table-counts'
                                           'strong')
    PAGINATION_BUTTON_GROUP = (By.CSS_SELECTOR, 'ul.pagination')



