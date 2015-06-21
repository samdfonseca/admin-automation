from adminautomation.locators.datatablelocators import DataTableLocators
from adminautomation.locators.by import css


class LocationsLocators(DataTableLocators):
    EXPORT_BUTTON = css('a.btn.blue')
    NEW_LOCATION_BUTTON = css('a.btn.green')
