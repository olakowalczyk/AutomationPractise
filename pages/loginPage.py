from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


class CreateAccount:

    LOCATION = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
    EMAIL_INPUT = (By.ID, 'email_create')
    CREATE_ACCOUNT_BUTTON = (By.ID, 'SubmitCreate')
    INVALID_EMAIL_MESSAGE = (By.CSS_SELECTOR, '#create_account_error>ol>li')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.LOCATION)

    def enter_email(self, email):
        email_input = self.browser.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(email)

    def create_account(self):
        submit_click = self.browser.find_element(*self.CREATE_ACCOUNT_BUTTON)
        submit_click.click()

    def is_invalid_email_message(self):
        msg = self.browser.find_element(*self.INVALID_EMAIL_MESSAGE).text
        if msg == 'Invalid email address.':
            return True
        return False

    def is_already_registered_message(self):
        msg = self.browser.find_element(*self.INVALID_EMAIL_MESSAGE).text
        if 'An account using this email address has already been registered.' in msg:
            return True
        return False


class SignIn:

    LOCATION = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    SIGN_IN_BUTTON = (By.ID, 'SubmitLogin')
    INVALID_MESSAGE = (
        By.CSS_SELECTOR, '#center_column > div.alert.alert-danger > ol > li')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.LOCATION)

    def sign_in(self, email, password):
        email_input = self.browser.find_element(*self.EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*self.PASSWORD)
        password_input.send_keys(password)
        submit = self.browser.find_element(*self.SIGN_IN_BUTTON)
        submit.click()

    def is_sign_in_page_available(self):
        try:
            element = self.browser.find_element(*self.SIGN_IN_BUTTON)
        except NoSuchElementException:
            return False
        return True

    def is_invalid_error_message_displayed(self):
        msg = self.browser.find_element(*self.INVALID_MESSAGE).text
        if 'Authentication failed' in msg:
            return True
        return False
