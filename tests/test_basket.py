from typing import Any
from pageObjects.product_page import ProductPage
from pageObjects.products_list_page import ProductsListPage
from pageObjects.basket_page import BasketPage

class TestBasket:

    def test_add_product_to_basket_from_product_page(self, browser: Any, login_as_standard_user: None):
        product_id = 1
        product_name = "Sauce Labs Bolt T-Shirt"
        product_page = ProductPage(browser)
        product_page.click_product_title_link(product_id)
        product_page.click_add_to_cart_button(product_name)
        product_page.click_shopping_cart_icon()
        basket_page = BasketPage(browser)
        cart_items_list = basket_page.get_cart_items_list()
        cart_item_name = basket_page.get_item_name(product_id)

        assert (len(cart_items_list)) == 1
        assert cart_item_name == product_name

    def test_add_product_to_basket_from_product_list(self, browser: Any, login_as_standard_user: None):
        product_id = 4
        product_name = "Sauce Labs Backpack"
        products_list_page = ProductsListPage(browser)
        products_list_page.click_add_to_cart_button(product_name)
        products_list_page.click_shopping_cart_icon()
        basket_page = BasketPage(browser)
        cart_items_list = basket_page.get_cart_items_list()
        cart_item_name = basket_page.get_item_name(product_id)

        assert (len(cart_items_list)) == 1
        assert cart_item_name == product_name
