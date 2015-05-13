from adminautomation.pages import BasePage, AdminPage
from adminautomation.locators import EventsCalendarLocators
from adminautomation.structures import Select2, PageSection


class EventsCalendarPage(AdminPage):
    PATH = '/events'
    locators = EventsCalendarLocators

    class AddNewEventForm(PageSection):
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

        class MonthView(PageSection):
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

        class WeekView(PageSection):
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

        class DayView(PageSection):
            @property
            def DAY_OF_WEEK(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.DayViewLocators.DAY_OF_WEEK)

            @property
            def EVENTS(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.DayViewLocators.EVENTS)

            @property
            def EVENT_NAMES(self):
                return self._page.get_elements(self._page.locators.CalendarViewLocators.DayViewLocators.EVENT_NAMES)



    def __init__(self, *args, **kwargs):
        super(EventsCalendarPage, self).__init__(*args, **kwargs)
        self.add_new_event_form = self.AddNewEventForm(self)
        self.calendar_view = self.CalendarView(self)
        self.calendar_view.month_view = self.calendar_view.MonthView(self)

