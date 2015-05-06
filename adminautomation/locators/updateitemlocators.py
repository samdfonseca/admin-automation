from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import *


class UpdateItemLocators(BaseLocatorGroup):
    CANCEL_BUTTON = css('.grey')
    UPDATE_BUTTON = css('button.pull-right:nth-child(2)')

    # General
    NAME = css('input[ng-model="item.name"]')
    BASE_PRICE = css('input[ng-model="item.base_price"]')
    DESCRIPTION = css('textarea[ng-model="item.description"]')
    SKU = css('input[ng-model="item.sku"]')
    WEIGHT = css('input[ng-model="item.weight"]')
    ALCOHOL = css('input[ng-model="item.alcohol"]')
    CATEGORY = css('bp-select[model="item.category_id"]')
    CATALOG = css('bp-select[model="item.catalog"]')
    TAX_GROUP = css('bp-select[model="item.tax_group_id"]')
    REPORTING_GROUP = css('bp-select[model="item.reporting_group_id"]')
    TOPPINGS_GROUP = css('bp-select[model="item.toppings_group_id"]')
    SIDE_GROUP = css('bp-select[model="item.side_group_id"]')

    # Menus
    SELECT_MENU_DROPDOWN = css('div[ng-model="new_menu.menu_id"]')
    MENUS_TABLE = css('table#menu_items_list"')

    # Addons
    SELECT_ADDON_GROUP_DROPDOWN = css('div[ng-model="addonGroupToAdd.id"]')
    ADDON_GROUPS_TABLE = css('table.table:nth-child(1)')

    # Inventory
    DO_NOT_TRACK_RADIO = css('input[value="no"]')
    TRACK_STOCK_ITEM_RADIO = css('input[value="track_stock_item"]')
    TRACK_RECIPE_RADIO = css('input[value="track_recipe"]')
    AUTO_CREATE_STOCK_ITEM_LINK = css('a[ng-click="createStockItemforItem()"]')
    RECIPE_DROPDOWN = css('div[ng-model="item.recipe_id"]')
