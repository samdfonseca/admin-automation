import pytest
import os
import ConfigParser
import simplejson as json
from boltons.fileutils import atomic_save
from bypassqatesting.adminsession import get_session_cookie
from bypassqatesting.drivers import get_driver
from bypassqatesting.logger import get_module_logger


mlog = get_module_logger()

def cookie_updater(db): db['admin_session_cookie'].update(get_session_cookie(user=db['admin_user'], passwd=db['admin_password'], venue=db['venue']['id'], root_url=db['baseurl']))

data_updaters = [cookie_updater]
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
        for updater in data_updaters:
            mlog.debug('Executing DB updater: {}'.format(updater.func_name))
            updater(db)
        with open(cached_db_file, 'w') as ff:
            mlog.debug('Caching original database: {}'.format(cached_db_file))
            json.dump(db, ff)
    def fin():
        mlog.debug('Closing database: {}'.format(db_file))
        with open(cached_db_file, 'r') as ff:
            mlog.debug('Reverting to cached database: {}'.format(cached_db_file))
            with atomic_save(db_file) as f:
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

@pytest.fixture(scope='module')
def unauthenticated_driver(request, testdata):
    mlog.debug('Starting new driver')
    # browser_type = testdata.get('browser_type')
    # browser_default_window_size = tuple(testdata.get('browser_default_window_size'))
    # selenium_server_url = testdata.get('selenium_server_url')
    # maximize_browser_window = testdata.get('maximize_browser_window')
    # custom_webdriver_desired_capabilities = testdata.get('custom_webdriver_desired_capabilities')
    webdriver_kwargs = testdata.get('webdriver_kwargs', {})
    mlog.debug('Driver kwargs: {}'.format(', '.join(map(lambda i: '='.join([i[0], i[1]]), webdriver_kwargs.items()))))
    driver = get_driver(**webdriver_kwargs)
    def fin():
        mlog.debug('Closing driver...')
        driver.close()
    request.addfinalizer(fin)
    return driver

@pytest.fixture(scope='module')
def driver(request, unauthenticated_driver, testdata):
    mlog.debug('Authenticating driver...')
    url = testdata.get('baseurl') + '404.html'
    user, password, venue, root_url = testdata['admin_user'], testdata['admin_password'], testdata['venue']['id'], testdata['baseurl']
    cookie = get_session_cookie(user=user, passwd=password, venue=venue, root_url=root_url)
    driver = unauthenticated_driver
    driver.get(url)
    driver.delete_all_cookies()
    driver.add_cookie(cookie)
    # def fin():
    #     mlog.debug('Closing driver...')
    #     driver.close()
    # request.addfinalizer(fin)
    mlog.debug('Driver started at url: {}'.format(driver.current_url))
    return driver

# def pytest_runtest_teardown(item):


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
