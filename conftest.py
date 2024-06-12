import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="session")
def driver(request):
     # Use the ChromeDriver from the drivers folder
    chrome_driver_path = request.config.getoption("--chromedriver-executable-path")
    service = ChromeService(executable_path=chrome_driver_path)
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Run in headless mode for CI
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--start-maximized")  # Start the browser maximized (important for login tests)
    
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--chromedriver-executable-path", action="store", default="./drivers/chromedriver.exe")