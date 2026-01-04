# tests/test_saucedemo_flow.py
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_saucedemo_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Step 1: Open site
    login_page.visit("https://www.saucedemo.com/")

    # Step 2: Login
    login_page.login("standard_user", "secret_sauce")  # demo creds

    # Step 3: Add item to cart
    inventory_page.add_first_item_to_cart()

    # Step 4: Go to cart
    inventory_page.go_to_cart()
    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(items) > 0
