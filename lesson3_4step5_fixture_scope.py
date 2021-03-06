import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"
PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'


@pytest.fixture(scope="class")
# Browser will be open/closed  1 time for class
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=PATH)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # here we drop fixture as argument
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")