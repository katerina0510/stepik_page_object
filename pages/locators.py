from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")

class ProductPageLocators():
	BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
	ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) strong")
	ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) strong")