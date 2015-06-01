import random
import string

from hamcrest import *
import nose.tools
from nose_parameterized import parameterized

from basetest import BaseTest
from adminautomation.pages import EventsCalendarPage
from bypassqatesting import datetimeutil
from bypassqatesting.api import events

class TestEventsCalendarPage(BaseTest):

    def test_enter_well_formated_date_into_start_date(self):
        page = EventsCalendarPage(self.driver, skip_login=True)
        start_time = datetimeutil.now()
        page.add_new_event_form.enter_start_date(start_time)
        page.PAGE_TITLE.click()
        assert_that(page.add_new_event_form.START_DATE.get_attribute('value'),
                    is_(start_time.strftime(page.add_new_event_form.DEFAULT_DATE_FORMAT)))

    def test_enter_well_formated_date_into_end_date(self):
        page = EventsCalendarPage(self.driver, skip_login=True)
        end_time = datetimeutil.now()
        page.add_new_event_form.enter_end_date(end_time)
        page.PAGE_TITLE.click()
        assert_that(page.add_new_event_form.END_DATE.get_attribute('value'),
                    is_(end_time.strftime(page.add_new_event_form.DEFAULT_DATE_FORMAT)))

    def test_create_new_event(self):
        page = EventsCalendarPage(self.driver, skip_login=True)
        page.choose_venue_from_list('QA Kingdom')
        page.navigate_to_events_calendar()
        start_time = datetimeutil.now()
        end_time = start_time + datetimeutil.timedelta(minutes=5)
        event_name = 'event_{}'.format(''.join(random.choice(string.ascii_letters + string.digits) for x in range(20)))
        page.add_new_event_form.create_event(event_name, start_time, end_time)
        all_events = events.get_all_events(venue_id='187')
        assert_that(all_events[-1]['name'], is_(event_name))
