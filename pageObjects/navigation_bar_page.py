from selenium.webdriver.common.by import By

class NavigationBarPage:
    __SHOPPING_CART_CONTAINER_ID = "shopping_cart_container"

    def __init__(self,driver) -> None:
        self.driver = driver

    def click_shopping_cart_icon(self):
        element = self.driver.find_element(By.ID, self.__SHOPPING_CART_CONTAINER_ID)
        element.click()