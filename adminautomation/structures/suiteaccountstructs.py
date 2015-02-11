from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.select import Select
from adminautomation.utils.locators import SuiteAccountsLocators, ModifySuiteAccountLocators, AdminPageLocators
from time import sleep


class SuiteAccountRow(object):
    # Not sure if having sub-page objects are a good idea. May complicate things.
    def __init__(self, table_row):
        self.ROW = table_row
        self.ACCOUNT_NAME = self._get_cell_text(SuiteAccountsLocators.DATATABLE_ROW_ACCOUNT_NAME)
        self.SUITE = self._get_cell_text(SuiteAccountsLocators.DATATABLE_ROW_SUITE)
        self.SUITE_HOLDER = self._get_cell_text(SuiteAccountsLocators.DATATABLE_ROW_SUITE_HOLDER)
        self.PHONE = self._get_cell_text(SuiteAccountsLocators.DATATABLE_ROW_PHONE)
        self.EMAIL = self._get_cell_text(SuiteAccountsLocators.DATATABLE_ROW_EMAIL)

        self._EDIT_LINK = table_row.find_element(*SuiteAccountsLocators.DATATABLE_ROW_EDIT)
        self._DELETE_LINK = table_row.find_element(*SuiteAccountsLocators.DATATABLE_ROW_DELETE)

        self.ID = self._DELETE_LINK.get_attribute("href").split("/")[-1]  # The number at the end of the delete link url

    def _get_cell_text(self, locator):
        return self.ROW.find_element(*locator).text

    def delete_account(self):
        self._DELETE_LINK.click()

    def edit_account(self):
        self._EDIT_LINK.click()


