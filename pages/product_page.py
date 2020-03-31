from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
	def add_product_to_basket(self):
		button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
		button_add.click()

	def shoold_be_choosen_product(self):
		self.should_be_choosen_product_name()
		self.should_be_choosen_product_price()

	def should_be_choosen_product_name(self):
		my_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		product_in_basket = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
		assert my_product == product_in_basket, f"Product names {my_product} and {product_in_basket} don't match"

	def should_be_choosen_product_price(self):
		my_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		price_in_basket = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
		assert my_price == price_in_basket, f"Product prices {my_price} and {price_in_basket} don't match"
