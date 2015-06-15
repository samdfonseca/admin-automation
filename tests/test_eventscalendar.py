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
    def tearDown(self):
        super(TestEventsCalendarPage, self).tearDown()
    #     current_events = events.filter_current_events(events.get_all_events(venue_id='187'))
    #     for event in current_events:
    #         events.delete_event(venue_id='187', event_id=event['id'])
        if self.event:
            events.delete_event(venue_id='187', event_id=self.event['id'])

    def setUp(self):
        super(TestEventsCalendarPage, self).setUp()
        self.event = None

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
        if page.driver.current_url != page.URL:
            page.go_to_page_url()
        start_time = datetimeutil.now()
        end_time = start_time + datetimeutil.timedelta(minutes=5)
        event_name = 'event_{}'.format(''.join(random.choice(string.ascii_letters + string.digits) for x in range(20)))
        page.add_new_event_form.create_event(event_name, start_time, end_time)
        page.sleep(1)
        self.event = events.get_all_events(venue_id='187')[-1]
        # self.event = events.filter_current_events(events.get_all_events(venue_id='187'))[0]
        assert_that(self.event['name'], is_(event_name))

    def test_create_new_event_with_template(self):
        page = EventsCalendarPage(self.driver, skip_login=True)
        page.choose_venue_from_list('QA Kingdom')
        if page.driver.current_url != page.URL:
            page.go_to_page_url()
        start_time = datetimeutil.now() + datetimeutil.timedelta(days=1)
        end_time = start_time + datetimeutil.timedelta(minutes=5)
        event_name = 'event_{}'.format(''.join(random.choice(string.ascii_letters + string.digits) for x in range(20)))
        event_template_name = 'First Template'
        page.add_new_event_form.create_event(event_name, start_time, end_time, event_template_name)
        page.sleep(1)
        self.event = events.get_all_events(venue_id='187')[-1]
        assert_that(self.event['name'], is_(event_name))
        assert_that(self.event['event_template_name'], is_(event_template_name))

    def test_create_new_event_with_single_tag(self):
        page = EventsCalendarPage(self.driver, skip_login=True)
        page.choose_venue_from_list('QA Kingdom')
        if page.driver.current_url != page.URL:
            page.go_to_page_url()
        start_time = datetimeutil.now() + datetimeutil.timedelta(days=2)
        end_time = start_time + datetimeutil.timedelta(minutes=5)
        event_name = 'event_{}'.format(''.join(random.choice(string.ascii_letters + string.digits) for x in range(20)))
        tags = 'testing'
        page.add_new_event_form.create_event(event_name, start_time, end_time, None, tags)
        page.sleep(1)
        self.event = events.get_all_events(venue_id='187')[-1]
        assert_that(self.event['name'], is_(event_name))
        assert_that(self.event['tag_list'], is_([tags]))

    def test_create_new_event_with_multiple_tags(self):
        page = EventsCalendarPage(self.driver, skip_login=True)
        page.choose_venue_from_list('QA Kingdom')
        if page.driver.current_url != page.URL:
            page.go_to_page_url()
        start_time = datetimeutil.now() + datetimeutil.timedelta(days=3)
        end_time = start_time + datetimeutil.timedelta(minutes=5)
        event_name = 'event_{}'.format(''.join(random.choice(string.ascii_letters + string.digits) for x in range(20)))
        tags = ['tagA', 'tagB', 'tagC']
        page.add_new_event_form.create_event(event_name, start_time, end_time, None, tags)
        page.sleep(1)
        self.event = events.get_all_events(venue_id='187')[-1]
        assert_that(self.event['name'], is_(event_name))
        assert_that(self.event['tag_list'], is_(tags))

    def test_create_new_event_with_multiple_tags_and_template(self):
        page = EventsCalendarPage(self.driver, skip_login=True)
        page.choose_venue_from_list('QA Kingdom')
        if page.driver.current_url != page.URL:
            page.go_to_page_url()
        start_time = datetimeutil.now() + datetimeutil.timedelta(days=4)
        end_time = start_time + datetimeutil.timedelta(minutes=5)
        event_name = 'event_{}'.format(''.join(random.choice(string.ascii_letters + string.digits) for x in range(20)))
        event_template_name = 'First Template'
        tags = ['tagA', 'tagB', 'tagC']
        page.add_new_event_form.create_event(event_name, start_time, end_time, event_template_name, tags)
        page.sleep(1)
        self.event = events.get_all_events(venue_id='187')[-1]
        assert_that(self.event['name'], is_(event_name))
        assert_that(self.event['tag_list'], is_(tags))
        assert_that(self.event['event_template_name'], is_(event_template_name))
