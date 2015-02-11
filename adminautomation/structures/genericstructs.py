from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.select import Select


class DropDownSelector(object):

    def __init__(self, element):
        self.element = element
        #self.TEXT =
