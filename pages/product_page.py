from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click() 
        self.solve_quiz_and_get_code()
        #import time
        #time.sleep(3000)

        self.should_be_product_added_to_basket_message()
        self.should_be_product_added_to_basket_message_has_same_product_name()
        self.should_be_basket_total_message()
        self.should_be_basket_total_equal_to_product_price()


    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "'Add to basket' button is not presented"

    def should_be_product_added_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE), "'Product added to basket' message is not presented"

    def should_be_product_added_to_basket_message_has_same_product_name(self):
        name_of_product_added_to_basket_message = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_ADDED_TO_BASKET_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert name_of_product_added_to_basket_message == product_name, "'Product in added to basket message' has different name"

    def should_be_basket_total_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), "'Basket price' message is not presented"

    def should_be_basket_total_equal_to_product_price(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE_AMOUNT).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert basket_total == product_price, "Basket total is not equal to product price"