from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    CHECKOUT_ITEMS = (By.CLASS_NAME, "cart_item")
    
    def get_items_count(self):
        return len(self.driver.find_elements(*self.CHECKOUT_ITEMS))
    def fill_info(self, first, last, zip_code):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.ZIP_CODE, zip_code)
        self.click(self.CONTINUE)

    def complete_order(self):
        self.click(self.FINISH)
