import pytest
from tinydb import TinyDB, where
from bypassqatesting.drivers import get_chrome_driver

@pytest.fixture(scope='session')
def testdata():
    return TinyDB('tests/db.json')

@pytest.fixture(scope='session')
def driver():
    return get_chrome_driver()

@pytest.fixture(scope='session')
def authenticated_driver(testdata):
    url = testdata.get(where('baseurl'))['baseurl'] + '404.html'
    cookie = testdata.get(where('admin_session_cookie'))['admin_session_cookie']
    driver = get_chrome_driver()
    driver.get(url)
    driver.add_cookie(cookie)
    return driver
