from urlparse import urlparse, urljoin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from adminautomation.pages import AdminPage, DataTablePage
from adminautomation.locators.by import css
from adminautomation.locators.locationslocators import LocationsLocators, NewLocationFormLocators
from adminautomation.locators.by import link_text
from adminautomation.structures import Select2


class LocationsPage(AdminPage, DataTablePage):

    PATH = 'locations#/'
    locators = LocationsLocators

    def __init__(self, driver, **kwargs):
        super(LocationsPage, self).__init__(driver, **kwargs)
        self.wait_for_page_to_fully_load()

    @property
    def new_location_button(self):
        return self.get_element(self.locators.NEW_LOCATION_BUTTON)

    @property
    def export_button(self):
        return self.get_element(self.locators.EXPORT_BUTTON)

    @property
    def alert(self):
        return Alert(self.driver)

    def open_new_location_form(self):
        self.new_location_button.click()
        self.wait_for_page_title('Locations - New', timeout=10)

    def search_for_location(self, query):
        self.filter_table('Name', query)
        # self.wait_for_table_load_after_filter()
        # self.wait_for_elements(self.locators.DATATABLE_TABLE_ROWS)

    def filter_table_by_type(self, location_type):
        self.show_filters()
        type_filter = Select(self.get_filter_input_by_column_header_text('Type'))
        type_filter.select_by_visible_text(location_type)
        self.wait_for_table_load_after_filter()

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
        ref_element_locator = kwargs.get('ref_element_locator', css('tr[ng-repeat="location in locations"]'))
        self.wait_for_elements(ref_element_locator)

    def get_row_by_name(self, location_name):
        # Fuck this is slow...
        elem = filter(lambda i: ' '.join(i.text.split()[:-4]) == location_name if 'Vending' not in i.text else ' '.join(i.text.split()[:-5]) == location_name, self.DATATABLE_TABLE_ROWS)[0]
        return elem

    def click_edit_location_link_by_name(self, location_name):
        elem = self.get_row_by_name(location_name)
        if not elem.is_displayed():
            self.scroll_into_view(elem)
        elem.find_element_by_link_text('Edit').click()

    def click_delete_location_link_by_name(self, location_name):
        elem = self.get_row_by_name(location_name)
        if not elem.is_displayed():
            self.scroll_into_view(elem)
        elem.find_element_by_link_text('Delete').click()

    def accept_alert(self):
        self.alert.accept()

    def dismiss_alert(self):
        self.alert.dismiss()


