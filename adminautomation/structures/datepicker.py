from datetime import datetime
from selenium.webdriver.remote.webelement import WebElement
from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import *


class DateTimePickerLocators(BaseLocatorGroup):
    MAIN_DIV = css('div.datetimepicker')

    YEARS_TABLE = MAIN_DIV + css('div.datetimepicker-years table')
    MONTHS_TABLE = MAIN_DIV + css('div.datetimepicker-months table')
    DAYS_TABLE = MAIN_DIV + css('div.datetimepicker-days table')
    HOURS_TABLE = MAIN_DIV + css('div.datetimepicker-hours table')
    MINUTES_TABLE = MAIN_DIV + css('div.datetimepicker-minutes table')
    CURRENT_TABLE = MAIN_DIV + css('div[style="display: block;"] table')

    PREVIOUS = CURRENT_TABLE + css('th.prev')
    SWITCH = CURRENT_TABLE + css('th.switch')
    NEXT = CURRENT_TABLE + css('th.next')
    TODAY = CURRENT_TABLE + css('th.today')

    NEXT = CURRENT_TABLE + css('th.next')
    TODAY = CURRENT_TABLE + css('th.today')


class DateTimeField(WebElement):
    def __init__(self, *args, **kwargs):
        super(DateTimeField, self).__init__(*args, **kwargs)

    @classmethod
    def _format_datetime(self, dt, fmt='%B %d, %Y %I:%M %p'):
        return dt.strftime(fmt)

    def enter_datetime_directly(self, dt):
        dt_fmt = self._format_datetime(dt)
        self.send_keys(dt_fmt)


# class DateTimePicker(object):
#
#     locators = DateTimePickerLocators
#
#     def __init__(self, datetime_entry=None):
#
#     @staticmethod
#     def _format_datetime(, format_str='%B %d, %Y %I:%M %p'):
#         """May 04, 2015 12:15 PM"""
#         datetime.strftime(
#
