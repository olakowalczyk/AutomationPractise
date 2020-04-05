from pages.loginPage import SignIn
from pages.myAccountPage import MyAccount
import pytest
from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

pytest_plugins = [
    'tests.config.browser'
]


def test_08_invalid_email(browser):
    test_data = {'email': 'invalidtest202003@test.com',
                 'password': 'password202003'}
    sign_in_page = SignIn(browser)
    sign_in_page.load()
    sign_in_page.sign_in(test_data.get('email'), test_data.get('password'))
    assert sign_in_page.is_invalid_error_message_displayed()


def test_09_invalid_password(browser):
    test_data = {'email': 'test202003@test.com',
                 'password': 'invalidpassword202003'}
    sign_in_page = SignIn(browser)
    sign_in_page.load()
    sign_in_page.sign_in(test_data.get('email'), test_data.get('password'))
    assert sign_in_page.is_invalid_error_message_displayed()


@pytest.mark.smoketest
def test_10_valid_login(browser):
    test_data = {'email': 'test202003@test.com',
                 'password': 'password202003',
                 'firstname': 'Test',
                 'lastname': 'Test'}
    sign_in_page = SignIn(browser)
    my_account_page = MyAccount(browser)
    sign_in_page.load()
    sign_in_page.sign_in(test_data.get('email'), test_data.get('password'))
    name = str(test_data.get('firstname')) + \
        ' ' + str(test_data.get('lastname'))
    assert my_account_page.is_my_account_page_available(name)


@pytest.mark.smoketest
def test_11_valid_logout(browser):
    test_10_valid_login((browser))
    my_account_page = MyAccount(browser)
    sign_in_page = SignIn(browser)
    my_account_page.log_out()
    assert sign_in_page.is_sign_in_page_available()
