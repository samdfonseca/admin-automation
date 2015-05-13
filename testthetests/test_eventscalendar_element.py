import unittest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from adminautomation.pages import EventsCalendarPage


class EventsCalendarTests(unittest.TestCase):
    @classmethod
    def setupClass(cls):
        cls.driver = webdriver.Chrome()
        cls.page = EventsCalendarPage(cls.driver, skip_login=True)

    @classmethod
    def teardownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def setup(self):
        self.page.refresh_page()

    def test_new_event_name_is_webelement(self):
        self.assertIsInstance(self.page.AddNewEventForm.NAME, WebElement)

    def test_new_event_name_send_keys(self):
        elem = self.page.AddNewEventForm.NAME
        elem.send_keys('test')
        self.assertEqual(self.page.AddNewEventForm.NAME.get_attribute('value'), 'test')
