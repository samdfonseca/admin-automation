from os import getenv
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_chrome_driver():
    return webdriver.Remote(command_executor=getenv('SELENIUM_SERVER_URL'),
                            desired_capabilities=DesiredCapabilities.CHROME)


def get_phantomjs_driver():
    return webdriver.Remote(command_executor=getenv('SELENIUM_SERVER_URL'),
                            desired_capabilities=DesiredCapabilities.PHANTOMJS)
