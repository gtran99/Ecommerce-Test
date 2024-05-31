from selenium.webdriver.common.by import By

def test_login(driver):
    driver.get("http://127.0.0.1:5000/login")
    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.NAME, "submit").click()

    # Verify login success
    success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Logged in successfully!" in success_message
