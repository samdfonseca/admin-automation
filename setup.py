try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


__version__ = '0.1.20150127'


with open('requirements.txt') as f:
    depends = map(str.strip, f.readlines())

setup(
    name='adminautomation',
    version=__version__,
    packages=['adminautomation'],
    url='https://github.com/bypasslane/admin-web-automation',
    install_requires=depends,
    dependency_links=[
        'git+ssh://git@github.com/bypasslane/testrailwrapper.git@0.1.20150127#egg=testrailwrapper-0.1.20150127',
        'git+ssh://git@github.com/bypasslane/bypass-qatesting-common.git@0.0.1#egg=bypassqatesting-0.0.2',
        'git+ssh://git@github.com/samdfonseca/sneeze.git#egg=nose-sneeze-0.0.3',
        'git+ssh://git@github.com/samdfonseca/pocket.git#egg=sneeze-pocket-0.0.1',
        'git+ssh://git@github.com/samdfonseca/pocket_change.git#egg=pocket-change-0.0.6',
        'git+ssh://git@github.com/samdfonseca/boltons#egg=boltons-0.6.5dev',
    ],
    description='Bypass Admin Automated Testing'
)

import os
selenium_server_version = '2.45.0'
bin_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'bin')
selenium_jar_file = os.path.join(bin_dir, 'selenium-server-standalone-{0}.jar'.format(selenium_server_version))
selenium_symlink_file = os.path.join(os.path.dirname(selenium_jar_file), 'selenium-server.jar')
selenium_version_file = os.path.join(bin_dir, '.selenium-version')


def download_selenium_server(version):
    import pycurl
    download_url = 'http://selenium-release.storage.googleapis.com/{0}/' \
                   'selenium-server-standalone-{0}.0.jar'.format(version[:-2])

    if not os.path.exists(bin_dir):
        os.mkdir(bin_dir)

    with open(selenium_jar_file, 'wb') as f:
        c = pycurl.Curl()
        c.setopt(c.URL, download_url)
        c.setopt(c.WRITEDATA, f)
        print('Downloading selenium server from {0}'.format(download_url))
        c.perform()
        print('Download finished')
        c.close()
        os.link(selenium_jar_file, selenium_symlink_file)

    with open(selenium_version_file, 'w') as f:
        f.write(version)


print(bin_dir)
print(selenium_jar_file)
print(selenium_symlink_file)
print(selenium_version_file)
try:
    if not os.path.exists(selenium_jar_file):
        download_selenium_server(selenium_server_version)
    elif open(selenium_version_file).read().strip() != selenium_server_version:
        download_selenium_server(selenium_server_version)
except IOError:
    download_selenium_server(selenium_server_version)

os.popen('brew install phantomjs')
os.popen('brew install chromedriver')
