from adminautomation.pages import AdminPage, DataTablePage
from adminautomation.locators import ItemsLocators


class ItemsPage(AdminPage, DataTablePage):

    PATH = '/items'
    locators = ItemsLocators

    def __init__(self, driver, **kwargs):
        super(ItemsPage, self).__init__(driver, **kwargs)
        self.wait_for_page_to_fully_load()

    @property
    def NEW_ITEM_BUTTON(self):
        return self.get_element(self.locators.NEW_ITEM_BUTTON)

    @property
    def ITEMS_SEARCHBOX(self):
        return self.get_element(self.locators.ITEMS_SEARCHBOX)

    def open_new_item_form(self):
        self.NEW_ITEM_BUTTON.click()
        self.wait_for_page_title('Items - New', timeout=30)

    def search_for_item(self, query):
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
        self.wait_for_elements(ref_element_locator, timeout=timeout)

