from pages.loginPage import CreateAccount
from pages.createAnAccountPage import CreateAccountInfo
from pages.myAccountPage import MyAccount
from selenium.webdriver import Chrome
import pytest
import requests
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

pytest_plugins = [
  'tests.config.browser'
]

def generate_email(): # gets generated email from website
    url = "https://generator.email/"
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    element = soup.find('span', attrs={'id' : 'email_ch_text'}).getText()
    return element

def test_01_invalid_email(browser):
	test_data = 'test'
	create_account_page = CreateAccount(browser)
	create_account_page.load()
	create_account_page.enter_email(test_data)
	create_account_page.create_account()
	assert create_account_page.is_invalid_email_message()

def test_02_existing_email(browser):
	test_data = 'test202003@test.com'
	create_account_page = CreateAccount(browser)
	create_account_page.load()
	create_account_page.enter_email(test_data)
	create_account_page.create_account()
	assert create_account_page.is_already_registered_message()

@pytest.mark.smoketest
def test_03_valid_email(browser):
	test_data = generate_email()
	create_account_page = CreateAccount(browser)
	registration_page = CreateAccountInfo(browser)
	create_account_page.load()
	create_account_page.enter_email(test_data)
	create_account_page.create_account()
	assert registration_page.is_account_creation_form_available()

def test_04_invalid_registration_missing_required_fields(browser):
	test_data = {'firstname':'', 
	'lastname': '', 
	'password': '', 
	'address': '', 
	'city': '', 
	'state': '', 
	'postcode' : '', 
	'country' : 'United States', 
	'mobilephone': ''}
	test_03_valid_email(browser)
	registration_page = CreateAccountInfo(browser)
	registration_page.input_account_data(**test_data)
	registration_page.register_account()
	assert registration_page.is_required_firstname_error_message_displayed()
	assert registration_page.is_required_lastname_error_message_displayed()
	assert registration_page.is_required_password_error_message_displayed()
	assert registration_page.is_required_address_error_message_displayed()
	assert registration_page.is_required_city_error_message_displayed()
	assert registration_page.is_required_state_error_message_displayed()
	assert registration_page.is_zipcode_error_message_displayed()
	assert registration_page.is_required_mobilephone_error_message_displayed()

def test_05_invalid_registration_password_too_short(browser):
	test_data = {'firstname':'Test', 
	'lastname': 'Test', 
	'password': 'pass', # must be at least 5-characters
	'address': 'Street 21', 
	'city': 'Montgomery', 
	'state': 'Alabama', 
	'postcode' : '12345', 
	'country' : 'United States', 
	'mobilephone': '123456789'}
	test_03_valid_email(browser)
	registration_page = CreateAccountInfo(browser)
	registration_page.input_account_data(**test_data)
	registration_page.register_account()
	assert registration_page.is_invalid_password_error_message_displayed()

def test_06_invalid_registration_zipcode_not_00000(browser):
	test_data = {'firstname':'Test', 
	'lastname': 'Test', 
	'password': 'password', 
	'address': 'Street 21', 
	'city': 'Montgomery', 
	'state': 'Alabama', 
	'postcode' : '1234', # must match 00000
	'country' : 'United States', 
	'mobilephone': '123456789'}
	test_03_valid_email(browser)
	registration_page = CreateAccountInfo(browser)
	registration_page.input_account_data(**test_data)
	registration_page.register_account()
	assert registration_page.is_zipcode_error_message_displayed()

@pytest.mark.smoketest
def test_07_valid_registration(browser):
	test_data = {'firstname':'Test', 
	'lastname': 'Test', 
	'password': 'password', 
	'address': 'Street 21', 
	'city': 'Montgomery', 
	'state': 'Alabama', 
	'postcode' : '12345',
	'country' : 'United States', 
	'mobilephone': '123456789'}
	test_03_valid_email(browser)
	registration_page = CreateAccountInfo(browser)
	my_account_page = MyAccount(browser)
	registration_page.input_account_data(**test_data)
	registration_page.register_account()
	customer_name = str(test_data.get('firstname')) + ' ' + str(test_data.get('lastname'))
	assert my_account_page.is_my_account_page_available(customer_name)