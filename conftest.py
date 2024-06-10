import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Run in headless mode for CI
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # driver = webdriver.Chrome(service=service, options=options)

     # Maximize the browser window (important for login tests)
    driver.maximize_window()
    yield driver
    driver.quit()