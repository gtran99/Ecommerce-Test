import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="session")
def driver():
    service = ChromeService(executable_path="./drivers/chromedriver")
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Uncomment for headless mode in CI
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--start-maximized")  # Start the browser maximized (important for login tests)
    
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
