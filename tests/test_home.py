def test_home_page(driver):
    driver.get("http://127.0.0.1:5000/")
    assert "E-Commerce" in driver.title

    # Verify product list
    products = driver.find_elements_by_class_name("card")
    assert len(products) > 0
