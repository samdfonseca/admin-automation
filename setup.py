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
        'git+ssh://git@github.com/bypasslane/testrailwrapper.git@0.1.20150127#egg=testrailwrapper-0.1.20150127'
    ],
    description='Bypass Admin Automated Testing'
)
