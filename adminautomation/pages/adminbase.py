# Basepage for all logged-in Admin pages

from adminautomation.pages import BasePage, LoginPage
from adminautomation.structures.dropdownselector import Select2
from adminautomation.locators import NavBarLocators, SidebarLocators, AdminPageLocators, BaseLocatorGroup
from adminautomation.locators.by import BaseLocator
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
from time import sleep
from urlparse import urljoin


class AdminPage(BasePage):

    admin_locators = NavBarLocators() + AdminPageLocators() + SidebarLocators()

    def __init__(self, driver, **kwargs):
        # self.admin_locators = BaseLocatorGroup()
        # for k, v in (NavBarLocators.__dict__.items() + SidebarLocators.__dict__.items() + AdminPageLocators.__dict__.items()):
        #     if isinstance(v, BaseLocator):
        #         self.admin_locators.__setattr__(k, v)

        self.SKIP_LOGIN = kwargs.get("skip_login", False)
        self.AUTO_LOGIN = kwargs.get("auto_login", True)

        super(AdminPage, self).__init__(driver, **kwargs)
        self.driver.get(self.ROOT_URL)

        login_url = urljoin(self.ROOT_URL, LoginPage.PATH)
        if self.driver.current_url == login_url and self.SKIP_LOGIN is True:
            self.attach_session_cookie()
            self.go_to_page_url()
        elif self.driver.current_url == login_url and self.AUTO_LOGIN is True:
            admin = LoginPage(self.driver)
            admin.login(kwargs.get("user"), kwargs.get("passwd"))
            admin.go_to_page_url()
        elif self.driver.current_url != self.URL:
            self.go_to_page_url()

    @property
    def LOGO_HOME_BUTTON(self):
        return self.get_element(self.admin_locators.LOGO_HOME_BUTTON)

    @property
    def VENUES_SELECT(self):
        return Select2(self, self.admin_locators.VENUES_LISTBOX)

    @property
    def VENUES_LISTBOX(self):
        return self.get_element(self.admin_locators.VENUES_LISTBOX)

    @property
    def VENUE_LIST_DROPDOWN(self):
        return self.get_element(self.admin_locators.VENUE_LIST_DROPDOWN)

    @property
    def VENUE_LIST_SEARCHBOX(self):
        return self.get_element(self.admin_locators.VENUE_LIST_SEARCHBOX)

    @property
    def VENUE_LIST(self):
        return self.get_element(self.admin_locators.VENUE_LIST)

    @property
    def VENUE_LIST_ITEMS(self):
        return self.get_elements(self.admin_locators.VENUE_LIST_ITEMS)

    @property
    def CURRENT_VENUE_OPTION(self):
        return self.get_element(self.admin_locators.CURRENT_VENUE_OPTION)

    @property
    def CURRENT_VENUE_ID(self):
        return self.CURRENT_VENUE_OPTION.get_attribute('value')

    @property
    def CURRENT_VENUE_NAME(self):
        return self.CURRENT_VENUE_OPTION.text

    @property
    def PUSH_UPDATES_NOTIFICATION(self):
        return self.get_element(self.admin_locators.PUSH_UPDATES_NOTIFICATION)

    @property
    def PUSH_UPDATES_BUTTON(self):
        return self.get_element(self.admin_locators.PUSH_UPDATES_BUTTON)

    @property
    def LOGOUT_BUTTON(self):
        return self.get_element(self.admin_locators.LOGOUT_BUTTON)

    @property
    def DASHBOARD(self):
        return self.get_element(self.admin_locators.DASHBOARD)

    @property
    def LOCATION_CONTROL(self):
        return self.get_element(self.admin_locators.LOCATION_CONTROL)

    @property
    def CATEGORIES(self):
        return self.get_element(self.admin_locators.CATEGORIES)

    @property
    def ITEM_CATEGORIES(self):
        return self.get_element(self.admin_locators.ITEM_CATEGORIES)

    @property
    def MODIFIER_CATEGORIES(self):
        return self.get_element(self.admin_locators.MODIFIER_CATEGORIES)

    @property
    def GROUPS(self):
        return self.get_element(self.admin_locators.GROUPS)

    @property
    def ITEMS(self):
        return self.get_element(self.admin_locators.ITEMS)

    @property
    def MENUS(self):
        return self.get_element(self.admin_locators.MENUS)

    @property
    def LOCATIONS(self):
        return self.get_element(self.admin_locators.LOCATIONS)

    @property
    def SECTIONS(self):
        return self.get_element(self.admin_locators.SECTIONS)

    @property
    def TABLES(self):
        return self.get_element(self.admin_locators.TABLES)

    @property
    def VARIANT_SETS(self):
        return self.get_element(self.admin_locators.VARIANT_SETS)

    @property
    def MODIFIERS(self):
        return self.get_element(self.admin_locators.MODIFIERS)

    @property
    def ADDON_GROUPS(self):
        return self.get_element(self.admin_locators.ADDON_GROUPS)

    @property
    def SUITES(self):
        return self.get_element(self.admin_locators.SUITES)

    @property
    def SUITES_ACCOUNTS(self):
        return self.get_element(self.admin_locators.SUITES_ACCOUNTS)

    @property
    def SUITES_SETUP(self):
        return self.get_element(self.admin_locators.SUITES_SETUP)

    @property
    def SUITES_PREORDER(self):
        return self.get_element(self.admin_locators.SUITES_PREORDER)

    @property
    def EVENTS(self):
        return self.get_element(self.admin_locators.EVENTS)

    @property
    def EVENTS_CALENDAR(self):
        return self.get_element(self.admin_locators.EVENTS_CALENDAR)

    @property
    def EVENTS_TEMPLATES(self):
        return self.get_element(self.admin_locators.EVENTS_TEMPLATES)

    @property
    def ORDERS(self):
        return self.get_element(self.admin_locators.ORDERS)

    @property
    def TIPS(self):
        return self.get_element(self.admin_locators.TIPS)

    @property
    def CASHROOM(self):
        return self.get_element(self.admin_locators.CASHROOM)

    @property
    def INVENTORY(self):
        return self.get_element(self.admin_locators.INVENTORY)

    @property
    def STATUS(self):
        return self.get_element(self.admin_locators.STATUS)

    @property
    def INVENTORY_CATEGORIES(self):
        return self.get_element(self.admin_locators.INVENTORY_CATEGORIES)

    @property
    def INVENTORY_TRANSFERS(self):
        return self.get_element(self.admin_locators.INVENTORY_TRANSFERS)

    @property
    def INVENTORY_MOVEMENTS(self):
        return self.get_element(self.admin_locators.INVENTORY_MOVEMENTS)

    @property
    def STANDSHEETS(self):
        return self.get_element(self.admin_locators.STANDSHEETS)

    @property
    def STOCK_ITEMS(self):
        return self.get_element(self.admin_locators.STOCK_ITEMS)

    @property
    def RECIPES(self):
        return self.get_element(self.admin_locators.RECIPES)

    @property
    def VENDORS(self):
        return self.get_element(self.admin_locators.VENDORS)

    @property
    def INVENTORY_AUDITS(self):
        return self.get_element(self.admin_locators.INVENTORY_AUDITS)

    @property
    def PURCHASE_AND_RECEIVING(self):
        return self.get_element(self.admin_locators.PURCHASE_AND_RECEIVING)

    @property
    def WAREHOUSES(self):
        return self.get_element(self.admin_locators.WAREHOUSES)

    @property
    def REPORTING(self):
        return self.get_element(self.admin_locators.REPORTING)

    @property
    def REPORTS(self):
        return self.get_element(self.admin_locators.REPORTS)

    @property
    def REPORT_TEMPLATES(self):
        return self.get_element(self.admin_locators.REPORT_TEMPLATES)

    @property
    def ORDER_TAKERS(self):
        return self.get_element(self.admin_locators.ORDER_TAKERS)

    @property
    def DEVICES(self):
        return self.get_element(self.admin_locators.DEVICES)

    @property
    def ALERTS(self):
        return self.get_element(self.admin_locators.ALERTS)

    @property
    def BUCKS(self):
        return self.get_element(self.admin_locators.BUCKS)

    @property
    def BUCKS_CARD_SEARCH(self):
        return self.get_element(self.admin_locators.BUCKS_CARD_SEARCH)

    @property
    def BUCKS_ADD_NEW_CARD(self):
        return self.get_element(self.admin_locators.BUCKS_ADD_NEW_CARD)

    @property
    def BUCKS_ALLOCATE_CARDS(self):
        return self.get_element(self.admin_locators.BUCKS_ALLOCATE_CARDS)

    @property
    def BUCKS_IMPORT_EXPORT(self):
        return self.get_element(self.admin_locators.BUCKS_IMPORT_EXPORT)

    @property
    def PAGE_TITLE(self):
        return self.get_element(self.admin_locators.PAGE_TITLE)

    @property
    def BREADCRUMB_LINKS(self):
        return self.get_elements(self.admin_locators.BREADCRUMB_LINKS)

    @property
    def PORTLET_TITLE(self):
        return self.get_element(self.admin_locators.PORTLET_TITLE)

    def return_to_home_by_navbar_logo(self):
        """
        Clicks the Bypass Admin logo to return to the main dashboard page.
        """

        self.LOGO_HOME_BUTTON.click()

    def expand_venues_list(self):
        """
        Opens the venues list to make the venues list and venue searchbox available.
        """

        try:
            if self.VENUE_LIST_DROPDOWN is None:
                self.VENUES_LISTBOX.click()
        except Warning:
            self.VENUES_LISTBOX.click()

    def collapse_venues_list(self):
        """
        Collapes the venues list.
        """

        if self.VENUE_LIST_DROPDOWN:
            self.VENUES_LISTBOX.click()

    def clear_venue_searchbox(self):
        """
        Clears any entered value in the venues searchbox.
        """

        self.expand_venues_list()
        while len(self.VENUE_LIST_SEARCHBOX.get_attribute("value")) > 0:
            self.VENUE_LIST_SEARCHBOX.send_keys(Keys.BACKSPACE)

    def search_for_venue(self, search_query):
        """
        Expands the venues list and enters the given search into the searchbox.
        :param search_query: a string to enter into the searchbox
        """

        self.expand_venues_list()
        self.clear_venue_searchbox()
        self.VENUE_LIST_SEARCHBOX.send_keys(search_query)

    def choose_venue_from_list(self, venue):
        """
        Selects a venue from the list of available venues based on the given name.
        :param venue: the venue name as a string
        """

        self.expand_venues_list()
        target_item = filter(lambda item: item.text == venue, self.VENUE_LIST_ITEMS)[0]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_item)
        while True:
            sleep(1)
            if target_item.is_displayed():
                break
        target_item.click()
        # list_items = self.VENUE_LIST_ITEMS
        # for item in list_items:
        #     if item.text == venue:
        #         break
        #     self.VENUE_LIST_SEARCHBOX.send_keys(Keys.ARROW_DOWN)
        # else:
        #     raise ValueError('Could not file venue: {}'.format(venue))
        #
        # item.click()

    def push_updates_to_devices(self):
        """
        Clicks the Push Update to Devices button that appears in the navbar.
        """

        self.PUSH_UPDATES_BUTTON.click()

    def logout(self):
        """
        Clicks the Logout button from the navbar.
        """

        self.LOGOUT_BUTTON.click()

    def expand_sidebar_tab(self, elem):
        """
        Expands a tab in the sidebar if not already expanded to make the subsections available.
        """

        if "open" not in elem.get_attribute("class").split(" "):
            elem.click()

        sleep(1) # Works for now. Should replace with an explicit wait.

    def navigate_to(self, *args, **kwargs):
        """
        Generic function for selecting a sidebar tab. Handles tab expansion and waits.
        """

        if not args:
            raise TypeError('AdminPage.navigate_to() takes at least 2 arguments (1 given)')

        for item in args[:-1]:
            self.expand_sidebar_tab(item)

        try:
            args[-1].click()
        except WebDriverException:
            if kwargs.get('retry', False):
                self.navigate_to(*args, **kwargs)

    def navigate_to_dashboard(self):
        """
        Navigates to the Dashboard page.
        """

        self.DASHBOARD.click()

    def navigate_to_item_categories(self):
        """
        Navigates to the Item Categories page.
        """

        self.navigate_to(self.LOCATION_CONTROL, self.CATEGORIES, self.ITEM_CATEGORIES)

    def navigate_to_modifier_categories(self):
        """
        Navigates to the Modifier Categories page.
        """

        self.navigate_to(self.LOCATION_CONTROL, self.CATEGORIES, self.MODIFIER_CATEGORIES)

    def navigate_to_groups(self):
        """
        Navigates to the Groups page.
        """

        self.navigate_to(self.LOCATION_CONTROL, self.GROUPS)

    def navigate_to_items(self):
        """
        Navigates to the Items page.
        """

        self.navigate_to(self.LOCATION_CONTROL, self.ITEMS)

    def navigate_to_menus(self):
        """
        Navigates to the Menus page.
        """

        self.navigate_to(self.LOCATION_CONTROL, self.MENUS)

    def navigate_to_locations(self):
        """
        Navigates to the Locations page.
        """

        self.navigate_to(self.LOCATION_CONTROL, self.LOCATIONS)

    def navigate_to_sections(self):
        """
        Navigates to the Sections page.
        """

        self.navigate_to(self.LOCATION_CONTROL, self.SECTIONS)

    def navigate_to_tables(self):
        """
        Navigates to the Tables page.
        """

        self.navigate_to(self.LOCATION_CONTROL, self.TABLES)

    def navigate_to_variant_sets(self):
        """
        Navigates to the Variant Sets page.
        """

        self.navigate_to(self.LOCATION_CONTROL, self.VARIANT_SETS)

    def navigate_to_modifiers(self):
        """
        Navigates to the Modifiers page.
        """

        self.navigate_to(self.LOCATION_CONTROL, self.MODIFIERS)

    def navigate_to_addon_groups(self):
        """
        Navigates to the Addon Groups page.
        """

        self.navigate_to(self.LOCATION_CONTROL, self.ADDON_GROUPS)

    def navigate_to_suites_accounts(self):
        """
        Navigates to the Suites Accounts page.
        """

        self.navigate_to(self.SUITES, self.SUITES_ACCOUNTS)

    def navigate_to_suites_setup(self):
        """
        Navigates to the Suites Setup page.
        """

        self.navigate_to(self.SUITES, self.SUITES_SETUP)

    def navigate_to_suites_preorder(self):
        """
        Navigates to the Suites Pre-Order page.
        """

        self.navigate_to(self.SUITES, self.SUITES_PREORDER)

    def navigate_to_events_calendar(self):
        """
        Navigates to the Events Calendar page.
        """

        self.navigate_to(self.EVENTS, self.EVENTS_CALENDAR)

    def navigate_to_event_templates(self):
        """
        Navigates to the Event Templates page.
        """

        self.navigate_to(self.EVENTS, self.EVENTS_TEMPLATES)

    def navigate_to_orders(self):
        """
        Navigates to the Orders page.
        """

        self.navigate_to(self.EVENTS, self.ORDERS)

    def navigate_to_tips(self):
        """
        Navigates to the Tips page.
        """

        self.navigate_to(self.EVENTS, self.TIPS)

    def navigate_to_cash_room(self):
        """
        Navigates to the Cash Room page.
        """

        self.navigate_to(self.EVENTS, self.CASHROOM)

    def navigate_to_status(self):
        """
        Navigates to the Status page.
        """

        self.navigate_to(self.INVENTORY, self.STATUS)

    def navigate_to_inventory_categories(self):
        """
        Navigates to the Inventory Categories page.
        """

        self.navigate_to(self.INVENTORY, self.INVENTORY_CATEGORIES)

    def navigate_to_inventory_transfers(self):
        """
        Navigates to the Inventory Transfers page.
        """

        self.navigate_to(self.INVENTORY, self.INVENTORY_TRANSFERS)

    def navigate_to_inventory_movements(self):
        """
        Navigates to the Inventory Movements page.
        """

        self.navigate_to(self.INVENTORY, self.INVENTORY_MOVEMENTS)

    def navigate_to_standsheets(self):
        """
        Navigates to the Standsheets page.
        """

        self.navigate_to(self.INVENTORY, self.STANDSHEETS)

    def navigate_to_stock_items(self):
        """
        Navigates to the Stock Items page.
        """

        self.navigate_to(self.INVENTORY, self.STOCK_ITEMS)

    def navigate_to_recipes(self):
        """
        Navigates to the Recipes page.
        """

        self.navigate_to(self.INVENTORY, self.RECIPES)

    def navigate_to_vendors(self):
        """
        Navigates to the Vendors page.
        """

        self.navigate_to(self.INVENTORY, self.VENDORS)

    def navigate_to_inventory_audits(self):
        """
        Navigates to the Inventory Audits page.
        """

        self.navigate_to(self.INVENTORY, self.INVENTORY_AUDITS)

    def navigate_to_purchasing_and_receiving(self):
        """
        Navigates to the Purchasing & Receiving page.
        """

        self.navigate_to(self.INVENTORY, self.PURCHASE_AND_RECEIVING)

    def navigate_to_warehouses(self):
        """
        Navigates to the Warehouses page.
        """

        self.navigate_to(self.INVENTORY, self.WAREHOUSES)

    def navigate_to_reports(self):
        """
        Navigates to the Reports page.
        """

        self.navigate_to(self.REPORTING, self.REPORTS)

    def navigate_to_report_templates(self):
        """
        Navigates to the Report Templates page.
        """

        self.navigate_to(self.REPORTING, self.REPORT_TEMPLATES)

    def navigate_to_order_takers(self):
        """
        Navigates to the Order Takers page.
        """

        self.ORDER_TAKERS.click()

    def navigate_to_devices(self):
        """
        Navigates to the Devices page.
        """

        self.DEVICES.click()

    def navigate_to_alerts(self):
        """
        Navigates to the Alerts page.
        """

        self.ALERTS.click()

    def navigate_to_bucks_search(self):
        """
        Navigates to the Bucks Search page.
        """

        self.navigate_to(self.BUCKS, self.BUCKS_CARD_SEARCH)

    def navigate_to_bucks_new_card(self):
        """
        Navigates to the Bucks Add New Card page.
        """

        self.navigate_to(self.BUCKS, self.BUCKS_ADD_NEW_CARD)

    def navigate_to_bucks_allocate_cards(self):
        """
        Navigates to the Bucks Allocate Cards page.
        """

        self.navigate_to(self.BUCKS, self.BUCKS_ALLOCATE_CARDS)

    def navigate_to_bucks_import_export(self):
        """
        Navigates to the Bucks Import Export page.
        """

        self.navigate_to(self.BUCKS, self.BUCKS_IMPORT_EXPORT)

    def wait_for_angular(self):
        angular_wait_script = """
        var callback = arguments[arguments.length - 1];
        var app = document.querySelector('div[ng-app]');
        try {
            if (angular.getTestability) {
                angular.getTestability(app).whenStable(callback);
            } else {
                angular.element(app).injector().get('$browser').
                        notifyWhenNoOutstandingRequests(callback);
            }
        } catch (e) {
            callback(e);
        }
        """
        self.driver.execute_async_script(angular_wait_script)


    #def _get_dropdown_selector_by_text(self, text, index_when_multiple_match=0):
    #    """
    #    Gets the 'select2-container' element based on the current text. If multiple selectors have the same text,
    #    the index_when_multiple_match argument is used to return that item.
    #    :param text: The text in the dropdown selector to return.
    #    :param index_when_multiple_match: The list index of the item to return if multiple selectors match text.
    #    :return: A DropDownSelector item.
    #    """

    #    elems = self.get_elements(DropDownSelectorLocators.INPUT_BOX_CONTRACTED)
    #    matched_elems =
    #    if len(elems) > 1:
    #        return elems[index_when_multiple_match]
    #    else:
    #        return elems
