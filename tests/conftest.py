import pytest
import os
import ConfigParser
import simplejson as json
from tinydb import TinyDB, where
from bypassqatesting.drivers import get_chrome_driver
from bypassqatesting.logger import get_module_logger


mlog = get_module_logger()

@pytest.fixture(scope='session')
def testdata(request):
    class TestData(dict):
        def __init__(self, item):
            super(TestData, self).__init__(**item)
        def update_db(self, item):
            self.update(item)
            db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.json')
            with open(db_file, 'w') as f:
                json.dump(self, f)
    db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.json')
    cached_db_file = '_'+os.path.basename(db_file)
    with open(db_file, 'r') as f:
        mlog.debug('Opening database: {}'.format(db_file))
        db = TestData(json.load(f))
        with open(cached_db_file, 'w') as ff:
            mlog.debug('Caching original database: {}'.format(cached_db_file))
            json.dump(db, ff)
    def fin():
        mlog.debug('Closing database: {}'.format(db_file))
        with open(cached_db_file, 'r') as ff:
            mlog.debug('Reverting to cached database: {}'.format(cached_db_file))
            with open(db_file, 'w') as f:
                json.dump(json.load(ff), f)
        os.remove(cached_db_file)
    request.addfinalizer(fin)
    return db

@pytest.fixture(scope='session', autouse=True)
def update_testdata(testdata):
    def updater(newvals):
        testdata.update(newvals)
        db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.json')
        with open(db_file, 'w') as f:
            json.dump(testdata, f)
    return updater

@pytest.fixture
def driver(request):
    mlog.debug('Starting new driver')
    driver = get_chrome_driver()
    def fin():
        mlog.debug('Closing driver...')
        driver.close()
    request.addfinalizer(fin)
    return driver

@pytest.fixture
def authenticated_driver(request, testdata):
    mlog.debug('Starting new authenticated driver...')
    url = testdata.get('baseurl') + '404.html'
    cookie = testdata.get('admin_session_cookie')
    driver = get_chrome_driver()
    driver.get(url)
    driver.add_cookie(cookie)
    def fin():
        mlog.debug('Closing driver...')
        driver.close()
    request.addfinalizer(fin)
    return driver

def pytest_addoption(parser):
    config = ConfigParser.ConfigParser(defaults={'baseurl': ''})
    config.read('setup.cfg')

    group = parser.getgroup('selenium', 'selenium')
    group._addoption('--baseurl',
                     action='store',
                     dest='base_url',
                     default=config.get('DEFAULT', 'baseurl'),
                     metavar='url',
                     help='base url for the application under test.')
