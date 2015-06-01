import random
import string

from hamcrest import *
import nose.tools
from nose_parameterized import parameterized

from basetest import BaseTest
from adminautomation.pages import EventsCalendarPage
from bypassqatesting.datetime import now

class TestEventsCalendarPage(BaseTest):

    # def create_new_event(self, event_length):
    #     """C1705 - Create New Event"""
    #     page = EventsCalendarPage(self.driver, skip_login=True)
    #     event_name = 'event_{}'.format(''.join(random.choice(string.ascii_letters + string.digits) for x in range(20)))
    #     start_time = datetime.datetime.now()
    #     page.add_new_event_form.create_event(event_name,
    #                                          start_time,
    #                                          start_time + event_length)
    #
    # def tests_events_calendar_create_new_event(self):
    #     event_lengths = [
    #         datetime.timedelta(minutes=5),
    #         datetime.timedelta(hours=6),
    #         datetime.timedelta(weeks=1)
    #     ]
    #     for event_length in event_lengths:
    #         yield self.create_new_event, self, event_length

    def test_enter_well_formated_date_into_start_date(self):
        page = EventsCalendarPage(self.driver, skip_login=True)
        start_time = now()
        page.add_new_event_form.enter_start_date(start_time)
        page.PAGE_TITLE.click()
        assert_that(page.add_new_event_form.START_DATE.get_attribute('value'),
                    is_(start_time.strftime(page.add_new_event_form.DEFAULT_DATE_FORMAT)))

    def test_enter_well_formated_date_into_end_date(self):
        page = EventsCalendarPage(self.driver, skip_login=True)
        end_time = now()
        page.add_new_event_form.enter_end_date(end_time)
        page.PAGE_TITLE.click()
        assert_that(page.add_new_event_form.END_DATE.get_attribute('value'),
                    is_(end_time.strftime(page.add_new_event_form.DEFAULT_DATE_FORMAT)))

