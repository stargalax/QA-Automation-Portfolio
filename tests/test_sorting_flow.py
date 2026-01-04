from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_sort_items(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.visit("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")

    # Sort items by price low to high
    inventory.sort_items("Price (low to high)")

    # Sort items by name Z to A
    inventory.sort_items("Name (Z to A)")
