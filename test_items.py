# import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_check_button(browser):
    browser.get(link)
    button_add_to_cart = len(browser.find_elements_by_xpath("//form[@id='add_to_basket_form']//button"))
    assert button_add_to_cart > 0, "Button does not exist"
    # time.sleep(10)