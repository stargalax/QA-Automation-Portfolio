from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, ".cart_item button")
    CHECKOUT_BUTTON = (By.ID, "checkout")  # <-- Add this

    def is_cart_empty(self):
        return len(self.driver.find_elements(*self.CART_ITEMS)) == 0

    def checkout_button_disabled(self):
        button = self.driver.find_element(*self.CHECKOUT_BUTTON)
        return not button.is_enabled()

    def remove_first_item(self):
        remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
        if remove_buttons:
            remove_buttons[0].click()
