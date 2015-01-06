# Locator objects used by the webdriver to find page elements
# For info on CSS Selectors see:
# https://saucelabs.com/resources/selenium/css-selectors
# http://www.w3.org/TR/CSS21/selector.html
# https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Getting_started/Selectors

from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    EMAIL_TEXTBOX = (By.CSS_SELECTOR, 'input#user_email')
    PASSWORD_TEXTBOX = (By.CSS_SELECTOR, 'input#user_password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.btn:contains("Login")')
    FORM_TITLE = (By.CSS_SELECTOR, 'h3.form-title')
    INVALID_LOGIN_TOAST = (By.CSS_SELECTOR, 'div#toast-container')
    INVALID_LOGIN_TOAST_MESSAGE = (By.CSS_SELECTOR, 'div.toast-message')


class ChooseVenueLocators(object):
    VENUES_LISTBOX = (By.CSS_SELECTOR, 'div#s2id_change_venue')
    VENUE_LIST_SEARCHBOX = (By.CSS_SELECTOR, 'input.select2-input')
    VENUE_LIST = (By.CSS_SELECTOR, 'ul.select2-results')
    VENUE_LIST_ITEMS = (By.CSS_SELECTOR, 'li.select2-result')
    VENUE_OPTIONS = (By.CSS_SELECTOR, 'select#change_venue option')
    GO_BUTTON = (By.CSS_SELECTOR, 'button.btn:contains("Go")')
    FORM_TITLE = (By.CSS_SELECTOR, 'h3.form-title')


class NavBarLocators(object):
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


class SidebarLocators(object):
    DASHBOARD = (By.CSS_SELECTOR, 'li.dashboard')

    LOCATION_CONTROL = (By.CSS_SELECTOR, 'li.locations')
    CATEGORIES = (By.CSS_SELECTOR, 'li.categories')
    ITEM_CATEGORIES = (By.CSS_SELECTOR, 'a[href="/categories"]')
    MODIFIER_CATEGORIES = (By.CSS_SELECTOR, 'a[href="/modifier_categories"]')
    GROUPS = (By.CSS_SELECTOR, 'a[href="/groups"]')
    ITEMS = (By.CSS_SELECTOR, 'a[href="/items"]')
    MENUS = (By.CSS_SELECTOR, 'a[href="/menus"]')
    LOCATIONS = (By.CSS_SELECTOR, 'a[href="/locations"]')
    SECTIONS = (By.CSS_SELECTOR, 'a[href="/sections"]')
    TABLES = (By.CSS_SELECTOR, 'a[href="/tables"]')
    VARIANT_SETS = (By.CSS_SELECTOR, 'a[href="/option_types"]')
    MODIFIERS = (By.CSS_SELECTOR, 'a[href="/modifiers"]')
    ADDON_GROUPS = (By.CSS_SELECTOR, 'a[href="/addon_groups"]')

    SUITES = (By.CSS_SELECTOR, 'li.suites')
    SUITES_ACCOUNTS = (By.CSS_SELECTOR, 'a[href="/suite_accounts"]')
    SUITES_SETUP = (By.CSS_SELECTOR, 'a[href="/suites"]')
    SUITES_PREORDER = (By.CSS_SELECTOR, 'a[href="/pre_orders"]')

    EVENTS = (By.CSS_SELECTOR, 'li.events')
    EVENTS_CALENDAR = (By.CSS_SELECTOR, 'a[href="/events"]')
    EVENTS_TEMPLATES = (By.CSS_SELECTOR, 'a[href="/event_templates"]')
    ORDERS = (By.CSS_SELECTOR, 'a[href="/orders"]')
    TIPS = (By.CSS_SELECTOR, 'a[href="/tips"]')
    CASHROOM = (By.CSS_SELECTOR, 'a[href="/cashroom"]')

    INVENTORY = (By.CSS_SELECTOR, 'li.inventory')
    STATUS = (By.CSS_SELECTOR, 'a[href="/inventory"]')
    INVENTORY_CATEGORIES = (By.CSS_SELECTOR, 'a[href="/inventory_categories"]')
    INVENTORY_TRANSFERS = (By.CSS_SELECTOR, 'a[href="/inventory_transfers"]')
    INVENTORY_MOVEMENTS = (By.CSS_SELECTOR, 'a[href="/inventory_movements"]')
    STANDSHEETS = (By.CSS_SELECTOR, 'a[href="/standsheets"]')
    STOCK_ITEMS = (By.CSS_SELECTOR, 'a[href="/stock_items"]')
    RECIPES = (By.CSS_SELECTOR, 'a[href="/recipes"]')
    VENDORS = (By.CSS_SELECTOR, 'a[href="/vendors"]')
    INVENTORY_AUDITS = (By.CSS_SELECTOR, 'a[href="/inventory_audits"]')
    PURCHASE_AND_RECEIVING = (By.CSS_SELECTOR, 'a[href="/purchase_orders"]')
    WAREHOUSES = (By.CSS_SELECTOR, 'a[href="/warehouses"]')

    REPORTING = (By.CSS_SELECTOR, 'li.reports')
    REPORTS = (By.CSS_SELECTOR, 'a[href="/reports"]')
    REPORT_TEMPLATES = (By.CSS_SELECTOR, 'a[href="/report_templates"]')

    ORDER_TAKERS = (By.CSS_SELECTOR, 'li.order-takers')
    DEVICES = (By.CSS_SELECTOR, 'li.terminals')
    ALERTS = (By.CSS_SELECTOR, 'li.alerts')