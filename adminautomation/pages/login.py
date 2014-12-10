from __future__ import print_function

from adminautomation.pages import BasePage
# from adminautomation.utils.locators import LoginPageLocators
from adminautomation.utils import LoginPageLocators
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):

    URL = "https://admin-integration.bypasslane.com/admin_sessions/new"

    # Expected values to check against
    CHECK_VALUES = {
        "page_title": "Admin Sessions - New",
        "form_title": "Login to your account"
    }


    def __init__(self, driver, **kwargs):
        super(LoginPage, self).__init__(driver)

        self.URL = kwargs.get("url", self.URL)

        self.driver.get(self.URL)


    @property
    def FORM_TITLE(self):
        return self.get_element(LoginPageLocators.FORM_TITLE)


    @property
    def EMAIL_TEXTBOX(self):
        return self.get_element(LoginPageLocators.EMAIL_TEXTBOX)


    @property
    def PASSWORD_TEXTBOX(self):
        return self.get_element(LoginPageLocators.PASSWORD_TEXTBOX)


    @property
    def LOGIN_BUTTON(self):
        return self.get_element(LoginPageLocators.LOGIN_BUTTON)


    def is_form_title_match(self, custom_message=None):
        """
        Checks that the login form title matches the expected value.

        :param custom_message: a custom message to throw if the assertion fails
        """

        found_form_title = self.FORM_TITLE.text
        self.check_value("form_title", found_form_title, custom_message=custom_message)


    def enter_email(self, email):
        """
        Enter an email into the login form.

        :param email: an email as a string
        """

        self.EMAIL_TEXTBOX.send_keys(email)


    def enter_password(self, passwd):
        """
        Enter a password into the login form.

        :param passwd: a password as a string
        """

        self.PASSWORD_TEXTBOX.send_keys(passwd)


    def click_login_button(self):
        """
        Simulates clicking the login button.
        """

        self.LOGIN_BUTTON.click()


    def press_return_in_email_field(self):
        """
        Simulates pressing the Return key while focused on the email field.
        """

        self.EMAIL_TEXTBOX.send_keys(Keys.RETURN)


    def press_return_in_password_field(self):
        """
        Simulates pressing the Return key while focused on the password field.
        """

        self.PASSWORD_TEXTBOX.send_keys(Keys.RETURN)


    def login(self, email, password):
        """
        Simulates the standard login workflow. Submits form by clicking login button.

        :param email: an email as a string
        :param password: a password as a string
        """

        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()


    def check_for_invalid_login_toast(self):
        """
        Checks for the existence of the invalid login toast.

        :return: a bool based on if the toast is found
        """

        return self.check_exists(LoginPageLocators.INVALID_LOGIN_TOAST)
