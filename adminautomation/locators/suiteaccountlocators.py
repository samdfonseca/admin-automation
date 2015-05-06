from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import css, xpath


class SuiteAccountsLocators(BaseLocatorGroup):
    NEW_SUITE_ACCOUNT_BUTTON = css('a.new-suite-account')
    ITEMS_PER_PAGE_SELECTOR = css('select[name="suite-accounts-list_length"]')
    ITEMS_PER_PAGE_OPTIONS = css('select[name="suite-accounts-list_length"] option')
    SUITE_ACCOUNTS_SEARCHBOX = css('div#suite-accounts-list_filter input[type="search"]')

    DATATABLE = css('table#suite-accounts-list')
    DATATABLE_HEADERS = css('table#suite-accounts-list thead td')
    DATATABLE_TABLE_ROWS = css('table#suite-accounts-list tbody tr')
    DATATABLE_ROW_ACCOUNT_NAME = css('td:nth-of-type(1)')
    DATATABLE_ROW_SUITE = css('td:nth-of-type(2)')
    DATATABLE_ROW_SUITE_HOLDER = css('td:nth-of-type(3)')
    DATATABLE_ROW_PHONE = css('td:nth-of-type(4)')
    DATATABLE_ROW_EMAIL = css('td:nth-of-type(5)')
    DATATABLE_ROW_EDIT = css('td:nth-of-type(6) a.edit')
    DATATABLE_ROW_DELETE = css('td:nth-of-type(6) a.destroy')

    DATATABLE_FOOTER = css('div#suite-accounts-list_info')
    PAGINATION_BUTTONS = css('ul.pagination')


class ModifySuiteAccountLocators(BaseLocatorGroup):
    PORTLET_TITLE = css('div.portlet-title '
                        'div.caption')
    FORM = css('div#suite-account')
    CANCEL_BUTTON = css('a#cancel')
    SAVE_BUTTON = css('div#save')

    SUITE_ACCOUNT_NAME_INPUT = css('input[ng-model="suite_account.name"]')
    SUITE_TYPE_INPUT = css('input[ng-model="suite_account.suite_type"]')
    BILLING_ADDRESS_INPUT = css('textarea[ng-model="suite_account.address"]')
    NOTES_INPUT = css('textarea[ng-model="suite_account.notes"]')

    SUITE_INPUT = css('div#suite-account '
                      'form div.form-group:nth-of-type(3) '
                      'a.select2-choice')
    SUITE_SELECTOR = css('select[ng-model="suite_account.suite_id"]')
    SUITE_DROPDOWN = css('body '
                         '> div#select2-drop')
    SUITE_DROPDOWN_SEARCHBOX = css('body '
                                   '> div#select2-drop '
                                   '> div.select2-search '
                                   '> input')
    SUITE_DROPDOWN_ITEMS = css('body '
                               '> div#select2-drop '
                               'ul.select2-results '
                               'div.select2-result-label')

    SUITE_HOLDER_LABEL = css('div.suite-holder'
                             'h4')
    SUITE_HOLDER_NEW_CUSTOMER_BUTTON = css('div.suite-holder > '
                                           'div[ng-hide="suite_account.suite_holder"] '
                                           '> button')
    SUITE_HOLDER_INPUT = css('div.suite-holder '
                             'a.select2-choice')
    SUITE_HOLDER_SELECTOR = css('div.suite-holder '
                                'span[ng-show="suiteOwners"] '
                                'select[ng-model="suite_account.suite_holder"]')
    SUITE_HOLDER_DROPDOWN = css('body '
                                '> div#select2-drop')
    SUITE_HOLDER_DROPDOWN_SEARCHBOX = css('body '
                                          '> div#select2-drop '
                                          'div.select2-search '
                                          '> input')
    SUITE_HOLDER_DROPDOWN_ITEMS = css('body '
                                      '> div#select2-drop '
                                      'ul.select2-results '
                                      'div.select2-result-label '
                                      'span.select2-match')

    SUITE_ADMIN_LABEL = css('div.suite-admin '
                            'h4')
    SUITE_ADMIN_NEW_CUSTOMER_BUTTON = css('div.suite-admin '
                                          'div[ng-hide="suite_account.suite_admin"] '
                                          '> button')
    SUITE_ADMIN_INPUT = css('div.suite-admin '
                            'div[ng-hide="suite_account.suite_admin"] '
                            'a.select2-choice')
    SUITE_ADMIN_SELECTOR = css('div.suite-admin '
                               'div[ng-show="suiteOwners"] '
                               'select[ng-model="suite_account.suite_admin"]')
    SUITE_ADMIN_DROPDOWN = css('body '
                               '> div#select2-drop')
    SUITE_ADMIN_DROPDOWN_SEARCHBOX = css('body '
                                         '> div#select2-drop '
                                         'div.select2-search '
                                         '> input')
    SUITE_ADMIN_DROPDOWN_ITEMS = css('body '
                                     '> div#select2-drop '
                                     'ul.select2-results '
                                     'div.select2-result-label '
                                     'span.select2-match')

    AUTHORIZED_SIGNERS_LABEL = css('div.authorized-signers '
                                   'h4')
    AUTHORIZED_SIGNERS_INPUT = css('div.authorized-signers '
                                   'input[ng-model="signer"]')
    AUTHORIZED_SIGNERS_ADD_SIGNERS_BUTTON = css('div.authorized-signers '
                                                'div#add.btn')

    NEW_CUSTOMER_DIALOG = css('body '
                              '> div.modal.fade.in '
                              'div.modal-dialog')
    NEW_CUSTOMER_NAME_LABEL = css('label:contains("Name")')
    NEW_CUSTOMER_NAME_INPUT = css('input[ng-model="customer.name"]')
    NEW_CUSTOMER_EMAIL_LABEL = css('label:contains("Email")')
    NEW_CUSTOMER_EMAIL_INPUT = css('input[ng-model="customer.email"]')
    NEW_CUSTOMER_PHONE_LABEL = css('label:contains("Phone Number")')
    NEW_CUSTOMER_PHONE_INPUT = css('input[ng-model="customer.phone_number"]')
    NEW_CUSTOMER_OFFICE_PHONE_LABEL = css('label:contains("Office Phone")')
    NEW_CUSTOMER_OFFICE_PHONE_INPUT = css('input[ng-model="customer.office_phone"]')
    NEW_CUSTOMER_CANCEL_BUTTON = css('footer.modal-footer '
                                     'div.btn:contains("Cancel")')
    NEW_CUSTOMER_SAVE_CHANGES_BUTTON = css('footer.modal-footer '
                                           'div.btn:contains("Save Changes")')
