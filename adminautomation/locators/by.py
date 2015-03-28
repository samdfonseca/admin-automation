# http://selenium-python.readthedocs.org/locating-elements.html
from functools import partial
from selenium.webdriver.common.by import By


class BaseLocator(tuple):
    def __new__(cls, by, value):
        return tuple.__new__(cls, (by, value))

    def __add__(self, value):
        return BaseLocator(self[0], ''.join([self[1],value]))


css = partial(BaseLocator, By.CSS_SELECTOR)
xpath = partial(BaseLocator, By.XPATH)
elem_id = partial(BaseLocator, By.ID)
link_text = partial(BaseLocator, By.LINK_TEXT)
partial_link_text = partial(BaseLocator, By.PARTIAL_LINK_TEXT)
name = partial(BaseLocator, By.NAME)
tag = partial(BaseLocator, By.TAG_NAME)
class_name = partial(BaseLocator, By.CLASS_NAME)
