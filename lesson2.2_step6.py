""" Task Robot-power: javaScript scroll
Open the page http://SunInJuly.github.io/execute_script.html.
Read the value for variable x.
Calculate a mathematical function of x.
Scroll down the page.
Enter your answer in the text box.
Select the checkbox "I'm the robot".
Toggle the radiobutton "Robots rule!"
Click on the "Submit" button.
"""

from selenium import webdriver
import time
import math

PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'
try:
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get("http://SunInJuly.github.io/execute_script.html")
    x = driver.find_element_by_id('input_value').text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    input_field = driver.find_element_by_id("answer")

    """Scrolling down , because element hidden by another element on the page"""
    driver.execute_script("return arguments[0].scrollIntoView(true);", input_field)

    input_field.send_keys(y)
    c_box = driver.find_element_by_id('robotCheckbox')
    c_box.click()
    radio = driver.find_element_by_id('robotsRule')
    radio.click()
    button = driver.find_element_by_class_name('btn.btn-primary')
    button.click()
finally:
    time.sleep(5)
    driver.quit()



