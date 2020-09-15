"""        TASK 'Robot-power'
Open the page http://suninjuly.github.io/math.html.
Read the value for variable x.
Calculate a mathematical function of x 
Enter your answer in the text box.
Check the "I'm the robot" checkbox.
Select the radiobutton "Robots rule!"
Click on the Submit button.
"""
from selenium import webdriver
import time
import math

PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'
try:
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get("http://suninjuly.github.io/math.html")
    x_element = driver.find_element_by_css_selector(".nowrap#input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    input_field = driver.find_element_by_id("answer")
    input_field.send_keys(y)
    c_box = driver.find_element_by_css_selector('.form-check-label[for="robotCheckbox"]')
    c_box.click()
    radio = driver.find_element_by_css_selector('.form-check-label[for="robotsRule"]')
    radio.click()
    button = driver.find_element_by_class_name('btn.btn-default')
    button.click()
finally:
    time.sleep(5)
    driver.quit()

