# cart_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    # Locator for the first item Remove button
    FIRST_ITEM_REMOVE_BUTTON = (By.CSS_SELECTOR, "button[data-test^='remove-']")

    def remove_first_item(self):
        """Click the Remove button for the first item in the cart."""
        self.click(self.FIRST_ITEM_REMOVE_BUTTON)
