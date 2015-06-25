# The base test class to be inherited by all other test classes

from __future__ import unicode_literals
import unittest
import os
from functools import wraps
import datetime

import tinydb
from tinydb import TinyDB, where
from tinydb.operations import delete, increment, decrement

from adminautomation.utils import TestCaseDataReader
from bypassqatesting.drivers import get_chrome_driver


class BaseTest(unittest.TestCase):
    # Ideally this would be an Abstract Base Class but it works fine as is for now

    DATA_FILE = None
    TEST_DATA = None
    AUTH_COOKIE = None

    @property
    def CURRENT_TEST_DATA(self):
        return self.TEST_DATA[self._testMethodName]

    @classmethod
    def setUpClass(cls):
        cls.db = TinyDB('tests/db.json')
        cls.TEST_DATA = TestCaseDataReader(cls.DATA_FILE) if cls.DATA_FILE else None
        cls.AUTH_COOKIE = cls.db.get(where('admin_session_cookie'))['admin_session_cookie']

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.driver = get_chrome_driver()
        if os.environ.get('DISPLAY') == ':99':
            self.driver.set_window_size(1500, 900) # Selenium server run in an Xvfb session
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @staticmethod
    def screenshot_on_error(test):
        @wraps(test)
        def wrapper(*args, **kwargs):
            try:
                test(*args, **kwargs)
            except:
                test_obj = args[0]
                screenshot_dir = './screenshots'
                if not os.path.exists(screenshot_dir):
                    os.mkdir(screenshot_dir)
                date_string = datetime.datetime.now().strftime('%m%d%y-%H%M%S')
                test_name = test_obj.__name__
                fname = '{screendir}/{testname}-{timestamp}.png'.format(screendir=os.path.abspath(screenshot_dir),
                                                                        testname=test_name,
                                                                        timestamp=date_string)
                test_obj.driver.get_screenshot_as_file(fname)
        return wrapper
    
    @classmethod
    def get_test_data(cls, key):
        try:
            return cls.db.get(where(key))[key]
        except TypeError:
            return None


class BaseLoginTest(BaseTest):
    # Forget why this was needed...
    pass
