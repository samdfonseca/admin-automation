from hamcrest import *
from selenium.common.exceptions import StaleElementReferenceException

from basetest import BaseTest
from adminautomation.pages import ItemsPage
from bypassqatesting.api.items import get_item_count, get_items_list


class ItemsTest(BaseTest):

    DATA_FILE = './tests/data/itemstests.json'

    @staticmethod
    def search_for_item(admin, search_query, target_item_name):
        admin.search_for_item(search_query)
        row = admin.get_item_row_by_name(target_item_name)
        assert(row.text, starts_with(target_item_name))

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
        assert(sorted_item_names, contains(displayed_item_names))

    def test_search_for_item_partial_match(self):
        admin = ItemsPage(self.driver, skip_login=True)
        admin.show_filters()
        admin.filter_table('Name', self.CURRENT_TEST_DATA.search_query)
        admin.sleep(2)
        rows = admin.filter_rows_by_value('Name', self.CURRENT_TEST_DATA.target_item_name)
        assert_that(self.CURRENT_TEST_DATA.target_item_name, is_in(map(lambda i: i.text, rows)))
        # assert_that(len(rows), greater_than_or_equal_to(1))

    def test_search_for_item_partial_nonstarting_match(self):
        admin = ItemsPage(self.driver, skip_login=True)
        admin.show_filters()
        admin.filter_table('Name', self.CURRENT_TEST_DATA.search_query)
        admin.sleep(2)
        rows = admin.filter_rows_by_value('Name', self.CURRENT_TEST_DATA.target_item_name)
        assert_that(self.CURRENT_TEST_DATA.target_item_name, is_in(map(lambda i: i.text, rows)))
        # assert_that(len(rows), greater_than_or_equal_to(1))

    def test_search_for_item_full_match(self):
        admin = ItemsPage(self.driver, skip_login=True)
        admin.show_filters()
        admin.filter_table('Name', self.CURRENT_TEST_DATA.search_query)
        admin.sleep(2)
        rows = admin.filter_rows_by_value('Name', self.CURRENT_TEST_DATA.target_item_name)
        assert_that(self.CURRENT_TEST_DATA.target_item_name, is_in(map(lambda i: i.text, rows)))
        # assert_that(len(rows), greater_than_or_equal_to(1))

    # def test_search(self):
    #     admin = ItemsPage(self.driver, skip_login=True)
    #     for test_method in filter(lambda i: i.startswith('test_search'), self.TEST_DATA):
    #         yield ItemsTest.search_for_item, admin, self.TEST_DATA[test_method].search_query, self.TEST_DATA[test_method].target_item_name

    def test_sort_items_by_name_ascending(self):
        self.sort_items_by_header('Name', ascending=True)

    def test_sort_items_by_name_descending(self):
        self.sort_items_by_header('Name', ascending=False)

