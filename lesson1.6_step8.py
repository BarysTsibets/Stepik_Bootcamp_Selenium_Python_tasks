from selenium import webdriver
import time
PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'
link = "http://suninjuly.github.io/find_xpath_form"

try:
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get(link)

    input1 = driver.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
    button = driver.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()