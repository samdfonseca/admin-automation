from __future__ import print_function

from adminautomation.pages import BasePage
from adminautomation.utils.locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):

    URL = "https://admin-integration.bypasslane.com"

    CHECK_VALUES = {
        "page_title": "Admin Sessions - New",
        "form_title": "Login to your account"
    }

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver.get(self.URL)

        self.FORM_TITLE = self.get_element(LoginPageLocators.FORM_TITLE)
        self.EMAIL_TEXTBOX = self.get_element(LoginPageLocators.EMAIL_TEXTBOX)
        self.PASSWORD_TEXTBOX = self.get_element(LoginPageLocators.PASSWORD_TEXTBOX)
        self.LOGIN_BUTTON = self.get_element(LoginPageLocators.LOGIN_BUTTON)


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
