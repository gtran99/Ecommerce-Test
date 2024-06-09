import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    # Initialize the WebDriver with WebDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()