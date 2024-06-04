from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_home_page(driver):
    driver.get("http://127.0.0.1:5000/")
    
    # Wait until the title contains "E-Commerce"
    WebDriverWait(driver, 10).until(EC.title_contains("E-Commerce"))
    
    # Verify the presence of product cards
    products = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "card")))
    
    # Assert that at least one product card is present
    assert len(products) > 0, "No product cards found on the home page"
