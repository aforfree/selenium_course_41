from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_ADDED_TO_BASKET_MESSAGE = (By.XPATH, "//div[@id='messages']//div[contains(@class, 'alertinner') and contains(string(), 'has been added to your basket.')]")
    NAME_OF_PRODUCT_ADDED_TO_BASKET_MESSAGE = (By.XPATH, "//div[@id='messages']//div[contains(@class, 'alertinner') and contains(string(), 'has been added to your basket.')]/strong")
    PRODUCT_NAME= (By.XPATH, "//article[contains(@class, 'product_page')]//div[contains(@class, 'product_main')]/h1")
    BASKET_TOTAL_MESSAGE = (By.XPATH, "//div[@id='messages']//div[contains(@class, 'alertinner') and contains(string(), 'Your basket total is now')]") # text = "Your basket total is now" <strong>{busket_price}</strong>
    BASKET_TOTAL_MESSAGE_AMOUNT = (By.XPATH, "//div[@id='messages']//div[contains(@class, 'alertinner') and contains(string(), 'Your basket total is now')]/p/strong") # <p> text = "Your basket total is now" <strong>{busket_price}</strong>
    PRODUCT_PRICE = (By.XPATH, "//article[@class='product_page']//div[contains(@class, 'product_main')]/p[contains(@class, 'price_color')]") # article.product_page > p.price_color