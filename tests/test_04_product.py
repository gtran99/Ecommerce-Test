from selenium.webdriver.common.by import By

def test_view_product(driver):
    driver.get("http://127.0.0.1:5000/")
    product_link = driver.find_element(By.LINK_TEXT, "View")
    product_link.click()

    # Verify product page
    product_name = driver.find_element(By.TAG_NAME, "h1").text
    assert product_name is not None
