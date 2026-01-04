# pages/inventory_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_first_item_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.click(self.CART_ICON)
