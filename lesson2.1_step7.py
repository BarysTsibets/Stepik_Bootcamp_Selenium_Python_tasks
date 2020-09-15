"""      TASK 'Robot-power' --- get_attribute
Open the page http://suninjuly.github.io/get_attribute.html.
Find a picture element on it, which is an image of a treasure chest.
Get the valuex attribute value from this element, which is the x value for the task.
Calculate a mathematical function of x (the function itself remains unchanged).
Enter your answer in the text box.
Check the "I'm the robot" checkbox.
Select the radiobutton "Robots rule!"
Click on the "Submit" button."""

from selenium import webdriver
import time
import math

PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'
try:
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get("http://suninjuly.github.io/get_attribute.html")
    x = driver.find_element_by_id('treasure').get_attribute('valuex')

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    input_field = driver.find_element_by_id("answer")
    input_field.send_keys(y)
    c_box = driver.find_element_by_id('robotCheckbox')
    c_box.click()
    radio = driver.find_element_by_id('robotsRule')
    radio.click()
    button = driver.find_element_by_class_name('btn.btn-default')
    button.click()
finally:
    time.sleep(5)
    driver.quit()