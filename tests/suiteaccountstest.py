#!./runtest

import unittest
from tests import BaseTest
from adminautomation.pages import SuiteAccountsPage
from adminautomation.utils.drivers import get_phantomjs_driver as PhantomJSDriver


class SuiteAccountsTest(BaseTest):

    DATA_FILE = "./data/suiteaccountstest.json"


    def test_search_account_name_full_match(self):
        # Enters a query into the search box and checks that the datatable displays an account
        # with a matching Account Name. Search query should be a full account name.

        test_data = self.CURRENT_TEST_DATA

        admin = SuiteAccountsPage(self.driver, skip_login=True, root_url="https://admin.alpha.bypasslane.com")

        admin.search_for_suite_account(test_data.search_query)

        for account in admin.get_accounts_by_name(test_data.search_query):
            self.assertEqual(account.ACCOUNT_NAME, test_data.search_query)



if __name__ == "__main__":
    unittest.main()