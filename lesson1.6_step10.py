from selenium import webdriver
import time
PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'

try:
    link = "http://suninjuly.github.io/registration1.html"

    driver = webdriver.Chrome(executable_path=PATH)
    driver.get(link)
    f_name = driver.find_element_by_css_selector(
        'div.form-group.first_class>input[placeholder="Input your first name"]')
    f_name.send_keys("Ivan")
    l_name = driver.find_element_by_css_selector(
        'div.form-group.second_class>input[placeholder="Input your last name"]')
    l_name.send_keys("Petrov")
    email = driver.find_element_by_css_selector(
        'div.form-group.third_class>input[placeholder="Input your email"]')
    email.send_keys('aaaa@gmail.com')
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = driver.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    driver.quit()