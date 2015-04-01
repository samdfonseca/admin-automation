import os
import unittest
from random import randrange
from adminautomation.pages import LoginPage, ChooseVenuePage
from adminautomation.pages import DashboardPage
from adminautomation.utils.drivers import get_chrome_driver


class TestRandomPageNavigationTest(unittest.TestCase):

    navigation_methods = map(lambda call: getattr(DashboardPage, call),
                             filter(lambda attr: attr.startswith('navigate_to'),
                                    filter(lambda attr: callable(getattr(DashboardPage, attr)), dir(DashboardPage))))

    def setUp(self):
        self.driver = get_chrome_driver()
        user = os.environ['ADMIN_USER']
        password = os.environ['ADMIN_PASSWORD']
        page = LoginPage(self.driver)
        page.login(user, password)
        page = ChooseVenuePage(self.driver)
        page.select_venue_from_list_by_name('Bypass WORLD Headquarters')

        self.page = DashboardPage(self.driver)

    def test_random_page_navigation(self):
        navigation_methods = self.navigation_methods
        while True:
            if not navigation_methods:
                break
            jump = navigation_methods.pop(randrange(len(navigation_methods)))
            jump(self.page)
