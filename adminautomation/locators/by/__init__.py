# http://selenium-python.readthedocs.org/locating-elements.html
from functools import partial
from selenium.webdriver.common.by import By


class LocatorTypeException(Exception):
    message = 'Unable to join locators of different types.'


class UnrecognizedLocatorValueException(Exception):
    message = 'Unable to handle locator values of the given type.'


class BaseLocator(tuple):
    def __new__(cls, by, value):
        return tuple.__new__(cls, (by, value))

    def __add__(self, value):
        if isinstance(value, BaseLocator):
            # Adding a BaseLocator to a BaseLocator
            if value[0] == self[0]:
                # BaseLocators both are of the same type, i.e. css + css
                return BaseLocator(self[0], ' '.join([self[1], value[1]]))
            else:
                # BaseLocators are of different types, i.e. css + xpath
                raise LocatorTypeException
        elif isinstance(value, basestring):
            return BaseLocator(self[0], ' '.join([self[1],value]))
        else:
            raise UnrecognizedLocatorValueException

    def __str__(self):
        return self[1]

    def format(self, *args):
        return BaseLocator(self[0], self[1].format(*args))


css = partial(BaseLocator, By.CSS_SELECTOR)
xpath = partial(BaseLocator, By.XPATH)
elem_id = partial(BaseLocator, By.ID)
link_text = partial(BaseLocator, By.LINK_TEXT)
partial_link_text = partial(BaseLocator, By.PARTIAL_LINK_TEXT)
name = partial(BaseLocator, By.NAME)
tag = partial(BaseLocator, By.TAG_NAME)
class_name = partial(BaseLocator, By.CLASS_NAME)
