import unittest
from urlparse import urljoin
from time import time
import requests
from basetest import BaseTest
from adminautomation.pages import SuiteAccountsPage
# from adminautomation.utils.drivers import get_phantomjs_driver as PhantomJSDriver


class SuiteAccountsTest(BaseTest):

    DATA_FILE = "./tests/data/suiteaccountstest.json"


    # @classmethod
    # def setUpClass(cls):
    #     request_data = {
    #         "suite_account": {
    #             "authorized_signers": [],
    #             "name": "test{0}".format(str(int(time()))),
    #             "suite_id": "3265",
    #             "suite_holder": {
    #                 "id": 1,
    #                 "name": "Doge User",
    #                 "phone_number": "512-555-5555",
    #                 "office_phone": "null",
    #                 "email": "doge@hotmail.com"
    #             },
    #             "suite_admin": {
    #                 "id": 1,
    #                 "name": "Doge User",
    #                 "phone_number": "512-555-5555",
    #                 "office_phone": "null",
    #                 "email": "doge@hotmail.com"
    #             },
    #             "suite_admin_id": 1,
    #             "suite_holder_id": 1
    #         }
    #     }
    #     headers = {
    #         '_session_id': cls.AUTH_COOKIE['value'],
    #     }
    #     url = urljoin(cls.SESSION_INFO['root_url'], 'suite_accounts.json')
    #     resp = requests.post(url=url, headers=headers, json=request_data)
    #     resp.raise_for_status()


    def test_search_account_name_full_match(self):
        """Search for a Suite Account by Account Name - Full Match"""
        # Enters a query into the search box and checks that the datatable displays an account
        # with a matching Account Name. Search query should be a full account name.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True)
        admin.search_for_suite_account(test_data.search_query)
        target = admin.get_account_by_id(test_data.target_account_id)
        self.assertNotIsInstance(target, type(None))
        self.assertEqual(target.ID, test_data.target_account_id)

    def test_search_account_name_partial_match(self):
        """Search for a Suite Account by Account Name - Partial Match"""
        # Enters a query into the search box and checks that the datatable displays an account
        # with a matching Account Name. Search query should be a full account name.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True)
        admin.search_for_suite_account(test_data.search_query)
        target = admin.get_account_by_id(test_data.target_account_id)
        self.assertNotIsInstance(target, type(None))
        self.assertEqual(target.ID, test_data.target_account_id)

    def test_search_suite_full_match(self):
        """Search for a Suite Account by Suite - Full Match"""
        # Enters a query into the search box and checks that the datatable displays an account
        # with a matching Account Name. Search query should be a full account name.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True)
        admin.search_for_suite_account(test_data.search_query)
        # target = admin.get_account_by_id(test_data.search_query)
        target = admin.get_account_by_id(test_data.target_account_id)
        self.assertNotIsInstance(target, type(None))
        self.assertEqual(target.ID, test_data.target_account_id)

    def test_search_suite_partial_match(self):
        """Search for a Suite Account by Suite - Partial Match"""
        # Enters a query into the search box and checks that the datatable displays an account
        # with a matching Account Name. Search query should be a full account name.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True)
        # target = admin.get_account_by_id(test_data.search_query)
        admin.search_for_suite_account(test_data.search_query)
        target = admin.get_account_by_id(test_data.target_account_id)
        self.assertNotIsInstance(target, type(None))
        self.assertEqual(target.ID, test_data.target_account_id)

    def test_search_suite_holder_full_match(self):
        """Search for a Suite Account by Suite Holder - Full Match"""
        # Enters a query into the search box and checks that the datatable displays an account
        # with a matching Account Name. Search query should be a full account name.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True)
        admin.search_for_suite_account(test_data.search_query)
        # target = admin.get_account_by_id(test_data.search_query)
        target = admin.get_account_by_id(test_data.target_account_id)
        self.assertNotIsInstance(target, type(None))
        self.assertEqual(target.ID, test_data.target_account_id)

    def test_search_suite_holder_partial_match(self):
        """Search for a Suite Account by Suite Holder - Partial Match"""
        # Enters a query into the search box and checks that the datatable displays an account
        # with a matching Account Name. Search query should be a full account name.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True)
        admin.search_for_suite_account(test_data.search_query)
        # target = admin.get_account_by_id(test_data.search_query)
        target = admin.get_account_by_id(test_data.target_account_id)
        self.assertNotIsInstance(target, type(None))
        self.assertEqual(target.ID, test_data.target_account_id)

    def test_search_phone_full_match(self):
        """Search for a Suite Account by Phone - Full Match"""
        # Enters a query into the search box and checks that the datatable displays an account
        # with a matching Account Name. Search query should be a full account name.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True)
        admin.search_for_suite_account(test_data.search_query)
        # target = admin.get_account_by_id(test_data.search_query)
        target = admin.get_account_by_id(test_data.target_account_id)
        self.assertNotIsInstance(target, type(None))
        self.assertEqual(target.ID, test_data.target_account_id)

    def test_search_phone_partial_match(self):
        """Search for a Suite Account by Phone - Partial Match"""
        # Enters a query into the search box and checks that the datatable displays an account
        # with a matching Account Name. Search query should be a full account name.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True)
        admin.search_for_suite_account(test_data.search_query)
        # target = admin.get_account_by_id(test_data.search_query)
        target = admin.get_account_by_id(test_data.target_account_id)
        self.assertNotIsInstance(target, type(None))
        self.assertEqual(target.ID, test_data.target_account_id)

    def test_search_email_full_match(self):
        """Search for a Suite Account by Email - Full Match"""
        # Enters a query into the search box and checks that the datatable displays an account
        # with a matching Account Name. Search query should be a full account name.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True)
        admin.search_for_suite_account(test_data.search_query)
        # target = admin.get_account_by_id(test_data.search_query)
        target = admin.get_account_by_id(test_data.target_account_id)
        self.assertNotIsInstance(target, type(None))
        self.assertEqual(target.ID, test_data.target_account_id)

    def test_search_email_partial_match(self):
        """Search for a Suite Account by Email - Partial Match"""
        # Enters a query into the search box and checks that the datatable displays an account
        # with a matching Account Name. Search query should be a full account name.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True)
        admin.search_for_suite_account(test_data.search_query)
        # target = admin.get_account_by_id(test_data.search_query)
        target = admin.get_account_by_id(test_data.target_account_id)
        self.assertNotIsInstance(target, type(None))
        self.assertEqual(target.ID, test_data.target_account_id)

    def test_new_suite_account_button(self):

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True)
        form = admin.get_new_suite_account_form()
        self.assertEqual(form.PORTLET_TITLE.text, test_data.target_form_title)

    def test_new_suite_account_form_cancel_button(self):

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True)
        form = admin.get_new_suite_account_form()
        self.assertEqual(form.PORTLET_TITLE.text, test_data.intermediate_form_title)
        form.cancel_form()
        self.assertEqual(admin.PORTLET_TITLE.text, test_data.target_form_title)


if __name__ == "__main__":
    unittest.main()
