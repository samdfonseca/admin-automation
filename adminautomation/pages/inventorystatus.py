from adminautomation.pages import AdminPage, BasePage, DataTablePage
from adminautomation.locators import InventoryStatusLocators
from adminautomation.structures.genericstructs import PaginationButtons

from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


class InventoryStatusPage(AdminPage, BasePage, DataTablePage):

    PATH = "/inventory"
    URL_ANCHOR = "#/status/locations"
    locators = InventoryStatusLocators
