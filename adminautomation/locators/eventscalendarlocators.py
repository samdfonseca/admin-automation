from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import css


class EventsCalendarLocators(BaseLocatorGroup):
    CALENDAR_VIEW_TAB = css('a[href="#calendar"]')
    EVENTS_LIST_VIEW_TAB = css('a[href="#events"]')

    class AddNewEventLocators(BaseLocatorGroup):
        NAME = css('input[ng-model="event.name"]')
        START_DATE = css('input[ng-model="event.starts_at"]')
        END_DATE = css('input[ng-model="event.ends_at"]')
        EVENT_TEMPLATE = css('div.event-template')
        EVENT_TYPE = css('div.event-type')
        CREATE_EVENT_BUTTON = css('input.btn[value="Create Event"]')

    class CalendarViewLocators(BaseLocatorGroup):
        CALENDAR_TAB = css('div#calendar')
        MONTH_BUTTON = css('button.fc-month-button')
        WEEK_BUTTON = css('button.fc-agendaWeek-button')
        DAY_BUTTON = css('button.fc-agendaDay-button')
        TODAY_BUTTON = css('button.fc-today-button')
        PREV_BUTTON = css('button.fc-prev-button')
        NEXT_BUTTON = css('button.fc-next-button')
        CALENDAR_TITLE = css('div.fc-center')

        class MonthViewLocators(BaseLocatorGroup):
            ALL_DAYS = css('.fc-day')
            HEADERS = css('.fc-day-header')
            PREV_MONTH_DAYS = css('.fc-other-month.fc-past')
            NEXT_MONTH_DAYS = css('.fc-other-month.fc-future')
            SUNDAYS = css('.fc-day.fc-sun')
            MONDAYS = css('.fc-day.fc-mon')
            TUESDAYS = css('.fc-day.fc-tue')
            WEDNESDAYS = css('.fc-day.fc-wed')
            THURSDAYS = css('.fc-day.fc-thu')
            FRIDAYS = css('.fc-day.fc-fri')
            SATURDAYS = css('.fc-day.fc-sat')
            TODAY = css('.fc-today')
            EVENTS = css('.fc-events')
            EVENT_NAMES = css('.fc-title')

        class WeekViewLocators(BaseLocatorGroup):
            ALL_DAYS = css('.fc-day')
            HEADERS = css('.fc-day-header')
            SUNDAY = css('.fc-day.fc-sun')
            MONDAY = css('.fc-day.fc-mon')
            TUESDAY = css('.fc-day.fc-tue')
            WEDNESDAY = css('.fc-day.fc-wed')
            THURSDAY = css('.fc-day.fc-thu')
            FRIDAY = css('.fc-day.fc-fri')
            SATURDAY = css('.fc-day.fc-sat')
            TODAY = css('.fc-day.fc-today')
            PAST_DAYS = css('.fc-day.fc-past')
            FUTURE_DAYS = css('.fc-day.fc-future')
            EVENTS = css('.fc-event')
            EVENT_NAMES = css('.fc-title')

        class DayViewLocators(BaseLocatorGroup):
            DAY_OF_WEEK = css('.fc-day-header')
            EVENTS = css('.fc-event')
            EVENT_NAMES = css('.fc-title')

    class EventsListLocators(BaseLocatorGroup):
        EVENTS_LIST_TABLE = css('table.event_list')
        HEADERS = css('thead tr:nth-child(1) th')
        NAME_HEADER = css('th:nth-child(1)')
        START_HEADER = css('th:nth-child(2)')
        END_HEADER = css('th:nth-child(3)')
        TYPE_HEADER = css('th:nth-child(4)')
        EVENT_TEMPLATE_HEADER = css('th:nth-child(5)')
        EVENT_ROWS = css('tr[ng-repeat="event in events"]')
