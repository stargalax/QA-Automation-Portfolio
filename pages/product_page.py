from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".product-container")
    ADD_TO_CART = (By.CSS_SELECTOR, "a.button.ajax_add_to_cart_button")

    def add_first_product_to_cart(self):
        self.click(self.FIRST_PRODUCT)
        self.click(self.ADD_TO_CART)
