import unittest
from basetest import BaseTest
from adminautomation.pages import OrdersPage


class OrdersTest(BaseTest):

    DATA_FILE = './tests/data/orderstests.json'

    def test_reload_table_button_no_changes(self):
        test_data = self.CURRENT_TEST_DATA

        admin = OrdersPage(self.driver, skip_login=True)
        # Get a list of the current order IDs
        pre_refresh_ids = [id_elem.text for id_elem in admin.DATATABLE_ORDER_IDS]
        admin.reload_table()
        post_refresh_ids = [id_elem.text for id_elem in admin.DATATABLE_ORDER_IDS]
        self.assertListEqual(pre_refresh_ids, post_refresh_ids)
