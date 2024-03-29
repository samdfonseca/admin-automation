from adminautomation.pages import AdminPage, DataTablePage
from adminautomation.locators import ItemsLocators
from adminautomation.locators.by import link_text
from adminautomation.utils.api.items import get_items_list


class ItemsPage(AdminPage, DataTablePage):

    PATH = '/items'
    locators = ItemsLocators

    def __init__(self, driver, **kwargs):
        super(ItemsPage, self).__init__(driver, **kwargs)
        self.wait_for_page_to_fully_load()
        self.items = get_items_list(venue_id=self.CURRENT_VENUE_ID)

    @property
    def NEW_ITEM_BUTTON(self):
        return self.get_element(self.locators.NEW_ITEM_BUTTON)

    @property
    def ITEMS_SEARCHBOX(self):
        return self.get_element(self.locators.ITEMS_SEARCHBOX)

    @property
    def BULK_ACTIONS_BUTTON(self):
        return self.get_element(self.locators.BULK_ACTIONS_BUTTON)

    @property
    def BULK_ACTIONS_MENU(self):
        return self.get_element(self.locators.BULK_ACTIONS_MENU)

    @property
    def BULK_ACTIONS_OPTIONS(self):
        return self.get_elements(self.locators.BULK_ACTIONS_OPTIONS)

    def open_new_item_form(self):
        self.NEW_ITEM_BUTTON.click()
        self.wait_for_page_title('Items - New')

    def search_for_item(self, query):
        self.ITEMS_SEARCHBOX.clear()
        self.ITEMS_SEARCHBOX.send_keys(query)

    def sort_header_ascending(self, header_text):
        header = filter(lambda head: head.text == header_text, self.DATATABLE_HEADERS)[0]
        while 'sort-asc' not in header.get_attribute('class').split():
            header.click()

    def sort_header_descending(self, header_text):
        header = filter(lambda head: head.text == header_text, self.DATATABLE_HEADERS)[0]
        while 'sort-desc' not in header.get_attribute('class').split():
            header.click()

    def wait_for_page_to_fully_load(self, **kwargs):
        """Wait for the page to complete any ajax/angular requests. Page should be static once fully loaded.
        Does this by waiting for the existance of an element at the given ref_element_locator.
        """
        ref_element_locator = kwargs.get('ref_element_locator', self.locators.DATATABLE_TABLE_ROWS)
        timeout = kwargs.get('timeout', 30)
        self.wait_for_elements(ref_element_locator)

    def get_item_row_by_name(self, item_name):
        self.wait_for_element(link_text(item_name))
        return self.filter_rows_by_value('Name', item_name)[0]

    def edit_item_by_name(self, item_name):
        item_id = filter(lambda i: i['name'] == item_name, self.items)[0]['id']
        base = self.driver.current_url.replace('#', '')
        base += '/' if not base.endswith('/') else ''
        url = '{0}/edit'.format(item_id)
        self.go_to_url(base, url)

    def click_edit_item_link_by_name(self, item_name):
        item_id = filter(lambda i: i['name'] == item_name, self.items)[0]['id']
        self.get_element(self.locators.EDIT_LINK_PARTIAL_HREF.format(item_id)).click()

    def toggle_take_bulk_actions_menu(self):
        self.BULK_ACTIONS_BUTTON.click()

    def open_take_bulk_actions_menu(self):
        if not self.BULK_ACTIONS_MENU.is_displayed():
            self.toggle_take_bulk_actions_menu()

    def close_take_bulk_actions_menu(self):
        if self.BULK_ACTIONS_MENU.is_displayed():
            self.toggle_take_bulk_actions_menu()
