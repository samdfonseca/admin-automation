from adminautomation.pages import LoginPage, ChooseVenuePage

from os.path import getmtime
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_admin_session_cookie(user, passwd, **kwargs):
    # Logs into admin as the given user and returns the authenticated session cookie which can be used
    # to circumvent logging in every time. If venue_name is provided, the session uses that Venue.

    AUTH_COOKIE_FILE = "auth_cookie.pickle"

    if not kwargs.get("force_new"):
        try:
            stored_cookie_mod_time = getmtime("auth_cookie.pickle")
        except OSError:
            stored_cookie_mod_time = None
        else:
            three_days_in_seconds = 60 * 60 * 24 * 3
            if time.time() - stored_cookie_mod_time < three_days_in_seconds:
                with open(AUTH_COOKIE_FILE, "r") as f:
                    cookie = pickle.load(f)
                    return cookie

    venue_name = kwargs.get('venue_name', 'Bypass World Headquarters')
    auth_url = kwargs.get('auth_url', 'https://admin-integration.bypasslane.com/admin_sessions/new')

    driver = webdriver.Chrome()
    # driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
    login_page = LoginPage(driver, url=auth_url)
    login_page.login(user, passwd)

    choose_venue_page = ChooseVenuePage(driver)
    choose_venue_page.click_venues_listbox()
    choose_venue_page.search_for_venue(venue_name)
    choose_venue_page.VENUE_LIST_SEARCHBOX.send_keys(Keys.RETURN)
    choose_venue_page.click_go_button()

    cookie = driver.get_cookie('_bypass_admin_session')
    with open(AUTH_COOKIE_FILE, "w") as f:
        pickle.dump(cookie, f)


    return cookie
