from adminautomation.locators import BaseLocatorGroup, BaseLocator
from adminautomation.locators.datatablelocators import DataTableLocators
from adminautomation.locators.by import css
from adminautomation.structures import Select2


class LocationsLocators(DataTableLocators):
    EXPORT_BUTTON = css('a.btn.blue')
    NEW_LOCATION_BUTTON = css('a.btn.green')

class NewLocationFormLocators(BaseLocatorGroup):
    FORM = css('form[action="/locations"]')
    NAME_INPUT = css('#location_name')
    DESCRIPTION_INPUT = css('#location_description')
    TYPE_SELECT = css('#location_type')
    LOCATION_GROUP_SELECT = css('#location_location_group_id')
    DEFAULT_TRANSFER_SOURCE_SELECT = css('#location_default_transfer_source_id')
    LOCATION_TAGS_INPUT = css('#location_tag_list')
    CLOSED_RADIO_BUTTON = css('#concessionClosed')
    OPEN_RADIO_BUTTON = css('#concessionOpen')
    INSEAT_DELIVERY_CHECKBOX = css('#location_has_inseat')
    HAS_PICKUP_CHECKBOX = css('#location_has_pickup')
    MERCHANDISE_CHECKBOX = css('#location_is_merchandise')
    PAYMENT_TYPE_CHECKBOXES = css('input#location_tender_accepted_')
    PRINT_RECEIPT_TWICE_CHECKBOX = css('#location_print_receipt_twice')
    AUTO_PRINT_CASH_ORDERS_CHECKBOX = css('#location_auto_print_cash')
    ACCEPT_DIGITAL_SIGNATURES_CHECKBOX = css('#location_signature_on_tablet')
    AUTO_PRINT_CREDIT_ORDERS_CHECKBOX = css('#location_auto_print_credit')
    AUTO_PRINT_REMOTE_ORDERS_CHECKBOX = css('#location_auto_print_remote_orders')
    AUTO_PRINT_OTHER_ORDERS_CHECKBOX = css('#location_auto_print_other')
    ALLOW_TIPS_CHECKBOX = css('#location_allow_tips')
    ENABLE_EMAIL_RECEIPTS_CHECKBOX = css('#location_email_receipts_enabled')
    CANCEL_BUTTON = css('a.btn.grey[href="/locations"]')
    SAVE_LOCATION_BUTTON = css('input.btn.light-blue[value="Save Location"]')