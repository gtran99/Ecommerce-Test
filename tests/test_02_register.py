from selenium.webdriver.common.by import By

def test_register(driver):
    driver.get("http://127.0.0.1:5000/register")
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.NAME, "confirm_password").send_keys("password")
    driver.find_element(By.NAME, "submit").click()

    # Verify registration success
    success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Account created successfully!" in success_message
