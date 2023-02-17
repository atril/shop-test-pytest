from selenium.webdriver.common.by import By

from pageObjects.navigation_bar_page import NavigationBarPage

class ProductsListPage(NavigationBarPage):

    def click_add_to_cart_button(self, product_name):
        product_name = product_name.replace(' ', '-').lower()
        add_to_cart_button = f"add-to-cart-{product_name}"
        element = self.driver.find_element(By.ID, add_to_cart_button)
        element.click()