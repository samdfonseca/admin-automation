# Functions for getting a pre-authenticated session cookie for new Admin

from adminautomation.pages import LoginPage, ChooseVenuePage

from os.path import getmtime
import pickle
from selenium import webdriver
from time import time

def get_admin_session_cookie(user, passwd, **kwargs):
    # Logs into admin as the given user and returns the authenticated session cookie which can be used
    # to circumvent logging in every time. If venue_name is provided, the session uses that Venue.

    THREE_DAYS_IN_SECONDS = 60 * 60 * 24 * 3

    auth_cookie_file = kwargs.get("cookie_file", "auth_cookie.pickle")
    max_cache_time = kwargs.get("max_cache_time", THREE_DAYS_IN_SECONDS)
    force_new_session = kwargs.get("force_new_session", False)
    auth_url = kwargs.get('auth_url', 'https://admin-integration.bypasslane.com/admin_sessions/new')
    session_cookie_name = kwargs.get("session_cookie_name", "_bypass_admin_session")
    cache_session_cookie = kwargs.get("cache_cookie", True)
    use_headless_browser = kwargs.get("headless", True)

    if user is None or passwd is None:
        raise Warning("user and passwd arguments should not be None in case the cached cookie is expired.")

    if force_new_session is not True:
        # If param force_new is not set to True, try to use a cached session cookie
        try:
            stored_cookie_mod_time = getmtime(auth_cookie_file)
        except OSError:
            stored_cookie_mod_time = None
        else:
            # Use the cache session cookie if it was modified (updated) within the last 3 days
            # Theses prolly a better way of doing this but it seems to work for now
            if time() - stored_cookie_mod_time < max_cache_time:
                with open(auth_cookie_file, "r") as f:
                    cookie = pickle.load(f)

                return cookie

    if user is None or passwd is None:
        raise TypeError("'user' and 'passwd' cannot be None")

    # If not using the cached session cookie, login to a new Admin session and extract its session cookie
    if use_headless_browser:
        # Use PhantomJS if headless param is set to True (Default)
        driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'], service_log_path="logs/ghostdriver.log")
    else:
        driver = webdriver.Chrome()

    admin = LoginPage(driver, url=auth_url)
    admin.login(user, passwd)

    # admin = ChooseVenuePage(admin.driver)
    # admin.select_venue_from_list_by_row_number(0)
    # admin.select_venue_from_list_by_name(venue_name)
    # admin.click_go_button()

    cookie = admin.driver.get_cookie(session_cookie_name)

    admin.driver.quit()

    # Pickle the session cookie and save it to a file if cache_session_cookie is set to True
    if cache_session_cookie:
        with open(auth_cookie_file, "w") as f:
            pickle.dump(cookie, f)

    return cookie


def attach_auth_session_to_driver(driver, session_cookie=None, **kwargs):
    """
    Replaces the current Admin session cookie on the given driver with a pre-authenticated cookie.
    If the param session_cookie is set to a valid cookie object, session_cookie is used without checking if
    it is authenticated. Otherwise, if session_cookie is set to None, kwargs are passed to get_admin_session_cookie,
    and a new session cookie is generated and used.

    :param driver: a webdriver object to attach the session to
    :param cookie: an optional cookie object which can be attached directly
    """

    if isinstance(session_cookie, dict):
        driver.delete_cookie(session_cookie["name"])
        driver.add_cookie(session_cookie)
    else:
        if kwargs.get("user") is None:
            raise TypeError("'user' is not set")
        if kwargs.get("passwd") is None:
            raise TypeError("'passwd' is not set")

        session_cookie = get_admin_session_cookie(kwargs.get("user"), kwargs.get("passwd"))
        if isinstance(session_cookie, dict):
            attach_auth_session_to_driver(driver, session_cookie=session_cookie)
        else:
            raise Exception("Unable to get session cookie")

    # preauthed_cookie = None
    # if isinstance(session_cookie, dict):
    #     # Cookie objects are dicts with certain keys-values.
    #     try:
    #         if session_cookie["domain"].lower() in driver.current_url.lower():
    #             # Assume session cookie is valid if it has the key 'domain' and its value is a substring of the
    #             # driver's current url
    #             preauthed_cookie = session_cookie
    #     except KeyError:
    #         preauthed_cookie = None
    #
    # if preauthed_cookie is None:
    #     # If session_cookie is not given or not usable, pass kwargs to get_admin_session_cookie.
    #     user = kwargs.pop("user")
    #     passwd = kwargs.pop("passwd")
    #
    #     preauthed_cookie = get_admin_session_cookie(user, passwd, **kwargs)
    #
    # # Delete the old cookie and add the new one
    # driver.delete_cookie(preauthed_cookie["name"])
    # driver.add_cookie(preauthed_cookie)


