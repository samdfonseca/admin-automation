from adminautomation.pages import LoginPage, ChooseVenuePage
from selenium import webdriver


def get_admin_session_cookie(user, passwd, **kwargs):
    # Logs into admin as the given user and returns the authenticated session cookie which can be used
    # to circumvent logging in every time. If venue_name is provided, the session uses that Venue.

    venue_name = kwargs.get('venue_name', 'Bypass World Headquarters')
    auth_url = kwargs.get('auth_url', 'https://admin-integration.bypasslane.com')

    driver = webdriver.PhantomJS()
    login_page = LoginPage(driver, auth_url)
    login_page.login(user, passwd)

    choose_venue_page = ChooseVenuePage(driver)
    choose_venue_page.click_venues_listbox()
    choose_venue_page.select_venue_from_list_by_name(venue_name)
    choose_venue_page.click_go_button()

    cookie = driver.get_cookie('_bypass_admin_session')

    return cookie
