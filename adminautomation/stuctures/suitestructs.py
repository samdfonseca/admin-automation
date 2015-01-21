from adminautomation.utils.locators import SuiteAccountsLocators as Locators

class SuiteAccountRow(object):
    # Not sure if having sub-page objects are a good idea. May complicate things.
    def __init__(self, table_row):
        self._ROW = table_row
        self.ACCOUNT_NAME = self._get_cell_text(Locators.DATATABLE_ROW_ACCOUNT_NAME)
        self.SUITE = self._get_cell_text(Locators.DATATABLE_ROW_SUITE)
        self.SUITE_HOLDER = self._get_cell_text(Locators.DATATABLE_ROW_SUITE_HOLDER)
        self.PHONE = self._get_cell_text(Locators.DATATABLE_ROW_PHONE)
        self.EMAIL = self._get_cell_text(Locators.DATATABLE_ROW_EMAIL)

        # self._EDIT_LINK = table_row.find_element(*Locators.DATATABLE_ROW_EDIT).find_element_by_css_selector("a.edit")
        # self._DELETE_LINK = table_row.find_element(*Locators.DATATABLE_ROW_EDIT).find_element_by_css_selector("a.destroy")
        self._EDIT_LINK = table_row.find_element(*Locators.DATATABLE_ROW_EDIT)
        self._DELETE_LINK = table_row.find_element(*Locators.DATATABLE_ROW_DELETE)


    def _get_cell_text(self, locator):
        return self._ROW.find_element(*locator).text


    def delete_account(self):
        self._DELETE_LINK.click()


    def edit_account(self):
        self._EDIT_LINK.click()
