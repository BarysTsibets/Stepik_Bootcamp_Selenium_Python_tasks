from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"
PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'

# Example with classmethod - fixture(Browser open just once for 2 tests)
class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome(executable_path=PATH)

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")
        print(1)

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print(2)

# Example withOUT classmethod - fixture(Browser open twice for 2 tests)
class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome(executable_path=PATH)


    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")
        print(3)

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print(4)
        #end
