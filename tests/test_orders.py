from requests.exceptions import HTTPError
from hamcrest import *
from selenium.webdriver.remote.webelement import WebElement
import nose.tools

from basetest import BaseTest
from adminautomation.pages import OrdersPage
from adminautomation.utils.api.orders import new_cash_order


class OrdersTest(BaseTest):

    DATA_FILE = './tests/data/orderstests.json'

    def test_reload_table_button_no_changes(self):
        test_data = self.CURRENT_TEST_DATA

        admin = OrdersPage(self.driver, skip_login=True)
        admin.driver.implicitly_wait(10)
        pre_refresh_ids = [id_elem.text for id_elem in admin.DATATABLE_ORDER_IDS]
        admin.reload_table()
        admin.sleep(2)
        post_refresh_ids = [id_elem.text for id_elem in admin.DATATABLE_ORDER_IDS]
        assert_that(post_refresh_ids, is_(pre_refresh_ids))

    def test_reload_table_button_new_order(self):
        test_data = self.CURRENT_TEST_DATA

        admin = OrdersPage(self.driver, skip_login=True)
        order = new_cash_order(base_url=self.SESSION_INFO['api_server'],
                               auth_server=self.SESSION_INFO['auth_server'],
                               user=self.SESSION_INFO['user'],
                               password=self.SESSION_INFO['passwd'],
                               venue_id=self.SESSION_INFO['default_venue'])
        admin.reload_table()
        admin.wait_for_element(admin.locators.DATATABLE + ' a[href="/orders/{0}"]'.format(order['id']))
        assert_that(admin.get_order_id_links_by_link_text(order['id'])[0], is_(WebElement))
