import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

@pytest.fixture(scope="module")
def driver():
    # Assuming chromedriver is placed in the 'drivers' directory
    #print(os.path.dirname(__file__), "drivers", "chromedriver")
    chrome_driver_path = os.path.join(os.path.dirname(__file__), "drivers", "chromedriver.exe")

    print(f"Using ChromeDriver from: {chrome_driver_path}")  # Debugging line

    # Create a Service object with the path to the ChromeDriver
    service = Service(executable_path=chrome_driver_path)

    # Initialize the WebDriver with the service object
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
    yield driver
    driver.quit()
