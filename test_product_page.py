from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link_part', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, link_part):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_part}"
	browser.implicitly_wait(10)
	page = ProductPage(browser, link)
	page.open()
	page.add_product_to_basket()
	page.solve_quiz_and_get_code()
	page.shoold_be_choosen_product()
