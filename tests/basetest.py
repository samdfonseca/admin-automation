import unittest

from selenium import webdriver

from adminautomation.utils.testcasedata import new_test_case_data_object as TestCaseData
from adminautomation.utils.testcasedata import read_test_case_data_file as TestCaseDataReader

class BaseTest(unittest.TestCase):

    TEST_DATA = None

    def setUp(self):
        BaseTest.TEST_DATA = TestCaseDataReader(self.DATA_FILE)
        self.driver = webdriver.Chrome()


    def tearDown(self):
        self.driver.close()


    @property
    def CURRENT_TEST_DATA(self):
        # Returns the data for the current test case in a dict.
        # Pops the first row of data in TEST_DATA['test_cases'], so the current test data will always
        # be located at TEST_DATA['test_cases'][0].

        current_test_case = BaseTest.TEST_DATA.pop(0)
        return TestCaseData(current_test_case)