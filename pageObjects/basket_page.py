from selenium.webdriver.common.by import By

class BasketPage:
    __CART_ITEMS_LIST_CLASS = "cart_item"


    def __init__(self,driver) -> None:
        self.driver = driver

    def get_cart_items_list(self):
        element = self.driver.find_elements(By.CLASS_NAME, self.__CART_ITEMS_LIST_CLASS)
        return element

    def get_item_name(self, product_id) -> str:
        item_title_link = f"item_{product_id}_title_link"
        element = self.driver.find_element(By.ID, item_title_link)
        return element.text