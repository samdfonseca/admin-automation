# class DataTableRow(object):
#     def __init__(self, row, headers, locators):
#         self.row = row
#         self.headers = headers
#         self.locators = locators
#
#     def __setattr__(self, key, value):
#         if isinstance(value, BaseLocator):
#             object.__setattr__(self, key, object.__getattribute__('row').find_element(*value))
#         else:
#             object.__setattr__(self, key, value)
#
# class DropDownSelector(object):
#
#     def __init__(self, element):
#         self.element = element
#         #self.TEXT =


class PaginationButtons(object):
    def __init__(self, button_group_element, buttons_locator=('css selector', 'li a')):
        """A generic set of pagination buttons, usually seen at the bottom of a datatable.
        :param button_group_element: The WebElement representing the pagination buttons. Should be the ul element
        containing the individual buttons.
        :param buttons_locator: The selector used to search for the individual buttons. Formated as a 2-item tuple
        containing a selector type, from the By class, and match value.
        """
        self.button_group_element = button_group_element
        self.buttons_locator = buttons_locator

    @property
    def BUTTONS(self):
        return self.button_group_element.find_elements(*self.buttons_locator)

    def get_first_page_button(self, first_page_button_locator=('css selector', 'a[ng-switch-when="first"]')):
        return self.button_group_element.find_element(*first_page_button_locator)

    def get_last_page_button(self, last_page_button_locator=('css selector', 'a[ng-switch-when="last"]')):
        return self.button_group_element.find_element(*last_page_button_locator)

    def get_next_page_button(self, next_page_button_locator=('css selector', 'a[ng-switch-when="next"]')):
        return self.button_group_element.find_element(*next_page_button_locator)

    def get_previous_page_button(self, previous_page_button_locator=('css selector', 'a[ng-switch-when="prev"]')):
        return self.button_group_element.find_element(*previous_page_button_locator)

    def get_button_by_text(self, button_text):
        return filter(lambda button: button.text == str(button_text), self.BUTTONS)[0]

