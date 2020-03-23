import pytest
from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

@pytest.fixture
def browser():
  driver = webdriver.Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()

