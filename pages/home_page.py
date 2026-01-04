from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SIGN_IN = (By.CLASS_NAME, "login")
    SEARCH_BOX = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.NAME, "submit_search")

    def go_to_login(self):
        self.click(self.SIGN_IN)

    def search_product(self, product_name):
        self.type(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)
