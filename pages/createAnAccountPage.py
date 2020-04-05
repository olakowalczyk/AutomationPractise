from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


class CreateAccountInfo:

    ACCOUNT_CREATION_FORM = (By.ID, 'account-creation_form')
    FIRST_NAME_INPUT = (By.ID, 'customer_firstname')
    LAST_NAME_INPUT = (By.ID, 'customer_lastname')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'passwd')
    ADDRESS_INPUT = (By.ID, 'address1')
    CITY_INPUT = (By.ID, 'city')
    STATE_DROPDOWN = (By.ID, 'id_state')
    POSTAL_CODE_INPUT = (By.ID, 'postcode')
    COUNTRY_DROPDOWN = (By.ID, 'id_country')
    MOBILE_PHONE_INPUT = (By.ID, 'phone_mobile')
    REGISTER_BUTTON = (By.ID, 'submitAccount')

    ERROR_MESSAGE = (By.CSS_SELECTOR, '#center_column > div')

    def __init__(self, browser):
        self.browser = browser

    def is_account_creation_form_available(self):
        form = self.browser.find_element(*self.ACCOUNT_CREATION_FORM)
        if form.is_displayed:
            return True
        return False

    def input_account_data(self, firstname, lastname, password, address, city, state, postcode, country, mobilephone):
        input_field = self.browser.find_element(*self.FIRST_NAME_INPUT)
        input_field.send_keys(firstname)
        input_field = self.browser.find_element(*self.LAST_NAME_INPUT)
        input_field.send_keys(lastname)
        input_field = self.browser.find_element(*self.PASSWORD_INPUT)
        input_field.send_keys(password)
        input_field = self.browser.find_element(*self.ADDRESS_INPUT)
        input_field.send_keys(address)
        input_field = self.browser.find_element(*self.CITY_INPUT)
        input_field.send_keys(city)
        dropdown = self.browser.find_element(*self.STATE_DROPDOWN)
        dropdown.send_keys(state)
        input_field = self.browser.find_element(*self.POSTAL_CODE_INPUT)
        input_field.send_keys(postcode)
        dropdown = self.browser.find_element(*self.COUNTRY_DROPDOWN)
        dropdown.send_keys(country)
        input_field = self.browser.find_element(*self.MOBILE_PHONE_INPUT)
        input_field.send_keys(mobilephone)

    def register_account(self):
        submit = self.browser.find_element(*self.REGISTER_BUTTON)
        submit.click()

    def is_required_firstname_error_message_displayed(self):
        msg = self.browser.find_element(*self.ERROR_MESSAGE).text
        if 'firstname is required' in msg:
            return True
        return False

    def is_required_lastname_error_message_displayed(self):
        msg = self.browser.find_element(*self.ERROR_MESSAGE).text
        if 'lastname is required' in msg:
            return True
        return False

    def is_required_password_error_message_displayed(self):
        msg = self.browser.find_element(*self.ERROR_MESSAGE).text
        if 'passwd is required' in msg:
            return True
        return False

    def is_invalid_password_error_message_displayed(self):
        msg = self.browser.find_element(*self.ERROR_MESSAGE).text
        if 'passwd is invalid' in msg:
            return True
        return False

    def is_required_address_error_message_displayed(self):
        msg = self.browser.find_element(*self.ERROR_MESSAGE).text
        if 'address1 is required' in msg:
            return True
        return False

    def is_required_city_error_message_displayed(self):
        msg = self.browser.find_element(*self.ERROR_MESSAGE).text
        if 'city is required' in msg:
            return True
        return False

    def is_required_state_error_message_displayed(self):
        msg = self.browser.find_element(*self.ERROR_MESSAGE).text
        if 'This country requires you to choose a State' in msg:
            return True
        return False

    def is_zipcode_error_message_displayed(self):
        msg = self.browser.find_element(*self.ERROR_MESSAGE).text
        if "The Zip/Postal code you've entered is invalid. It must follow this format: 00000" in msg:
            return True
        return False

    def is_required_country_error_message_displayed(self):
        msg = self.browser.find_element(*self.ERROR_MESSAGE).text
        if 'Country is invalid' in msg:
            return True
        return False

    def is_required_mobilephone_error_message_displayed(self):
        msg = self.browser.find_element(*self.ERROR_MESSAGE).text
        if 'You must register at least one phone number' in msg:
            return True
        return False
