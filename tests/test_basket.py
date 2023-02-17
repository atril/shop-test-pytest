from typing import Any
from pageObjects.product_page import ProductPage
from pageObjects.products_list_page import ProductsListPage
from pageObjects.basket_page import BasketPage

class TestBasket:

    def test_add_product_to_basket_from_product_page(self, browser: Any, login_as_standard_user: None):
        self.browser = browser
        self.product_id = 1
        self.product_name = "Sauce Labs Bolt T-Shirt"
        self.product_page = ProductPage(self.browser)
        self.product_page.click_product_title_link(self.product_id)
        self.product_page.click_add_to_cart_button(self.product_name)
        self.product_page.click_shopping_cart_icon()
        self.basket_page = BasketPage(self.browser)
        self.cart_items_list = self.basket_page.get_cart_items_list()
        self.cart_item_name = self.basket_page.get_item_name(self.product_id)

        assert (len(self.cart_items_list)) == 1
        assert self.cart_item_name == self.product_name

    def test_add_product_to_basket_from_product_list(self, browser: Any, login_as_standard_user: None):
        self.browser = browser
        self.product_id = 4
        self.product_name = "Sauce Labs Backpack"
        self.products_list_page = ProductsListPage(self.browser)
        self.products_list_page.click_add_to_cart_button(self.product_name)
        self.products_list_page.click_shopping_cart_icon()
        self.basket_page = BasketPage(self.browser)
        self.cart_items_list = self.basket_page.get_cart_items_list()
        self.cart_item_name = self.basket_page.get_item_name(self.product_id)

        assert (len(self.cart_items_list)) == 1
        assert self.cart_item_name == self.product_name
