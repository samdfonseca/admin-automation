from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import *
from adminautomation.structures import AdminElement


class DataTableLocators(BaseLocatorGroup):
    HEADERS = css("thead > tr:nth-child(1) th")
    FILTERS = css("thead > tr:nth-child(2) th")
    ROWS = css("tbody > tr")


# class DataTableRowLocators(BaseLocatorGroup):


class DataTable(AdminElement):
    def __init__(self, webelement):
        self.elem = webelement
        self.driver = self.elem.parent
    
    @property
    def headers(self):
        return self.get_elements(DataTableLocators.HEADERS)

    @property
    def filters(self):
        return self.get_elements(DataTableLocators.FILTERS)

    @property
    def rows(self):
        return self.get_elements(DataTableLocators.ROWS)


