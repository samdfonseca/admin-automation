from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import css


class ChooseVenueLocators(BaseLocatorGroup):
    VENUES_LISTBOX = css('div#s2id_change_venue')
    VENUE_LIST_SEARCHBOX = css('input.select2-input')
    VENUE_LIST = css('ul.select2-results')
    VENUE_LIST_ITEMS = css('li.select2-result')
    VENUE_OPTIONS = css('select#change_venue option')
    GO_BUTTON = css('button.btn')
    FORM_TITLE = css('h3.form-title')
