from __future__ import print_function

from adminautomation.pages import BasePage
from adminautomation.utils import ChooseVenueLocators
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys


class ChooseVenuePage(BasePage):

    URL = "https://admin-integration.bypasslane.com/admin_sessions/choose_venue"

    # Expected values to check against
    CHECK_VALUES = {
        "page_title": "Admin Sessions - Choose Venue",
        "form_title": "Please Select a Venue"
    }


    def __init__(self, driver, **kwargs):
        super(ChooseVenuePage, self).__init__(driver)

        self.URL = kwargs.get("url", self.URL)

        self.driver.get(self.URL)


    @property
    def VENUES_LISTBOX(self):
        return self.get_element(ChooseVenueLocators.VENUES_LISTBOX)


    @property
    def VENUE_OPTIONS(self):
        return self.get_elements(ChooseVenueLocators.VENUE_OPTIONS)


    @property
    def GO_BUTTON(self):
        return self.get_element(ChooseVenueLocators.GO_BUTTON)


    @property
    def FORM_TITLE(self):
        return self.get_element(ChooseVenueLocators.FORM_TITLE)


    @property
    def VENUE_LIST(self):
        return self.get_element(ChooseVenueLocators.VENUE_LIST, "Cannot locate VENUE_LIST")


    @property
    def VENUE_LIST_ITEMS(self):
        return self.get_elements(ChooseVenueLocators.VENUE_LIST_ITEMS, "Cannot locate VENUE_LIST_ITEMS")


    @property
    def VENUE_LIST_SEARCHBOX(self):
        return self.get_element(ChooseVenueLocators.VENUE_LIST_SEARCHBOX, "Cannot locate VENUE_LIST_SEARCHBOX")


    def is_form_title_match(self, custom_message=None):
        """
        Checks that the choose venue form title matches the expected value.

        :param custom_message: a custom message to throw if the assertion fails
        """

        found_form_title = self.FORM_TITLE.text
        self.check_value("form_title", found_form_title, custom_message=custom_message)


    def is_dropdown_visible(self):
        """
        Checks if the venues list is dropped down or not.

        :return: a boolean, True if visible, False if not
        """

        if self.VENUE_LIST_SEARCHBOX is not None and self.VENUE_LIST is not None:
            if self.VENUE_LIST_SEARCHBOX.is_displayed() and self.VENUE_LIST.is_displayed():
                return True

        return False

    def expand_venues_listbox(self):
        """
        Simulates clicking the venues listbox. If already expanded, does nothing.
        """

        if self.is_dropdown_visible() is False:
            # If the dropdown is not visible/expanded, click it
            self.VENUES_LISTBOX.click()


    def contract_venues_listbox(self):
        """
        Simulates pressing escape in the venues list searchbox. If already contracted, does nothing.
        """

        if self.is_dropdown_visible():
            # If the dropdown is visible/expanded, press escape in the searchbox.
            self.VENUE_LIST_SEARCHBOX.send_keys(Keys.ESCAPE)


    def toggle_venues_listbox(self):
        """
        Toggles the venues listbox between expanded and contracted.
        """

        if self.is_dropdown_visible():
            # If the dropdown is visible/expanded, contract it.
            self.contract_venues_listbox()
        else:
            # If the dropdown is not visible/expanded, expand it.
            self.expand_venues_listbox()


    def click_go_button(self):
        """
        Simulates clicking the go button.
        """

        self.GO_BUTTON.click()


    def clear_searchbox(self):
        """
        Deletes all characters from the searchbox.
        """

        while len(self.VENUE_LIST_SEARCHBOX.get_attribute("value")) > 0:
            self.VENUE_LIST_SEARCHBOX.send_keys(Keys.BACKSPACE)


    def get_current_list_items(self):
        """
        Gets the items currently displayed by the dropdown menu. If drowndown menu is not visible,
        function return an empty list.

        :return: a list of WebElement objects
        """

        if self.is_dropdown_visible():
            return self.get_elements(ChooseVenueLocators.VENUE_LIST_ITEMS)

        return []


    def search_for_venue(self, search_query):
        """
        Simulates clicking the venues searchbox.
        """

        self.expand_venues_listbox()

        self.clear_searchbox()
        if isinstance(search_query, basestring):
            self.VENUE_LIST_SEARCHBOX.send_keys(search_query)


    def select_venue_from_list_by_name(self, venue_name):
        """
        Selects the list item that matches venue_name.

        :param venue_name: the venue's name as a string
        """

        self.expand_venues_listbox()
        list_items = self.get_current_list_items()
        for item in list_items:
            if item.text == venue_name:
                break
            self.VENUE_LIST_SEARCHBOX.send_keys(Keys.ARROW_DOWN)
        else:
            print("Could not find venue in list: {}".format(venue_name))
            return

        item.click()


    def select_venue_from_list_by_row_number(self, row):
        """
        Selects the list item based on row number.

        :param row: the row number as an integer
        """

        if self.is_dropdown_visible() is False:
            print("Dropdown list is not visible. Unable to select a venue.")
            return

        list_items = self.get_current_list_items()
        if row in range(len(list_items)):
            list_items[row].click()


    def select_venue_by_venue_id(self, venue_id):
        """
        Selects the venue based on its venue_id attribute.

        :param venue_id: the venue's id number as an integer
        """

        for item in self.VENUE_OPTIONS:
            if item.get_attribute("value") == venue_id: break
        else:
            print("Could not find venue id in list: {}".format(venue_id))
            return

        item.click()

