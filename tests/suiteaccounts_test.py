#!./runtest

import unittest
from basetest import BaseTest
from adminautomation.pages import SuiteAccountsPage
# from adminautomation.utils.drivers import get_phantomjs_driver as PhantomJSDriver


class SuiteAccountsTest(BaseTest):

    DATA_FILE = "./tests/data/suiteaccountstest.json"


    def test_search_account_name_full_match(self):
        """Search for a Suite Account - Full Match"""
        # Enters a query into the search box and checks that the datatable displays an account
        # with a matching Account Name. Search query should be a full account name.
        #
        # NEEDS TESTRAIL CASE

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True)

        admin.search_for_suite_account(test_data.search_query)

        for account in admin.get_accounts_by_name(test_data.search_query):
            self.assertEqual(account.ACCOUNT_NAME, test_data.search_query)



if __name__ == "__main__":
    unittest.main()