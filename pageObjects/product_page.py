from selenium.webdriver.common.by import By

from pageObjects.navigation_bar_page import NavigationBarPage

class ProductPage(NavigationBarPage):

    def click_product_title_link(self, product_id):
        item_title = f"item_{product_id}_title_link"
        element = self.driver.find_element(By.ID, item_title)
        element.click()

    def click_add_to_cart_button(self, product_name):
        product_name = product_name.replace(' ', '-').lower()
        add_to_cart_button = f"add-to-cart-{product_name}"
        element = self.driver.find_element(By.ID, add_to_cart_button)
        element.click()