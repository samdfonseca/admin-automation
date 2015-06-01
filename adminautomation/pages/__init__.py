from .basepage import BasePage
from .login import LoginPage
from .adminbase import AdminPage
from .choosevenue import ChooseVenuePage
from .eventscalendar import EventsCalendarPage
from .datatablepage import DataTablePage
from .dashboard import DashboardPage
from .suiteaccounts import SuiteAccountsPage
from .orders import OrdersPage
from .inventorystatus import InventoryStatusPage
from .items import ItemsPage

__all__ = [
    'BasePage',
    'ChooseVenuePage',
    'EventsCalendarPage',
    'LoginPage',
    'AdminPage',
    'DashboardPage',
    'SuiteAccountsPage',
    'OrdersPage',
    'InventoryStatusPage',
    'DataTablePage',
    'ItemsPage',
]
