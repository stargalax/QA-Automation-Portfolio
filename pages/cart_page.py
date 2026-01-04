from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "a.button-medium[title='Proceed to checkout']")
    CART_SUMMARY = (By.ID, "cart_summary")

    def proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT)

    def is_product_in_cart(self):
        return "Product" in self.get_text(self.CART_SUMMARY)
