from selenium import webdriver
import pytest


PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=PATH)
    yield browser
    print("\nquit browser..")
    browser.quit()