# tests/test_edge_cases.py
import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.edge
def test_invalid_login(driver):
    """Attempt login with invalid credentials."""
    login = LoginPage(driver)
    login.visit("https://www.saucedemo.com/")

    # Wrong username
    login.login("wrong_user", "secret_sauce")
    assert "Username and password do not match" in login.get_error_message()

    # Wrong password
    login.login("standard_user", "wrong_pass")
    assert "Username and password do not match" in login.get_error_message()

    # Empty fields
    login.login("", "")
    assert "Username and password do not match" in login.get_error_message()


@pytest.mark.edge
def test_locked_out_user(driver):
    """Check that locked_out_user cannot login."""
    login = LoginPage(driver)
    login.visit("https://www.saucedemo.com/")
    login.login("locked_out_user", "secret_sauce")
    assert "locked out" in login.get_error_message().lower()
@pytest.mark.edge
def test_checkout_empty_cart(driver):
    """Attempt checkout with empty cart (should be blocked)."""
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.visit("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")

    # Go to cart without adding items
    inventory.go_to_cart()
    assert cart.is_cart_empty(), "Cart should be empty"

    # Check that checkout has no items
    cart.click(cart.CHECKOUT_BUTTON)
    checkout = CheckoutPage(driver)
    assert checkout.get_items_count() == 0, "Checkout should have 0 items when cart is empty"


@pytest.mark.edge
def test_sorting_inventory(driver):
    """Test sorting filters on inventory page."""
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.visit("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")

    # Sort by price low → high
    inventory.sort_by("Price (low to high)")
    prices = [float(p.text.replace("$", "")) for p in inventory.get_item_prices()]
    assert prices == sorted(prices), "Prices are not sorted low → high"

    # Sort by price high → low
    inventory.sort_by("Price (high to low)")
    prices = [float(p.text.replace("$", "")) for p in inventory.get_item_prices()]
    assert prices == sorted(prices, reverse=True), "Prices are not sorted high → low"

    # Sort by name A → Z
    inventory.sort_by("Name (A to Z)")
    names = [n.text for n in inventory.get_item_names()]
    assert names == sorted(names), "Names are not sorted A → Z"

    # Sort by name Z → A
    inventory.sort_by("Name (Z to A)")
    names = [n.text for n in inventory.get_item_names()]
    assert names == sorted(names, reverse=True), "Names are not sorted Z → A"
