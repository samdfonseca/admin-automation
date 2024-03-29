# Page object for the Suite Accounts page

from adminautomation.pages import AdminPage, DataTablePage
from adminautomation.locators import SuiteAccountsLocators
from adminautomation.structures.suiteaccountstructs import (SuiteAccountRow,
                                                            NewSuiteAccountForm)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert


class SuiteAccountsPage(AdminPage, DataTablePage):

    PATH = "/suite_accounts"
    locators = SuiteAccountsLocators

    @property
    def NEW_SUITE_ACCOUNT_BUTTON(self):
        return self.get_element(self.locators.NEW_SUITE_ACCOUNT_BUTTON)

    @property
    def ITEMS_PER_PAGE_OPTIONS(self):
        return self.get_elements(self.locators.ITEMS_PER_PAGE_OPTIONS)

    @property
    def SUITE_ACCOUNT_SEARCHBOX(self):
        return self.get_element(self.locators.SUITE_ACCOUNTS_SEARCHBOX)

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
    def DATATABLE_TABLE_ROWS(self):
        trs = self.get_elements(self.locators.DATATABLE_TABLE_ROWS)
        return map(SuiteAccountRow, trs)

    # @property
    # def DATATABLE(self):
    #     return self.get_element(self.locators.DATATABLE)

    # @property
    # def DATATABLE_HEADERS(self):
    #     return self.get_elements(self.locators.DATATABLE_HEADERS)

    # @property
    # def ITEMS_PER_PAGE_SELECTOR(self):
    #     return self.get_element(self.locators.ITEMS_PER_PAGE_SELECTOR)

    # @property
    # def DATATABLE_FOOTER(self):
    #     return self.get_element(self.locators.DATATABLE_FOOTER)

    # @property
    # def PAGINATION_BUTTONS(self):
    #     return self.get_elements(self.locators.PAGINATION_BUTTONS)

    def change_items_per_page(self, target_option):
        Select(self.ITEMS_PER_PAGE_SELECTOR).select_by_visible_text(str(target_option))

    def clear_suite_account_searchbox(self):
        self.SUITE_ACCOUNT_SEARCHBOX.send_keys(Keys.ESCAPE)

    def search_for_suite_account(self, query):
        self.clear_suite_account_searchbox()
        self.SUITE_ACCOUNT_SEARCHBOX.send_keys(query)

    @staticmethod
    def sort_by_header_ascending(header):
        # Raises an exception if headers parent element is not a thead
        if header.find_element_by_xpath("../..").tag_name != "thead":
            raise Exception('Not a valid datatable header element.')

        if "sorting_asc" not in header.get_attribute("class").split(" "):
            header.click()

    @staticmethod
    def sort_by_header_descending(header):
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
    def select_edit_suite_account_in_row(row):
        selector = SuiteAccountsLocators.DATATABLE_ROW_EDIT
        row.find_element(*selector).click()

    def get_edit_suite_account_form_by_id(self, account_id):
        account = self.get_account_by_id(account_id)
        self.select_edit_suite_account_in_row(account.ROW)
        return NewSuiteAccountForm(self.driver)

    @staticmethod
    def select_delete_suite_account_in_row(row):
        selector = SuiteAccountsLocators.DATATABLE_ROW_DELETE
        row.find_element(*selector).click()

    def accept_delete_suite_account_alert(self):
        Alert(self.driver).accept()

    def delete_suite_account_by_id(self, account_id):
        account = self.get_account_by_id(account_id)
        self.select_delete_suite_account_in_row(account.ROW)
        self.accept_delete_suite_account_alert()

    def get_accounts_by_name(self, account_name):
        return filter(lambda row: row.ACCOUNT_NAME == account_name, self.DATATABLE_TABLE_ROWS)

    def get_accounts_by_email(self, email):
        return filter(lambda row: row.EMAIL == email, self.DATATABLE_TABLE_ROWS)

    def get_accounts_by_suite_holder(self, suite_holder):
        return filter(lambda row: row.SUITE_HOLDER == suite_holder, self.DATATABLE_TABLE_ROWS)

    def get_accounts_by_phone(self, phone):
        return filter(lambda row: row.PHONE == phone, self.DATATABLE_TABLE_ROWS)

    def get_accounts_by_suite(self, suite):
        return filter(lambda row: row.SUITE == suite, self.DATATABLE_TABLE_ROWS)

    def get_account_by_id(self, id):
        for account in self.DATATABLE_TABLE_ROWS:
            if account.ID == id:
                return account
        else:
            return None

    def get_new_suite_account_form(self):
        self.NEW_SUITE_ACCOUNT_BUTTON.click()
        return NewSuiteAccountForm(self.driver)

