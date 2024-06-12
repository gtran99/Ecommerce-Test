import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="session")
def driver():
    service = ChromeService(executable_path="./drivers/chromedriver")
    # service = ChromeService(executable_path="./drivers/chromedriver.exe")  Uncomment if testing locally on Windows
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode for CI
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage') # Prevent issues due to limited shared memory
    options.add_argument('--disable-gpu') # Disable GPU hardware acceleration
    options.add_argument('--remote-debugging-port=9222') # Enable remote debugging
    options.add_argument("--window-size=1920,1080")  # Ensure sufficient size for UI elements
    options.add_argument('--disable-extensions') 
    options.add_argument('--disable-software-rasterizer')

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
