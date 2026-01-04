# pages/cart_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def is_cart_empty(self):
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items) == 0

    def checkout_button_disabled(self):
        button = self.find_element(self.CHECKOUT_BUTTON)
        return not button.is_enabled()
