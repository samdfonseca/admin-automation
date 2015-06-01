from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from adminautomation.pages import BasePage, AdminPage
from adminautomation.locators import EventsCalendarLocators
from adminautomation.structures import Select2, PageSection, AdminElement


class EventsCalendarPage(AdminPage):
    PATH = '/events'
    locators = EventsCalendarLocators

    # def __init__(self, *args, **kwargs):
    #     kwargs['skip_login'] = True
    #     super(EventsCalendarPage, self).__init__(self, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(EventsCalendarPage, self).__init__(*args, **kwargs)
        self.add_new_event_form = self.AddNewEventForm(self)
        self.calendar_view = self.CalendarView(self)
        self.calendar_view.month_view = self.calendar_view.MonthView(self)
        self.calendar_view.week_view = self.calendar_view.WeekView(self)
        self.calendar_view.day_view = self.calendar_view.DayView(self)
        self.event_list_view = self.EventListView(self)
        self.event_list_view.event_list_table = self.event_list_view.EventListTable(self, self.locators.EventListLocators.EVENT_LIST_TABLE)

    class AddNewEventForm(PageSection):
        DEFAULT_DATE_FORMAT = '%B %d, %Y %I:%M %p'

        @property
        def NAME(self):
            return self._page.get_element(self._page.locators.AddNewEventLocators.NAME)

        @property
        def START_DATE(self):
            return self._page.get_element(self._page.locators.AddNewEventLocators.START_DATE)

        @property
        def END_DATE(self):
            return self._page.get_element(self._page.locators.AddNewEventLocators.END_DATE)

        @property
        def EVENT_TEMPLATE(self):
            return Select2(self._page.get_element(self._page.locators.AddNewEventLocators.EVENT_TEMPLATE))

        @property
        def EVENT_TYPE(self):
            return self._page.get_element(self._page.locators.AddNewEventLocators.EVENT_TYPE)

        @property
        def CREATE_EVENT_BUTTON(self):
            return self._page.get_element(self._page.locators.AddNewEventLocators.CREATE_EVENT_BUTTON)

        def enter_name(self, name):
            """
            :param str name:
            :return:
            """
            self.NAME.send_keys(name)

        @staticmethod
        def enter_date(date_input_element, date, date_format=None):
            """
            :param date_element:
            :param date:
            :param_date_format:
            :return:
            """
            date_format = EventsCalendarPage.AddNewEventForm.DEFAULT_DATE_FORMAT if date_format is None else date_format
            date_input_element.clear()
            date_input_element.send_keys(date.strftime(date_format))
            date_input_element.click()

        def enter_start_date(self, date, date_format=None):
            """
            :param date:
            :param date_format:
            :return:
            """
            self.enter_date(self.START_DATE, date, date_format)

        def enter_end_date(self, date, date_format=None):
            """
            :param date:
            :param date_format:
            :return:
            """
            self.enter_date(self.END_DATE, date, date_format)

        def enter_event_template(self, template_name):
            """

            :param template_name:
            :return:
            """
            self.EVENT_TEMPLATE.select_by_visible_text(template_name)

        def enter_event_type(self, event_type):
            """

            :param event_type:
            :return:
            """
            self.EVENT_TYPE.send_keys(event_type)

        def click_create_event_button(self):
            """

            :return:
            """
            self.CREATE_EVENT_BUTTON.click()

        def create_event(self, name, start_date, end_date, template_name=None, event_type=None, **kwargs):
            """

            :param name:
            :param start_date:
            :param end_date:
            :param template_name:
            :return:
            """
            self.enter_name(name)
            self.enter_start_date(start_date, kwargs.get('start_date_format'))
            self.enter_end_date(end_date, kwargs.get('end_date_format'))
            if template_name:
                self.enter_event_template(template_name)
            if event_type:
                self.enter_event_type(event_type)
            self.click_create_event_button()

    class CalendarView(PageSection):
        @property
        def MONTH_BUTTON(self):
            return self._page.get_element(self._page.locators.CalendarViewLocators.MONTH_BUTTON)

        @property
        def WEEK_BUTTON(self):
            return self._page.get_element(self._page.locators.CalendarViewLocators.WEEK_BUTTON)

        @property
        def DAY_BUTTON(self):
            return self._page.get_element(self._page.locators.CalendarViewLocators.DAY_BUTTON)

        @property
        def TODAY_BUTTON(self):
            return self._page.get_element(self._page.locators.CalendarViewLocators.TODAY_BUTTON)

        @property
        def PREV_BUTTON(self):
            return self._page.get_element(self._page.locators.CalendarViewLocators.PREV_BUTTON)

        @property
        def NEXT_BUTTON(self):
            return self._page.get_element(self._page.locators.CalendarViewLocators.NEXT_BUTTON)

        @property
        def CALENDAR_TITLE(self):
            return self._page.get_element(self._page.locators.CalendarViewLocators.CALENDAR_TITLE)

        class CalendarViewSection(PageSection):
            def open(self, wait_for=None):
                self.open_view_button.click()
                if wait_for:
                    self._page.wait_for_element(wait_for)

        class MonthView(CalendarViewSection):
            def __init__(self, *args, **kwargs):
                super(EventsCalendarPage.CalendarView.MonthView, self).__init__(*args, **kwargs)
                self.open_view_button = self._page.calendar_view.MONTH_BUTTON

            @property
            def ALL_DAYS(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.MonthViewLocators.ALL_DAYS)

            @property
            def HEADERS(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.MonthViewLocators.HEADER)

            @property
            def PREV_MONTH_DAYS(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.MonthViewLocators.PREV_MONTH_DAYS)

            @property
            def NEXT_MONTH_DAYS(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.MonthViewLocators.NEXT_MONTH_DAYS)

            @property
            def TODAY(self):
                return self._page.get_element(self._page.locators.CalendarViewLocators.MonthViewLocators.TODAY)

            @property
            def EVENTS(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.MonthViewLocators.EVENTS)

            @property
            def EVENT_NAMES(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.MonthViewLocators.EVENT_NAMES)

        class WeekView(CalendarViewSection):
            def __init__(self, *args, **kwargs):
                super(EventsCalendarPage.CalendarView.WeekView, self).__init__(*args, **kwargs)
                self.open_view_button = self._page.calendar_view.WEEK_BUTTON

            @property
            def ALL_DAYS(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.WeekViewLocators.ALL_DAYS)

            @property
            def HEADERS(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.WeekViewLocators.HEADER)

            @property
            def PAST_DAYS(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.WeekViewLocators.PAST_DAYS)

            @property
            def FUTURE_DAYS(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.WeekViewLocators.FUTURE_DAYS)

            @property
            def TODAY(self):
                return self._page.get_element(self._page.locators.CalendarViewLocators.WeekViewLocators.TODAY)

            @property
            def EVENTS(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.WeekViewLocators.EVENTS)

            @property
            def EVENT_NAMES(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.WeekViewLocators.EVENT_NAMES)

        class DayView(CalendarViewSection):
            def __init__(self, *args, **kwargs):
                super(EventsCalendarPage.CalendarView.DayView, self).__init__(*args, **kwargs)
                self.open_view_button = self._page.calendar_view.DAY_BUTTON

            @property
            def DAY_OF_WEEK(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.DayViewLocators.DAY_OF_WEEK)

            @property
            def EVENTS(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.DayViewLocators.EVENTS)

            @property
            def EVENT_NAMES(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.DayViewLocators.EVENT_NAMES)

    class EventListView(PageSection):
        class EventListTable(AdminElement):
            locators = EventsCalendarLocators.EventListLocators()

            @property
            def headers(self):
                return self.get_elements(self.locators.HEADERS)

            @property
            def name_header(self):
                return self.get_element(self.locators.NAME_HEADER)

            @property
            def start_header(self):
                return self.get_element(self.locators.START_HEADER)

            @property
            def end_header(self):
                return self.get_element(self.locators.END_HEADER)

            @property
            def type_header(self):
                return self.get_element(self.locators.TYPE_HEADER)

            @property
            def event_template_header(self):
                return self.get_element(self.locators.EVENT_TEMPLATE_HEADER)

    @property
    def calendar_view_tab(self):
        return self.get_element(self.locators.CALENDAR_VIEW_TAB)

    @property
    def events_list_view_tab(self):
        return self.get_element(self.locators.EVENTS_LIST_VIEW_TAB)

    def open_calendar_view_tab(self):
        self.calendar_view_tab.click()

    def open_events_list_view_tab(self):
        self.events_list_view_tab.click()
