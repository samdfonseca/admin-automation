from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import css


class NavBarLocators(BaseLocatorGroup):
    LOGO_HOME_BUTTON = css('a.navbar-brand[href="/"]')

    VENUES_SELECT = css('form#update_venue')
    VENUES_LISTBOX = css('div#s2id_change_venue')
    VENUE_LIST_DROPDOWN = css('div#select2-drop')
    VENUE_LIST_SEARCHBOX = css('input.select2-input')
    VENUE_LIST = css('ul.select2-results')
    VENUE_LIST_ITEMS = css('li.select2-result')
    CURRENT_VENUE_OPTION = css('select#change_venue option[selected="selected"]')

    PUSH_UPDATES_NOTIFICATION = css('li#push-menus span.notification')
    PUSH_UPDATES_BUTTON = css('a[href="/menu_push"]')

    LOGOUT_BUTTON = css('a[href="/admin_sessions"]')
