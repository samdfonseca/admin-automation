from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import *


class NewItemDialogLocators(BaseLocatorGroup):
    FORM = css('form[name="newItemForm"]')
    FOOD_AND_BEVERAGE_RADIO = css('input[value="food"]')
    MERCHANDISE_AND_RETAIL_RADIO = css('input[value="merchandise"]')
    NAME_TEXTBOX = css('input[name="name"]')
    PRICE_TEXTBOX = css('input[name="base_price"]')
    NO_VARIANTS_RADIO = css('input[name="no variants"]')
    VARIANTS_RADIO = css('input[name="variants"]')
    VARIANTS_MULTI_SELECT = css('multi-select[ng-mogel="item.option_type_ids"] ')
    AVAILABLE_VARIANTS_SEARCHBOX = VARIANTS_MULTI_SELECT + css('div.ms-selectable '
                                                               'input.search-input')
    AVAILABLE_VARIANTS_LIST = VARIANTS_MULTI_SELECT + css('div.ms-selectable '
                                                          'ul.ms-list')
    SELECTED_VARIANTS_SEARCHBOX = VARIANTS_MULTI_SELECT + css('div.ms-selection '
                                                              'input.search-input')
    SELECTED_VARIANTS_LIST = VARIANTS_MULTI_SELECT + css('div.ms-selection '
                                                         'ul.ms-list')
    CANCEL_BUTTON = FORM + css('div.btn.grey')
    ADVANCE_BUTTON = FORM + css('div.btn.light-blue')
