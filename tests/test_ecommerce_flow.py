import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_ecommerce_flow(driver):
    home = HomePage(driver)
    login = LoginPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    # Step 1: Open site
    home.visit("http://automationpractice.com/index.php")

    # Step 2: Go to login
    home.go_to_login()

    # Step 3: Login
    login.login("testuser@example.com", "Password123")  # replace with valid demo account
    assert "Test User" in login.get_account_name()

    # Step 4: Search product
    home.search_product("dress")

    # Step 5: Add product to cart
    product.add_first_product_to_cart()
    time.sleep(3)  # wait for cart overlay

    # Step 6: Proceed to checkout
    cart.proceed_to_checkout()
    assert cart.is_product_in_cart()
