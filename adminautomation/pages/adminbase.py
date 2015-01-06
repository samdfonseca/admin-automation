# Base page for all logged-in Admin pages

from adminautomation.pages import BasePage
from adminautomation.utils import NavBarLocators, SidebarLocators


class AdminPage(BasePage):

    @property
    def LOGO_HOME_BUTTON(self):
        return self.get_element(NavBarLocators.LOGO_HOME_BUTTON)


    @property
    def VENUES_LISTBOX(self):
        return self.get_element(NavBarLocators.VENUES_LISTBOX)


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