class NewSuiteAccountForm(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def FORM(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ModifySuiteAccountLocators.FORM))

    @property
    def PORTLET_TITLE(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.PORTLET_TITLE)

    @property
    def CANCEL_BUTTON(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.CANCEL_BUTTON)

    @property
    def SAVE_BUTTON(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.SAVE_BUTTON)

    @property
    def SUITE_ACCOUNT_NAME_INPUT(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.SUITE_ACCOUNT_NAME_INPUT)

    @property
    def SUITE_TYPE_INPUT(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.SUITE_TYPE_INPUT)

    @property
    def SUITE_INPUT(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.SUITE_INPUT)

    @property
    def SUITE_INPUT_SELECTOR(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.SUITE_SELECTOR)

    @property
    def SUITE_INPUT_DROPDOWN(self):
        try:
            self.SUITE_INPUT.click()
        except WebDriverException:
            pass
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ModifySuiteAccountLocators.SUITE_DROPDOWN))
        # return self.FORM.find_element(*ModifySuiteAccountLocators.SUITE_INPUT_DROPDOWN)

    @property
    def SUITE_INPUT_DROPDOWN_SEARCHBOX(self):
        return self.SUITE_INPUT_DROPDOWN.find_element(*ModifySuiteAccountLocators.SUITE_DROPDOWN_SEARCHBOX)

    @property
    def SUITE_INPUT_DROPDOWN_ITEMS(self):
        return self.SUITE_INPUT_DROPDOWN.find_elements(*ModifySuiteAccountLocators.SUITE_DROPDOWN_ITEMS)

    @property
    def BILLING_ADDRESS_INPUT(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.BILLING_ADDRESS_INPUT)

    @property
    def NOTES_INPUT(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.NOTES_INPUT)

    @property
    def SUITE_HOLDER_NEW_CUSTOMER_BUTTON(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.SUITE_HOLDER_NEW_CUSTOMER_BUTTON)

    @property
    def SUITE_HOLDER_INPUT(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.SUITE_HOLDER_INPUT)

    @property
    def SUITE_HOLDER_SELECTOR(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.SUITE_HOLDER_SELECTOR)

    @property
    def SUITE_HOLDER_DROPDOWN(self):
        try:
            self.SUITE_HOLDER_INPUT.click()
        except WebDriverException:
            pass
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ModifySuiteAccountLocators.SUITE_HOLDER_DROPDOWN))
        # return self.FORM.find_element(*ModifySuiteAccountLocators.SUITE_HOLDER_DROPDOWN)

    @property
    def SUITE_HOLDER_DROPDOWN_SEARCHBOX(self):
        return self.SUITE_HOLDER_DROPDOWN.find_element(*ModifySuiteAccountLocators.SUITE_HOLDER_DROPDOWN_SEARCHBOX)

    @property
    def SUITE_HOLDER_DROPDOWN_ITEMS(self):
        return self.SUITE_HOLDER_DROPDOWN.find_elements(*ModifySuiteAccountLocators.SUITE_HOLDER_DROPDOWN_ITEMS)

    @property
    def SUITE_ADMIN_NEW_CUSTOMER_BUTTON(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.SUITE_ADMIN_NEW_CUSTOMER_BUTTON)

    @property
    def SUITE_ADMIN_INPUT(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.SUITE_ADMIN_INPUT)

    @property
    def SUITE_ADMIN_SELECTOR(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.SUITE_ADMIN_SELECTOR)

    @property
    def SUITE_ADMIN_DROPDOWN(self):
        try:
            self.SUITE_ADMIN_INPUT.click()
        except WebDriverException:
            pass
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ModifySuiteAccountLocators.SUITE_ADMIN_DROPDOWN))

    @property
    def SUITE_ACCOUNT_DROPDOWN_SEARCHBOX(self):
        return self.SUITE_ADMIN_DROPDOWN.find_element(*ModifySuiteAccountLocators.SUITE_ADMIN_DROPDOWN_SEARCHBOX)

    @property
    def SUITE_ACCOUNT_DROPDOWN_ITEMS(self):
        return self.SUITE_ADMIN_DROPDOWN.find_elements(*ModifySuiteAccountLocators.SUITE_ADMIN_DROPDOWN_ITEMS)

    @property
    def AUTHORIZED_SIGNERS_INPUT(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.AUTHORIZED_SIGNERS_INPUT)

    @property
    def AUTHORIZED_SIGNERS_ADD_SIGNERS_BUTTON(self):
        return self.FORM.find_element(*ModifySuiteAccountLocators.AUTHORIZED_SIGNERS_ADD_SIGNERS_BUTTON)

    def fill_form(self, **kwargs):
        """
        Fills the New Suite Account/Modify Suite Account form.

        :param suite_account_name: The name to enter into the Suite Account Name field as a string.
        :param suite_type: The suite type to enter into the Suite Type field as a string.
        :param suite: The name of the suite to attach to the Suite Account as a string.
        :param billing_address: The billing address of the Suite Account as as string.
        :param notes: Notes to attach to the Suite Account as a string.
        :param suite_holder: The name of the Suite Holder associated with the Suite Account as a string.
        :param suite_admin: The name of the Suite Admin associated with the Suite Account as a string.
        :param authorized_signers: The names of the Authorized Signers on the Suite Account as a list of strings.
        """
        suite_account_name = kwargs.get("suite_account_name")
        suite_type = kwargs.get("suite_type")
        suite = kwargs.get("suite")
        billing_address = kwargs.get("billing_address")
        notes = kwargs.get("notes")
        suite_holder = kwargs.get("suite_holder")
        suite_admin = kwargs.get("suite_admin")
        authorized_signers = kwargs.get("authorized_signers")

        if suite_account_name is not None:
            self.fill_suite_account_name(suite_account_name)
        if suite_type is not None:
            self.fill_suite_type(suite_type)
        if suite is not None:
            self.fill_suite(suite)
        if billing_address is not None:
            self.fill_billing_address(billing_address)
        if notes is not None:
            self.fill_notes(notes)
        if suite_holder is not None:
            self.fill_suite_holder(suite_holder)
        if suite_admin is not None:
            self.fill_suite_admin(suite_admin)
        if authorized_signers is not None:
            for signer in authorized_signers:
                self.add_authorized_signer(signer)

    def fill_suite_account_name(self, suite_account_name):
        self.SUITE_ACCOUNT_NAME_INPUT.clear()
        self.SUITE_ACCOUNT_NAME_INPUT.send_keys(suite_account_name)

    def fill_suite_type(self, suite_type):
        self.SUITE_TYPE_INPUT.clear()
        self.SUITE_TYPE_INPUT.send_keys(suite_type)

    def fill_suite(self, suite):
        Select(self.SUITE_INPUT_SELECTOR).select_by_visible_text(suite)

    def fill_billing_address(self, address):
        self.BILLING_ADDRESS_INPUT.clear()
        self.BILLING_ADDRESS_INPUT.send_keys(address)

    def fill_notes(self, notes):
        self.NOTES_INPUT.clear()
        self.NOTES_INPUT.send_keys(notes)

    def fill_suite_holder(self, suite_holder):
        Select(self.SUITE_HOLDER_SELECTOR).select_by_visible_text(suite_holder)

    def fill_suite_admin(self, suite_admin):
        Select(self.SUITE_ADMIN_SELECTOR).select_by_visible_text(suite_admin)

    def add_authorized_signer(self, signer):
        self.AUTHORIZED_SIGNERS_INPUT.clear()
        self.AUTHORIZED_SIGNERS_INPUT.send_keys(signer)
        self.AUTHORIZED_SIGNERS_ADD_SIGNERS_BUTTON.click()

    def save_form(self):
        self.SAVE_BUTTON.click()

    def cancel_form(self):
        self.CANCEL_BUTTON.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(AdminPageLocators.PORTLET_TITLE))
        #sleep(1)


class EditSuiteAccountForm(NewSuiteAccountForm):
    pass


class NewCustomerDialog(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def DIALOG(self):
        return self.driver.find_element(*ModifySuiteAccountLocators.NEW_CUSTOMER_DIALOG)

    @property
    def NAME_INPUT(self):
        return self.DIALOG.find_element(*ModifySuiteAccountLocators.NEW_CUSTOMER_NAME_INPUT)

    @property
    def EMAIL_INPUT(self):
        return self.DIALOG.find_element(*ModifySuiteAccountLocators.NEW_CUSTOMER_EMAIL_INPUT)

    @property
    def PHONE_INPUT(self):
        return self.DIALOG.find_element(*ModifySuiteAccountLocators.NEW_CUSTOMER_PHONE_INPUT)

    @property
    def OFFICE_PHONE_INPUT(self):
        return self.DIALOG.find_element(*ModifySuiteAccountLocators.NEW_CUSTOMER_OFFICE_PHONE_INPUT)

    @property
    def CANCEL_BUTTON(self):
        return self.DIALOG.find_element(*ModifySuiteAccountLocators.NEW_CUSTOMER_CANCEL_BUTTON)

    @property
    def SAVE_CHANGES_BUTTON(self):
        return self.DIALOG.find_element(*ModifySuiteAccountLocators.NEW_CUSTOMER_SAVE_CHANGES_BUTTON)


class EditCustomerDialog(NewCustomerDialog):
    pass
