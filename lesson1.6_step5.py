from selenium import webdriver
import math
import time

PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'
URL = str(math.ceil(math.pow(math.pi, math.e)*10000))
try:
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get("http://suninjuly.github.io/find_link_text")
    link = driver.find_element_by_link_text(URL)
    link.click()
    input1 = driver.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # copy answer for this task
    time.sleep(10)
    # close browser
    driver.quit()



