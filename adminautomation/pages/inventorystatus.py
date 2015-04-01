from adminautomation.pages import AdminPage, BasePage, DataTablePage
from adminautomation.locators import InventoryStatusLocators


class InventoryStatusPage(AdminPage, DataTablePage, BasePage):

    PATH = "/inventory"
    URL_ANCHOR = "#/status/locations"
    locators = InventoryStatusLocators
