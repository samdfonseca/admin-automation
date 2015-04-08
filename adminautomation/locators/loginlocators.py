from adminautomation.locators import BaseLocatorGroup
from adminautomation.locators.by import css


class LoginPageLocators(BaseLocatorGroup):
    EMAIL_TEXTBOX = css('input#user_email')
    PASSWORD_TEXTBOX = css('input#user_password')
    LOGIN_BUTTON = css('button.btn')
    FORM_TITLE = css('h3.form-title')
    INVALID_LOGIN_TOAST = css('div#toast-container')
    INVALID_LOGIN_TOAST_MESSAGE = css('div.toast-message')
