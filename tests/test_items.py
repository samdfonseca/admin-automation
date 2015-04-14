import operator
from hamcrest import *
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement

from basetest import BaseTest
from adminautomation.pages import ItemsPage
from adminautomation.utils.api.items import get_item_count, get_items_list


class ItemsTest(BaseTest):

    DATA_FILE = './tests/data/itemstests.json'

    def search_for_item(self, admin, test_data):
        admin.search_for_item(test_data.search_query)
        row = admin.get_item_row_by_name(test_data.target_item_name)
        assert(row.text, starts_with(test_data.target_item_name))

    def sort_items_by_header(self, header_text, ascending=True):
        header_to_key_dict = {
            'Name': 'name',
            'Category': 'category_name',
            'Reporting Group': 'reporting_group_name',
            'Price': 'base_price',
        }
        admin = ItemsPage(self.driver, skip_login=True)
        sort_func = [admin.sort_header_descending, admin.sort_header_ascending][ascending]
        sort_func(header_text)
        admin.sleep(2)

        sorted_items = sorted(admin.items, key=lambda item: item[header_to_key_dict[header_text]].lower())
        sorted_item_names = map(lambda item: item['name'], sorted_items)
        while True:
            try:
                displayed_item_names = map(lambda item: item.text,
                                           admin.DATATABLE.find_elements(*admin.locators.ROW_ITEM_NAME_LINK))
            except StaleElementReferenceException:
                admin.sleep(.5)
            else:
                break
        print(sorted_item_names[:len(displayed_item_names)])
        print(displayed_item_names)
        assert(sorted_item_names, contains(displayed_item_names))


    def test_search_for_item_partial_match(self):
        self.search_for_item(self.CURRENT_TEST_DATA)

    def test_search_for_item_full_match(self):
        admin = ItemsPage(self.driver, skip_login=True)


        self.search_for_item(self.CURRENT_TEST_DATA)

    def test_sort_items_by_name_ascending(self):
        self.sort_items_by_header('Name', ascending=True)

    def test_sort_items_by_name_descending(self):
        self.sort_items_by_header('Name', ascending=False)
