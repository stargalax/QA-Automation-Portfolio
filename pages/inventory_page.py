from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    #FIRST_ITEM_ADD_BUTTON = (By.CSS_SELECTOR, ".inventory_item:first-child button")
    FIRST_ITEM_ADD_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")

    CART_ICON = (By.ID, "shopping_cart_container")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def add_first_item_to_cart(self):
        #self.click(self.FIRST_ITEM_ADD_BUTTON)
        buttons = self.driver.find_elements(*self.FIRST_ITEM_ADD_BUTTON)
        if buttons:
            buttons[0].click()

    def go_to_cart(self):
        self.click(self.CART_ICON)
    
    def sort_items(self, option_text):
        from selenium.webdriver.support.ui import Select
        select = Select(self.wait.until(lambda d: d.find_element(*self.SORT_DROPDOWN)))
        select.select_by_visible_text(option_text)

    