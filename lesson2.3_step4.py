from selenium import webdriver
import math
import time

PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'
try:
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get('http://suninjuly.github.io/alert_accept.html')
    button = driver.find_element_by_class_name('btn.btn-primary')
    button.click()
    confirm = driver.switch_to.alert
    confirm.accept()
    x = driver.find_element_by_id('input_value').text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    result = driver.find_element_by_id('answer')
    result.send_keys(y)
    driver.find_element_by_class_name('btn.btn-primary').click()
finally:
    time.sleep(8)
    driver.quit()


