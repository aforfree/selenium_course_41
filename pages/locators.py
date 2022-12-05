from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, \
        "button.btn-add-to-basket")
    PRODUCT_ADDED_TO_BASKET_MESSAGE = (By.XPATH, \
        "//div[@id='messages']//div[contains(@class, 'alert-success') and position()=1]//div[contains(@class, 'alertinner')]") 
    NAME_OF_PRODUCT_ADDED_TO_BASKET_MESSAGE = (By.XPATH, \
        "//div[@id='messages']//div[contains(@class, 'alert-success') and position()=1]//div[contains(@class, 'alertinner')]/strong")
    PRODUCT_NAME= (By.XPATH, \
        "//article[contains(@class, 'product_page')]//div[contains(@class, 'product_main')]/h1")
    BASKET_TOTAL_MESSAGE = (By.XPATH, \
        "//div[@id='messages']//div[contains(@class, 'alert-info')]//div[contains(@class, 'alertinner')]")
    BASKET_TOTAL_MESSAGE_AMOUNT = (By.XPATH, \
        "//div[@id='messages']//div[contains(@class, 'alert-info')]//div[contains(@class, 'alertinner')]/p/strong") 
    PRODUCT_PRICE = (By.XPATH, \
        "//article[@class='product_page']//div[contains(@class, 'product_main')]/p[contains(@class, 'price_color')]") 

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//div[contains(@class, 'page_inner')]//a[contains(@class, 'btn') and contains(@href, 'basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.XPATH, "//div[contains(@id, 'content_inner')]//div[contains(@class, 'basket-items')]")
    EMPTY_BASKET_TEXT = (By.XPATH, "//div[contains(@id, 'content_inner')]//p") 
    