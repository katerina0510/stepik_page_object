from .pages.product_page import ProductPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
	browser.implicitly_wait(10)
	page = ProductPage(browser, link)
	page.open()
	page.add_product_to_basket()
	page.solve_quiz_and_get_code()
	page.shoold_be_choosen_product()
	