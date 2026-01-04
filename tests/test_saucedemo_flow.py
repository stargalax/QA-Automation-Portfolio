import pytest
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_purchase(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Step 1: Open site and login
    login.visit("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")

    # Step 2: Add first item to cart
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    # Step 3: Remove item (test remove functionality)
    cart.remove_first_item()
    inventory.go_to_cart()  # go back to inventory
    inventory.add_first_item_to_cart()

    # Step 4: Verify cart is empty
    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(items) == 0
    # # Step 4: Go to checkout and complete purchase
    # cart.go_to_checkout()
    # checkout.fill_info("John", "Doe", "12345")
    # checkout.complete_order()
