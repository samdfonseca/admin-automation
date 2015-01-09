# Base page for all logged-in Admin pages

from adminautomation.pages import BasePage, LoginPage
from adminautomation.utils.locators import NavBarLocators, SidebarLocators, AdminPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from time import sleep
from urlparse import urljoin


class AdminPage(BasePage):

    def __init__(self, driver, **kwargs):
        self.SKIP_LOGIN = kwargs.get("skip_login", False)
        self.AUTO_LOGIN = kwargs.get("auto_login", True)

        super(AdminPage, self).__init__(driver, **kwargs)

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
        return self.get_element(NavBarLocators.LOGO_HOME_BUTTON)


    @property
    def VENUES_LISTBOX(self):
        return self.get_element(NavBarLocators.VENUES_LISTBOX)


    @property
    def VENUE_LIST_DROPDOWN(self):
        return self.get_element(NavBarLocators.VENUE_LIST_DROPDOWN)


    @property
    def VENUE_LIST_SEARCHBOX(self):
        return self.get_element(NavBarLocators.VENUE_LIST_SEARCHBOX)


    @property
    def VENUE_LIST(self):
        return self.get_element(NavBarLocators.VENUE_LIST)


    @property
    def VENUE_LIST_ITEMS(self):
        return self.get_elements(NavBarLocators.VENUE_LIST_ITEMS)


    @property
    def CURRENT_VENUE_ITEM(self):
        return self.get_element(NavBarLocators.CURRENT_VENUE_ITEM)


    @property
    def PUSH_UPDATES_NOTIFICATION(self):
        return self.get_element(NavBarLocators.PUSH_UPDATES_NOTIFICATION)


    @property
    def PUSH_UPDATES_BUTTON(self):
        return self.get_element(NavBarLocators.PUSH_UPDATES_BUTTON)


    @property
    def LOGOUT_BUTTON(self):
        return self.get_element(NavBarLocators.LOGOUT_BUTTON)


    @property
    def DASHBOARD(self):
        return self.get_element(SidebarLocators.DASHBOARD)


    @property
    def LOCATION_CONTROL(self):
        return self.get_element(SidebarLocators.LOCATION_CONTROL)


    @property
    def CATEGORIES(self):
        return self.get_element(SidebarLocators.CATEGORIES)


    @property
    def ITEM_CATEGORIES(self):
        return self.get_element(SidebarLocators.ITEM_CATEGORIES)


    @property
    def MODIFIER_CATEGORIES(self):
        return self.get_element(SidebarLocators.MODIFIER_CATEGORIES)


    @property
    def GROUPS(self):
        return self.get_element(SidebarLocators.GROUPS)


    @property
    def ITEMS(self):
        return self.get_element(SidebarLocators.ITEMS)


    @property
    def MENUS(self):
        return self.get_element(SidebarLocators.MENUS)


    @property
    def LOCATIONS(self):
        return self.get_element(SidebarLocators.LOCATIONS)


    @property
    def SECTIONS(self):
        return self.get_element(SidebarLocators.SECTIONS)


    @property
    def TABLES(self):
        return self.get_element(SidebarLocators.TABLES)


    @property
    def VARIANT_SETS(self):
        return self.get_element(SidebarLocators.VARIANT_SETS)


    @property
    def MODIFIERS(self):
        return self.get_element(SidebarLocators.MODIFIERS)


    @property
    def ADDON_GROUPS(self):
        return self.get_element(SidebarLocators.ADDON_GROUPS)


    @property
    def SUITES(self):
        return self.get_element(SidebarLocators.SUITES)


    @property
    def SUITES_ACCOUNTS(self):
        return self.get_element(SidebarLocators.SUITES_ACCOUNTS)


    @property
    def SUITES_SETUP(self):
        return self.get_element(SidebarLocators.SUITES_SETUP)


    @property
    def SUITES_PREORDER(self):
        return self.get_element(SidebarLocators.SUITES_PREORDER)


    @property
    def EVENTS(self):
        return self.get_element(SidebarLocators.EVENTS)


    @property
    def EVENTS_CALENDAR(self):
        return self.get_element(SidebarLocators.EVENTS_CALENDAR)


    @property
    def EVENTS_TEMPLATES(self):
        return self.get_element(SidebarLocators.EVENTS_TEMPLATES)


    @property
    def ORDERS(self):
        return self.get_element(SidebarLocators.ORDERS)


    @property
    def TIPS(self):
        return self.get_element(SidebarLocators.TIPS)


    @property
    def CASHROOM(self):
        return self.get_element(SidebarLocators.CASHROOM)


    @property
    def INVENTORY(self):
        return self.get_element(SidebarLocators.INVENTORY)


    @property
    def STATUS(self):
        return self.get_element(SidebarLocators.STATUS)


    @property
    def INVENTORY_CATEGORIES(self):
        return self.get_element(SidebarLocators.INVENTORY_CATEGORIES)


    @property
    def INVENTORY_TRANSFERS(self):
        return self.get_element(SidebarLocators.INVENTORY_TRANSFERS)


    @property
    def INVENTORY_MOVEMENTS(self):
        return self.get_element(SidebarLocators.INVENTORY_MOVEMENTS)


    @property
    def STANDSHEETS(self):
        return self.get_element(SidebarLocators.STANDSHEETS)


    @property
    def STOCK_ITEMS(self):
        return self.get_element(SidebarLocators.STOCK_ITEMS)


    @property
    def RECIPES(self):
        return self.get_element(SidebarLocators.RECIPES)


    @property
    def VENDORS(self):
        return self.get_element(SidebarLocators.VENDORS)


    @property
    def INVENTORY_AUDITS(self):
        return self.get_element(SidebarLocators.INVENTORY_AUDITS)


    @property
    def PURCHASE_AND_RECEIVING(self):
        return self.get_element(SidebarLocators.PURCHASE_AND_RECEIVING)


    @property
    def WAREHOUSES(self):
        return self.get_element(SidebarLocators.WAREHOUSES)


    @property
    def REPORTING(self):
        return self.get_element(SidebarLocators.REPORTING)


    @property
    def REPORTS(self):
        return self.get_element(SidebarLocators.REPORTS)


    @property
    def REPORT_TEMPLATES(self):
        return self.get_element(SidebarLocators.REPORT_TEMPLATES)


    @property
    def ORDER_TAKERS(self):
        return self.get_element(SidebarLocators.ORDER_TAKERS)


    @property
    def DEVICES(self):
        return self.get_element(SidebarLocators.DEVICES)


    @property
    def ALERTS(self):
        return self.get_element(SidebarLocators.ALERTS)


    @property
    def PAGE_TITLE(self):
        return self.get_element(AdminPageLocators.PAGE_TITLE)


    @property
    def BREADCRUMB_LINKS(self):
        return self.get_elements(AdminPageLocators.BREADCRUMB_LINKS)


    @property
    def PORTLET_TITLE(self):
        return self.get_element(AdminPageLocators.PORTLET_TITLE)


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


    def navigate_to(self, parent_tabs, target_tab):
        """
        Generic function for selecting a sidebar tab. Handles tab expansion and waits.
        """

        for tab in parent_tabs:
            self.expand_sidebar_tab(tab)

        try:
            target_tab.click()
        except WebDriverException:
            self.navigate_to(parent_tabs, target_tab)


    def navigate_to_dashboard(self):
        """
        Navigates to the Dashboard page.
        """

        self.DASHBOARD.click()


    def navigate_to_item_categories(self):
        """
        Navigates to the Item Categories page.
        """

        self.navigate_to([self.LOCATION_CONTROL, self.CATEGORIES], self.ITEM_CATEGORIES)


    def navigate_to_modifier_categories(self):
        """
        Navigates to the Modifier Categories page.
        """

        self.navigate_to([self.LOCATION_CONTROL, self.CATEGORIES], self.MODIFIER_CATEGORIES)


    def navigate_to_groups(self):
        """
        Navigates to the Groups page.
        """

        self.navigate_to([self.LOCATION_CONTROL], self.GROUPS)


    def navigate_to_items(self):
        """
        Navigates to the Items page.
        """

        self.navigate_to([self.LOCATION_CONTROL], self.ITEMS)


    def navigate_to_menus(self):
        """
        Navigates to the Menus page.
        """

        self.navigate_to([self.LOCATION_CONTROL], self.MENUS)


    def navigate_to_locations(self):
        """
        Navigates to the Locations page.
        """

        self.navigate_to([self.LOCATION_CONTROL], self.LOCATIONS)


    def navigate_to_sections(self):
        """
        Navigates to the Sections page.
        """

        self.navigate_to([self.LOCATION_CONTROL], self.SECTIONS)


    def navigate_to_tables(self):
        """
        Navigates to the Tables page.
        """

        self.navigate_to([self.LOCATION_CONTROL], self.TABLES)


    def navigate_to_variant_sets(self):
        """
        Navigates to the Variant Sets page.
        """

        self.navigate_to([self.LOCATION_CONTROL], self.VARIANT_SETS)


    def navigate_to_modifiers(self):
        """
        Navigates to the Modifiers page.
        """

        self.navigate_to([self.LOCATION_CONTROL], self.MODIFIERS)


    def navigate_to_addon_groups(self):
        """
        Navigates to the Addon Groups page.
        """

        self.navigate_to([self.LOCATION_CONTROL], self.ADDON_GROUPS)


    def navigate_to_suites_accounts(self):
        """
        Navigates to the Suites Accounts page.
        """

        self.navigate_to([self.SUITES], self.SUITES_ACCOUNTS)


    def navigate_to_suites_setup(self):
        """
        Navigates to the Suites Setup page.
        """

        self.navigate_to([self.SUITES], self.SUITES_SETUP)


    def navigate_to_suites_preorder(self):
        """
        Navigates to the Suites Pre-Order page.
        """

        self.navigate_to([self.SUITES], self.SUITES_PREORDER)


    def navigate_to_events_calendar(self):
        """
        Navigates to the Events Calendar page.
        """

        self.navigate_to([self.EVENTS], self.EVENTS_CALENDAR)


    def navigate_to_event_templates(self):
        """
        Navigates to the Event Templates page.
        """

        self.navigate_to([self.EVENTS], self.EVENTS_TEMPLATES)


    def navigate_to_orders(self):
        """
        Navigates to the Orders page.
        """

        self.navigate_to([self.EVENTS], self.ORDERS)


    def navigate_to_tips(self):
        """
        Navigates to the Tips page.
        """

        self.navigate_to([self.EVENTS], self.TIPS)


    def navigate_to_cash_room(self):
        """
        Navigates to the Cash Room page.
        """

        self.navigate_to([self.EVENTS], self.CASHROOM)


    def nagivate_to_status(self):
        """
        Navigates to the Status page.
        """

        self.navigate_to([self.INVENTORY], self.STATUS)


    def navigate_to_inventory_categories(self):
        """
        Navigates to the Inventory Categories page.
        """

        self.navigate_to([self.INVENTORY], self.INVENTORY_CATEGORIES)


    def navigate_to_inventory_transfers(self):
        """
        Navigates to the Inventory Transfers page.
        """

        self.navigate_to([self.INVENTORY], self.INVENTORY_TRANSFERS)


    def navigate_to_inventory_movements(self):
        """
        Navigates to the Inventory Movements page.
        """

        self.navigate_to([self.INVENTORY], self.INVENTORY_MOVEMENTS)


    def navigate_to_standsheets(self):
        """
        Navigates to the Standsheets page.
        """

        self.navigate_to([self.INVENTORY], self.STANDSHEETS)


    def navigate_to_stock_items(self):
        """
        Navigates to the Stock Items page.
        """

        self.navigate_to([self.INVENTORY], self.STOCK_ITEMS)


    def navigate_to_recipes(self):
        """
        Navigates to the Recipes page.
        """

        self.navigate_to([self.INVENTORY], self.RECIPES)


    def navigate_to_vendors(self):
        """
        Navigates to the Vendors page.
        """

        self.navigate_to([self.INVENTORY], self.VENDORS)


    def navigate_to_inventory_audits(self):
        """
        Navigates to the Inventory Audits page.
        """

        self.navigate_to([self.INVENTORY], self.INVENTORY_AUDITS)


    def navigate_to_purchasing_and_receiving(self):
        """
        Navigates to the Purchasing & Receiving page.
        """

        self.navigate_to([self.INVENTORY], self.PURCHASE_AND_RECEIVING)


    def navigate_to_warehouses(self):
        """
        Navigates to the Warehouses page.
        """

        self.navigate_to([self.INVENTORY], self.WAREHOUSES)


    def navigate_to_reports(self):
        """
        Navigates to the Reports page.
        """

        self.navigate_to([self.REPORTING], self.REPORTS)


    def navigate_to_report_templates(self):
        """
        Navigates to the Report Templates page.
        """

        self.navigate_to([self.REPORTING], self.REPORT_TEMPLATES)


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
