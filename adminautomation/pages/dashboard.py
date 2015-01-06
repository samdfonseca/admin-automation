

from adminautomation.pages import AdminPage
from selenium.webdriver.common.keys import Keys


class DashboardPage(AdminPage):

    PATH = "/"

    CHECK_VALUES = {
        "page_title": "Dashboard - Index"
    }


