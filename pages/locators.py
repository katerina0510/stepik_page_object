from selenium.webdriver.common.by import By

class BasePageLocators():
	BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn")
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
	PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
		
class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
	REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
	REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
	ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) strong")
	ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) strong")

	BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")

	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
	
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) strong")

