# Base page for all logged-in Admin pages

from adminautomation.pages import BasePage
from adminautomation.utils import NavBarLocators, SidebarLocators
from selenium.webdriver.common.keys import Keys


class AdminPage(BasePage):

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


    def return_to_home_by_navbar_logo(self):
        """
        Clicks the Bypass Admin logo to return to the main dashboard page.
        """

        self.LOGO_HOME_BUTTON.click()


    def expand_venues_list(self):
        """
        Opens the venues list to make the venues list and venue searchbox available.
        """

        if self.VENUE_LIST_DROPDOWN is None:
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
        list_items = self.VENUE_LIST_ITEMS
        for item in list_items:
            if item.text == venue:
                break
            self.VENUE_LIST_SEARCHBOX.send_keys(Keys.ARROW_DOWN)
        else:
            raise ValueError('Could not file venue: {}'.format(venue))

        item.click()


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


    def navigate_to_dashboard(self):
        """
        Navigates to the Dashboard page.
        """

        self.DASHBOARD.click()


    def navigate_to_item_categories(self):
        """
        Navigates to the Item Categories page.
        """

        self.expand_sidebar_tab(self.LOCATION_CONTROL)
        self.expand_sidebar_tab(self.CATEGORIES)
        self.ITEM_CATEGORIES.click()


    def navigate_to_modifier_categories(self):
        """
        Navigates to the Modifier Categories page.
        """

        self.expand_sidebar_tab(self.LOCATION_CONTROL)
        self.expand_sidebar_tab(self.CATEGORIES)
        self.MODIFIER_CATEGORIES.click()


    def navigate_to_groups(self):
        """
        Navigates to the Groups page.
        """

        self.expand_sidebar_tab(self.LOCATION_CONTROL)
        self.GROUPS.click()


    def navigate_to_items(self):
        """
        Navigates to the Items page.
        """

        self.expand_sidebar_tab(self.LOCATION_CONTROL)
        self.ITEMS.click()


    def navigate_to_menus(self):
        """
        Navigates to the Menus page.
        """

        self.expand_sidebar_tab(self.LOCATION_CONTROL)
        self.MENUS.click()


    def navigate_to_locations(self):
        """
        Navigates to the Locations page.
        """

        self.expand_sidebar_tab(self.LOCATION_CONTROL)
        self.LOCATIONS.click()


    def navigate_to_sections(self):
        """
        Navigates to the Sections page.
        """

        self.expand_sidebar_tab(self.LOCATION_CONTROL)
        self.SECTIONS.click()


    def navigate_to_tables(self):
        """
        Navigates to the Tables page.
        """

        self.expand_sidebar_tab(self.LOCATION_CONTROL)
        self.TABLES.click()


    def navigate_to_variant_sets(self):
        """
        Navigates to the Variant Sets page.
        """

        self.expand_sidebar_tab(self.LOCATION_CONTROL)
        self.VARIANT_SETS.click()


    def navigate_to_modifiers(self):
        """
        Navigates to the Modifiers page.
        """

        self.expand_sidebar_tab(self.LOCATION_CONTROL)
        self.MODIFIERS.click()


    def navigate_to_addon_groups(self):
        """
        Navigates to the Addon Groups page.
        """

        self.expand_sidebar_tab(self.LOCATION_CONTROL)
        self.ADDON_GROUPS.click()


    def navigate_to_suites_accounts(self):
        """
        Navigates to the Suites Accounts page.
        """

        self.expand_sidebar_tab(self.SUITES)
        self.SUITES_ACCOUNTS.click()


    def navigate_to_suites_setup(self):
        """
        Navigates to the Suites Setup page.
        """

        self.expand_sidebar_tab(self.SUITES)
        self.SUITES_SETUP.click()


    def navigate_to_suites_preorder(self):
        """
        Navigates to the Suites Pre-Order page.
        """

        self.expand_sidebar_tab(self.SUITES)
        self.SUITES_PREORDER.click()


    def navigate_to_events_calendar(self):
        """
        Navigates to the Events Calendar page.
        """

        self.expand_sidebar_tab(self.EVENTS)
        self.EVENTS_CALENDAR.click()


    def navigate_to_event_templates(self):
        """
        Navigates to the Event Templates page.
        """

        self.expand_sidebar_tab(self.EVENTS)
        self.EVENTS_TEMPLATES.click()


    def navigate_to_orders(self):
        """
        Navigates to the Orders page.
        """

        self.expand_sidebar_tab(self.EVENTS)
        self.ORDERS.click()


    def navigate_to_tips(self):
        """
        Navigates to the Tips page.
        """

        self.expand_sidebar_tab(self.EVENTS)
        self.TIPS.click()


    def navigate_to_cash_room(self):
        """
        Navigates to the Cash Room page.
        """

        self.expand_sidebar_tab(self.EVENTS)
        self.CASHROOM.click()


    def nagivate_to_status(self):
        """
        Navigates to the Status page.
        """

        self.expand_sidebar_tab(self.INVENTORY)
        self.STATUS.click()


    def navigate_to_inventory_categories(self):
        """
        Navigates to the Inventory Categories page.
        """

        self.expand_sidebar_tab(self.INVENTORY)
        self.INVENTORY_CATEGORIES.click()


    def navigate_to_inventory_transfers(self):
        """
        Navigates to the Inventory Transfers page.
        """

        self.expand_sidebar_tab(self.INVENTORY)
        self.INVENTORY_TRANSFERS.click()


    def navigate_to_inventory_movements(self):
        """
        Navigates to the Inventory Movements page.
        """

        self.expand_sidebar_tab(self.INVENTORY)
        self.INVENTORY_MOVEMENTS.click()


    def navigate_to_standsheets(self):
        """
        Navigates to the Standsheets page.
        """

        self.expand_sidebar_tab(self.INVENTORY)
        self.STANDSHEETS.click()


    def navigate_to_stock_items(self):
        """
        Navigates to the Stock Items page.
        """

        self.expand_sidebar_tab(self.INVENTORY)
        self.STOCK_ITEMS.click()


    def navigate_to_recipes(self):
        """
        Navigates to the Recipes page.
        """

        self.expand_sidebar_tab(self.INVENTORY)
        self.RECIPES.click()


    def navigate_to_vendors(self):
        """
        Navigates to the Vendors page.
        """

        self.expand_sidebar_tab(self.INVENTORY)
        self.VENDORS.click()


    def navigate_to_inventory_audits(self):
        """
        Navigates to the Inventory Audits page.
        """

        self.expand_sidebar_tab(self.INVENTORY)
        self.INVENTORY_AUDITS.click()


    def navigate_to_purchasing_and_receiving(self):
        """
        Navigates to the Purchasing & Receiving page.
        """

        self.expand_sidebar_tab(self.INVENTORY)
        self.PURCHASE_AND_RECEIVING.click()


    def navigate_to_warehouses(self):
        """
        Navigates to the Warehouses page.
        """

        self.expand_sidebar_tab(self.INVENTORY)
        self.WAREHOUSES.click()


    def navigate_to_reports(self):
        """
        Navigates to the Reports page.
        """

        self.expand_sidebar_tab(self.REPORTING)
        self.REPORTS.click()


    def navigate_to_report_templates(self):
        """
        Navigates to the Report Templates page.
        """

        self.expand_sidebar_tab(self.REPORTING)
        self.REPORT_TEMPLATES.click()


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
