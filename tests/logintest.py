#!/usr/bin/env python

import sys
sys.path.append("..")

import unittest
from selenium import webdriver
from adminautomation.pages import LoginPage


class BypassIntegrationLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_user_with_valid_credentials(self):
        with open("login.auth", "r") as f:
            user, passwd = f.readlines()
        login_page = LoginPage(self.driver)
        login_page.login(user.strip(), passwd.strip())
        assert login_page.driver.current_url == "https://admin-integration.bypasslane.com/admin_sessions/choose_venue"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()