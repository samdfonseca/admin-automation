from selenium.webdriver.support.select import Select
from adminautomation.pages import AdminPage, DataTablePage
from adminautomation.locators.locationslocators import LocationsLocators
from adminautomation.locators.by import link_text


class LocationsPage(AdminPage, DataTablePage):

    PATH = 'locations#/'
    locators = LocationsLocators

    def __init__(self, driver, **kwargs):
        super(LocationsPage, self).__init__(driver, **kwargs)
        self.wait_for_page_to_fully_load()

    @property
    def new_location_button(self):
        return self.get_element(self.locators.new_location_button)

    @property
    def export_button(self):
        return self.get_element(self.locators.EXPORT_BUTTON)

    def open_new_location_form(self):
        self.new_location_button.click()
        self.wait_for_page_title('Locations - New', timeout=10)

    def search_for_location(self, query):
        self.filter_table('Name', query)

    def filter_table_by_type(self, location_type):
        self.show_filters()
        type_column = map(lambda i: i.text, self.DATATABLE_HEADERS).index('Type')
        type_filter = Select(self.DATATABLE_FILTERS[type_column].find_by('css selector', 'select'))
        type_filter.select_by_visible_text(location_type)

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

    def get_row_by_name(self, item_name):
        self.wait_for_element(link_text(item_name))
        return self.filter_rows_by_value('Name', item_name)[0]

    def click_edit_location_link_by_name(self, location_name):
        elem = filter(lambda i: ' '.join(i.text.split()[:-4]) == location_name, self.DATATABLE_TABLE_ROWS)[0]
        elem.find_element_by_link_text('Edit').click()

    def click_delete_location_link_by_name(self, location_name):
        elem = filter(lambda i: ' '.join(i.text.split()[:-4]) == location_name, self.DATATABLE_TABLE_ROWS)[0]
        elem.find_element_by_link_text('Delete').click()

