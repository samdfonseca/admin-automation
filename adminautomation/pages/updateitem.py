from adminautomation.pages import AdminPage
from adminautomation.locators import UpdateItemLocators


class UpdateItemPage(AdminPage):

    locators = UpdateItemLocators

    @property
    def NAME(self):
        return self.get_element(self.locators.NAME)

    @property
    def BASE_PRICE(self):
        return self.get_element(self.locators.BASE_PRICE)

    @property
    def DESCRIPTION(self):
        return self.get_element(self.locators.DESCRIPTION)

    @property
    def SKU(self):
        return self.get_element(self.locators.SKU)

    @property
    def WEIGHT(self):
        return self.get_element(self.locators.WEIGHT)

    @property
    def ALCOHOL(self):
        return self.get_element(self.locators.ALCOHOL)

    @property
    def CATEGORY(self):
        return self.get_element(self.locators.CATEGORY)

    @property
    def CATALOG(self):
        return self.get_element(self.locators.CATALOG)

    @property
    def TAX_GROUP(self):
        return self.get_element(self.locators.TAX_GROUP)

    @property
    def REPORTING_GROUP(self):
        return self.get_element(self.locators.REPORTING_GROUP)

    @property
    def TOPPINGS_GROUP(self):
        return self.get_element(self.locators.TOPPINGS_GROUP)

    @property
    def SIDE_GROUP(self):
        return self.get_element(self.locators.SIDE_GROUP)

    @property
    def SELECT_MENU_DROPDOWN(self):
        return self.get_element(self.locators.SELECT_MENU_DROPDOWN)

    @property
    def MENUS_TABLE(self):
        return self.get_element(self.locators.MENUS_TABLE)

    @property
    def SELECT_ADDON_GROUP_DROPDOWN(self):
        return self.get_element(self.locators.SELECT_ADDON_GROUP_DROPDOWN)

    @property
    def ADDON_GROUPS_TABLE(self):
        return self.get_element(self.locators.ADDON_GROUPS_TABLE)

