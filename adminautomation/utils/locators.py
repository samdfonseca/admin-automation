from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    EMAIL_TEXTBOX = (By.ID, 'user_email')
    PASSWORD_TEXTBOX = (By.ID, 'user_password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.btn')
    FORM_TITLE = (By.CLASS_NAME, 'form-title')
    INVALID_LOGIN_TOAST = (By.CLASS_NAME, 'toast-container')
    INVALID_LOGIN_TOAST_MESSAGE = (By.CLASS_NAME, 'toast-message')


class ChooseVenueLocators(object):
    VENUES_LISTBOX = (By.ID, 's2id_change_venue')
    VENUE_LIST_SEARCHBOX = (By.CLASS_NAME, 'select2-input')
    VENUE_LIST = (By.CLASS_NAME, 'select2-results')
    VENUE_LIST_ITEMS = (By.CLASS_NAME, 'select2-result')
    VENUE_OPTIONS = (By.XPATH, '//select[@id="change_venue"]/option')
    GO_BUTTON = (By.CSS_SELECTOR, 'button.btn')
    FORM_TITLE = (By.CLASS_NAME, 'form-title')