class NewLocationPage(AdminPage):
    PATH = 'locations/new'
    locators = NewLocationFormLocators

    @property
    def name_input(self):
        return self.get_element(self.locators.NAME_INPUT)

    @property
    def name(self):
        return self.name_input.get_attribute('value')

    @property
    def description_input(self):
        return self.get_element(self.locators.DESCRIPTION_INPUT)

    @property
    def description(self):
        return self.description_input.get_attribute('value')

    @property
    def type_select(self):
        return Select2(self.get_element(self.locators.TYPE_SELECT))

    @property
    def type(self):
        return self.type_select.select.first_selected_option.text.strip()

    @property
    def location_group_select(self):
        return Select2(self.get_element(self.locators.LOCATION_GROUP_SELECT))

    @property
    def location_group(self):
        return self.location_group_select.select.first_selected_option.text

    @property
    def default_transfer_source_select(self):
        return Select2(self.get_element(self.locators.DEFAULT_TRANSFER_SOURCE_SELECT))

    @property
    def location_tags_input(self):
        return self.get_element(self.locators.LOCATION_TAGS_INPUT)

    @property
    def closed_radio_button(self):
        return self.get_element(self.locators.CLOSED_RADIO_BUTTON)

    @property
    def open_radio_button(self):
        return self.get_element(self.locators.OPEN_RADIO_BUTTON)

    @property
    def inseat_delivery_checkbox(self):
        return self.get_element(self.locators.INSEAT_DELIVERY_CHECKBOX)

    @property
    def has_pickup_checkbox(self):
        return self.get_element(self.locators.HAS_PICKUP_CHECKBOX)

    @property
    def merchandise_checkbox(self):
        return self.get_element(self.locators.MERCHANDISE_CHECKBOX)

    @property
    def payment_type_checkboxes(self):
        return self.get_elements(self.locators.PAYMENT_TYPE_CHECKBOXES)

    @property
    def print_receipts_twice_checkbox(self):
        return self.get_element(self.locators.PRINT_RECEIPT_TWICE_CHECKBOX)

    @property
    def auto_print_cash_orders_checkbox(self):
        return self.get_element(self.locators.AUTO_PRINT_CASH_ORDERS_CHECKBOX)

    @property
    def accept_digital_signatures_checkbox(self):
        return self.get_element(self.locators.ACCEPT_DIGITAL_SIGNATURES_CHECKBOX)

    @property
    def auto_print_credit_orders_checkbox(self):
        return self.get_element(self.locators.AUTO_PRINT_CREDIT_ORDERS_CHECKBOX)

    @property
    def auto_print_remote_orders_checkbox(self):
        return self.get_element(self.locators.AUTO_PRINT_REMOTE_ORDERS_CHECKBOX)

    @property
    def auto_print_other_orders_checkbox(self):
        return self.get_element(self.locators.AUTO_PRINT_OTHER_ORDERS_CHECKBOX)

    @property
    def allow_tips_checkbox(self):
        return self.get_element(self.locators.ALLOW_TIPS_CHECKBOX)

    @property
    def enable_email_receipts_checkbox(self):
        return self.get_element(self.locators.ENABLE_EMAIL_RECEIPTS_CHECKBOX)

    @property
    def cancel_button(self):
        return self.get_element(self.locators.CANCEL_BUTTON)

    @property
    def save_location_button(self):
        return self.get_element(self.locators.SAVE_LOCATION_BUTTON)

    def enter_name(self, name):
        self.name_input.clear()
        self.name_input.send_keys(name)

    def enter_description(self, description):
        self.description_input.clear()
        self.description_input.send_keys(description)

    def select_location_type(self, type):
        self.type_select.select_by_visible_text(type)

    def select_location_group(self, group):
        self.location_group_select.select_by_visible_text(group)

    def clear_location_group(self):
        self.location_group_select.clear()

    def select_default_transfer_source(self, source):
        self.default_transfer_source_select.select_by_visible_text(source)

    def clear_default_transfer_source(self):
        self.default_transfer_source_select.clear()

    def add_location_tag(self, tag):
        self.location_tags_input.send_keys(tag)
        # self.location_tags_input.send_keys(Keys.ENTER)

    def clear_location_tags(self):
        for elem in self.location_tags_input.find_elements_by_css_selector('a.select2-search-choice-close'):
            elem.click()
        i = 0
        while self.location_tags_input.text != '':
            self.location_tags_input.send_keys(Keys.BACK_SPACE)
            i += 1
            if i > 100:
                break

    def remove_location_tag(self, tag):
        elems = self.location_tags_input.find_elements_by_xpath('..').find_elements_by_css_selector('li.select2-search-choice')
        try:
            elem = filter(lambda e: e.text == tag, elems)[0]
        except IndexError:
            return
        elem.find_element_by_tag_name('a').click()

    def set_status_closed(self):
        if self.is_open:
            self.closed_radio_button.click()

    def set_status_open(self):
        if self.is_closed:
            self.open_radio_button.click()

    @property
    def is_closed(self):
        return self.closed_radio_button.is_selected()

    @property
    def is_open(self):
        return self.open_radio_button.is_selected()

    @property
    def has_inseat_delivery(self):
        return self.inseat_delivery_checkbox.is_selected()

    def check_inseat_delivery(self):
        if not self.has_inseat_delivery:
            self.inseat_delivery_checkbox.click()

    def uncheck_inseat_delivery(self):
        if self.has_inseat_delivery:
            self.inseat_delivery_checkbox.click()

    @property
    def has_pickup(self):
        return self.has_pickup_checkbox.is_selected()

    def check_has_pickup(self):
        if not self.has_pickup:
            self.has_pickup_checkbox.click()

    def uncheck_has_pickup(self):
        if self.has_pickup:
            self.has_pickup_checkbox.click()

    @property
    def is_merchandise(self):
        return self.merchandise_checkbox.is_selected()

    def check_merchandise(self):
        if not self.is_merchandise:
            self.merchandise_checkbox.click()

    def uncheck_merchandise(self):
        if self.is_merchandise:
            self.merchandise_checkbox.click()

    def _get_payment_checkbox_by_name(self, payment_type):
        try:
            return filter(lambda e: e.find_element_by_xpath('../../..').text == payment_type, self.payment_type_checkboxes)[0]
        except IndexError:
            return None

    def payment_type_is_enabled(self, payment_type):
        elem = self._get_payment_checkbox_by_name(payment_type)
        return elem.is_selected()

    def check_payment_type(self, payment_type):
        if not self.payment_type_is_enabled(payment_type):
            self._get_payment_checkbox_by_name(payment_type).click()

    def uncheck_payment_type(self, payment_type):
        if self.payment_type_is_enabled(payment_type):
            self._get_payment_checkbox_by_name(payment_type).click()

    def cancel(self):
        self.cancel_button.click()

    def save_location(self):
        self.save_location_button.click()


class EditLocationPage(NewLocationPage):
    PATH = 'locations/{0}/edit'

    def __init__(self, driver, **kwargs):
        self.driver = driver
        location_id = kwargs.get('location_id') # If location_id is supplied, browser with navigate to the url
        if location_id:
            self.PATH = self.PATH.format(location_id)
            baseurl = '{0}://{1}'.format(*urlparse(self.url)[:2])
            url = urljoin(baseurl, self.PATH)
            self.driver.get(url)
