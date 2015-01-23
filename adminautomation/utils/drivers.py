from os import getenv
from selenium import webdriver


def get_chrome_driver():
    return webdriver.Remote(command_executor=getenv('SELENIUM_SERVER_URL', 'http://127.0.0.1:4444/wd/hub'),
                            desired_capabilities=webdriver.DesiredCapabilities.CHROME)



def get_phantomjs_driver():
    return webdriver.Remote(command_executor=getenv('SELENIUM_SERVER_URL', 'http://127.0.0.1:4444/wd/hub'),
                            desired_capabilities=webdriver.DesiredCapabilities.PHANTOMJS)
