from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome

class MyAccount:

	NAV_MY_ACCOUNT = (By.CSS_SELECTOR, '#header > div.nav > div > div > nav > div:nth-child(1)')
	NAV_SIGN_OUT = (By.CSS_SELECTOR, '#header > div.nav > div > div > nav > div:nth-child(2) > a')

	def __init__(self, browser):
		self.browser = browser

	def log_out(self):
		sign_out = self.browser.find_element(*self.NAV_SIGN_OUT)
		sign_out.click()

	def is_my_account_page_available(self, name):
		nav_element = self.browser.find_element(*self.NAV_MY_ACCOUNT)
		text = self.browser.find_element(*self.NAV_MY_ACCOUNT).text
		if text == name: return True
		return False

	