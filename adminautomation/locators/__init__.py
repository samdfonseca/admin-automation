from adminautomation.locators.by import BaseLocator


class DuplicateLocatorNameException(Exception):
    message = 'BaseLocator objects use the same name for a locator attribute. Unable to add together.'


class BaseLocatorGroup(object):
    @classmethod
    def _locators(cls):
        return {k: v for k, v in cls.__dict__.items() if isinstance(v, BaseLocator)}

    def __add__(self, other):
        """
        :type other: BaseLocatorGroup
        :return:
        """
        locators_b = other._locators()
        for locator_name, locator_obj in locators_b.iteritems():
            if self.__dict__.get(locator_name):
                raise DuplicateLocatorNameException('Both objects have attribute: {}. '
                                                    'Unable to merge.'.format(locator_name))
            self.__setattr__(locator_name, locator_obj)
        return self


from .adminlocators import AdminPageLocators
from .choosevenuelocators import ChooseVenueLocators
from .eventscalendarlocators import EventsCalendarLocators
from .inventorystatuslocators import InventoryStatusLocators
from .itemslocators import ItemsLocators
from .loginlocators import LoginPageLocators
from .navbarlocators import NavBarLocators
from .newitemlocators import NewItemDialogLocators
from .orderslocators import OrdersLocators
from .sidebarlocators import SidebarLocators
from .suiteaccountlocators import SuiteAccountsLocators, ModifySuiteAccountLocators
from .updateitemlocators import UpdateItemLocators
