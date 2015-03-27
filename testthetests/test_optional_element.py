import unittest
from adminautomation.pages import InventoryStatusPage
from adminautomation.locators.by import BaseLocator
from selenium import webdriver

class TestInventoryStatusPage(unittest.TestCase):
    def test_not_unused_element(self):
        self.assertIsInstance(self.page.locators.ITEMS_PER_PAGE_SELECTOR, BaseLocator)

    def setUp(self):
        driver = webdriver.PhantomJS()
        self.page = InventoryStatusPage(driver)

    def tearDown(self):
        self.page.driver.quit()
