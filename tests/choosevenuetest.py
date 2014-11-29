#!/usr/bin/env python

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from basetest import BaseTest
from adminautomation.pages import LoginPage, ChooseVenuePage


class ChooseVenueTest(BaseTest):
    def test_select_venue_by_name(self):
        with open("login.auth", "r") as f:
            user, passwd = f.readlines()
        login_page = LoginPage(self.driver)
        login_page.login(user.strip(), passwd.strip())
        choose_venue_page = ChooseVenuePage(self.driver)
        choose_venue_page.click_venues_listbox()
        choose_venue_page.select_venue_from_list_by_name("QA Kingdom")
        choose_venue_page.click_go_button()
        el = self.driver.find_element_by_class_name("select2-chosen")
        assert el.text == "QA Kingdom"


if __name__ == "__main__":
    unittest.main()