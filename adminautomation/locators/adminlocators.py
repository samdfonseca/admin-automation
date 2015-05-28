from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import css


class AdminPageLocators(BaseLocatorGroup):

    PAGE_TITLE = css('h3.page-title')
    BREADCRUMB_LINKS = css('ul.breadcrumb a')
    PORTLET_TITLE = css('div.portlet-title div.caption')

