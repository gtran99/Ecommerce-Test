import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

@pytest.fixture(scope="module")
def driver():
    # Determine the path to the ChromeDriver based on the environment
    if os.name == 'nt':  # Windows
        driver_path = os.path.join('drivers', 'chromedriver.exe')
    else:  # macOS or Linux for CI
        driver_path = os.path.join('drivers', 'chromedriver')

    # Initialize the WebDriver
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
    yield driver
    driver.quit()
