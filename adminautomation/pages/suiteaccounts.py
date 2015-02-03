

from adminautomation.pages import AdminPage, BasePage
from adminautomation.utils.locators import SuiteAccountsLocators
from adminautomation.stuctures import SuiteAccountRow
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert


class SuiteAccountsPage(AdminPage, BasePage):

    PATH = "/suite_accounts"

    @property
    def NEW_SUITE_ACCOUNT_BUTTON(self):
        return self.get_element(SuiteAccountsLocators.NEW_SUITE_ACCOUNT_BUTTON)


    @property
    def ITEMS_PER_PAGE_SELECTOR(self):
        return self.get_element(SuiteAccountsLocators.ITEMS_PER_PAGE_SELECTOR)


    @property
    def ITEMS_PER_PAGE_OPTIONS(self):
        return self.get_elements(SuiteAccountsLocators.ITEMS_PER_PAGE_OPTIONS)


    @property
    def SUITE_ACCOUNT_SEARCHBOX(self):
        return self.get_element(SuiteAccountsLocators.SUITE_ACCOUNTS_SEARCHBOX)


    @property
    def DATATABLE(self):
        return self.get_element(SuiteAccountsLocators.DATATABLE)


    @property
    def DATATABLE_HEADERS(self):
        return self.get_elements(SuiteAccountsLocators.DATATABLE_HEADERS)


    @property
    def DATATABLE_ACCOUNT_NAME_HEADER(self):
        return filter(lambda elem: elem.text == "Account Name", self.DATATABLE_HEADERS)[0]


    @property
    def DATATABLE_SUITE_HEADER(self):
        return filter(lambda elem: elem.text == "Suite", self.DATATABLE_HEADERS)[0]


    @property
    def DATATABLE_SUITE_HOLDER_HEADER(self):
        return filter(lambda elem: elem.text == "Suite Holder", self.DATATABLE_HEADERS)[0]


    @property
    def DATATABLE_PHONE_HEADER(self):
        return filter(lambda elem: elem.text == "Phone", self.DATATABLE_HEADERS)[0]


    @property
    def DATATABLE_EMAIL_HEADER(self):
        return filter(lambda elem: elem.text == "Email", self.DATATABLE_HEADERS)[0]


    @property
    def DATATABLE_EDIT_HEADER(self):
        return filter(lambda elem: elem.text == "Edit", self.DATATABLE_HEADERS)[0]


    @property
    def DATATABLE_ROWS(self):
        trs = self.get_elements(SuiteAccountsLocators.DATATABLE_ROWS)
        return map(SuiteAccountRow, trs)


    @property
    def DATATABLE_FOOTER(self):
        return self.get_element(SuiteAccountsLocators.DATATABLE_FOOTER)


    @property
    def PAGINATION_BUTTONS(self):
        return self.get_elements(SuiteAccountsLocators.PAGINATION_BUTTONS)


    def change_items_per_page(self, target_option):
        Select(self.ITEMS_PER_PAGE_SELECTOR).select_by_visible_text(str(target_option))


    def clear_suite_account_searchbox(self):
        self.SUITE_ACCOUNT_SEARCHBOX.send_keys(Keys.ESCAPE)


    def search_for_suite_account(self, query):
        self.clear_suite_account_searchbox()
        self.SUITE_ACCOUNT_SEARCHBOX.send_keys(query)


    def sort_by_header_ascending(self, header):
        # Raises an exception if headers parent element is not a thead
        if header.find_element_by_xpath("../..").tag_name != "thead":
            raise Exception('Not a valid datatable header element.')

        if "sorting_asc" not in header.get_attribute("class").split(" "):
            header.click()


    @staticmethod
    def sort_by_header_descending(self, header):
        # Raises an exception if headers parent element is not a thead
        if header.find_element_by_xpath("../..").tag_name != "thead":
            raise Exception('Not a valid datatable header element.')

        if "sorting_asc" in header.get_attribute("class").split(" "):
            header.click()
        elif "sorting" in header.get_attribute("class").split(" "):
            header.click()
            header.click()


    def select_pagination_button_by_text(self, button_text):
        match_button = filter(lambda element: element.text == str(button_text), self.PAGINATION_BUTTONS)[0]
        match_button.click()


    @staticmethod
    def select_edit_suite_account_in_row(self, row):
        selector = SuiteAccountsLocators.DATATABLE_ROW_EDIT
        row.find_element(*selector).click()


    @staticmethod
    def select_delete_suite_account_in_row(self, row):
        selector = SuiteAccountsLocators.DATATABLE_ROW_DELETE
        row.find_element(*selector).click()


    def accept_delete_suite_account_alert(self):
        Alert(self.driver).accept()


    def get_accounts_by_name(self, account_name):
        return filter(lambda row: row.ACCOUNT_NAME == account_name, self.DATATABLE_ROWS)


    def get_accounts_by_email(self, email):
        return filter(lambda row: row.EMAIL == email, self.DATATABLE_ROWS)

