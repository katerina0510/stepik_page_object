from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
	def should_be_basket_empty(self):
		self.should_be_text_basket_is_empty()
		self.should_not_be_products_in_basket()

	def should_be_basket_url(self):
		assert "basket" in self.browser.current_url, "URL doesn't contain 'basket'"

	def should_be_text_basket_is_empty(self):
		assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT) \
		    	and "Your basket is empty" in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text, \
		    		"No english text that basket is empty"

	def should_not_be_products_in_basket(self):
		assert self.is_not_element_presented(*BasketPageLocators.PRODUCTS_IN_BASKET), "Basket is not empty"
