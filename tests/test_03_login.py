from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout(driver):
    # Maximize the browser window to ensure all elements are visible
    driver.maximize_window()

    # Navigate to login screen
    driver.get("http://127.0.0.1:5000")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Login"))).click()

    success_message = driver.find_element(By.TAG_NAME, "h1").text
    assert "Login" in success_message

     # Login
    driver.get("http://127.0.0.1:5000/login")
    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.NAME, "submit").click()


    # Verify login
    success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Logged in successfully!" in success_message

    # Log out
    driver.find_element(By.LINK_TEXT, "Logout").click()

    # Verify logout
    assert "Login" in driver.page_source
    assert "Register" in driver.page_source
    assert "Logout" not in driver.page_source