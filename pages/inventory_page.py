# pages/inventory_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class InventoryPage(BasePage):
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".inventory_item button")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def go_to_cart(self):
        #self.click((By.CLASS_NAME, "shopping_cart_link"))
        self.click(self.CART_LINK)


    def add_first_item_to_cart(self):
        #self.click((By.CSS_SELECTOR, ".inventory_item:first-child button"))
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if buttons:
            buttons[0].click()
    
    
    def sort_items(self, sort_option):
        dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(sort_option)
        
    def sort_by(self, option_text):
        dropdown = Select(self.find_element(self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(option_text)

    def get_item_prices(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    def get_item_names(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
