from adminautomation.pages import AdminPage, BasePage
from adminautomation.locators import InventoryStatusLocators
from adminautomation.structures.genericstructs import PaginationButtons

from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


class InventoryStatusPage(AdminPage, BasePage):

    PATH = "/inventory"
    URL_ANCHOR = "#/status/locations"
    DATATABLE_COLUMN_MAP = {'Location': 0,
                            'Status': 1,
                            'Location Type'
