"""   Task:
Open the page http://suninjuly.github.io/selects1.html
Calculate the sum of the given numbers
Select in the drop-down list a value equal to the calculated amount
Press the "Submit" button"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'
link1 = 'http://suninjuly.github.io/selects1.html'
link2 = 'http://suninjuly.github.io/selects2.html'

try:
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get(link2)
    number1 = driver.find_element_by_css_selector('.nowrap#num1').text
    number2 = driver.find_element_by_css_selector('.nowrap#num2').text
    result = int(number1) + int(number2)

    select = Select(driver.find_element_by_id('dropdown'))
    select.select_by_value(f"{result}")

    driver.find_element_by_class_name('btn.btn-default').click()

finally:
    time.sleep(10)
    driver.quit()





