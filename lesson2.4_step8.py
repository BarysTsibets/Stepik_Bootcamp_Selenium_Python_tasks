"""           Expected Conditions:
    'WebDriverWait(driver, 12).until(Ec.text_to_be_present_in_element((By.ID, "price"), "100"))'

Open the page http://suninjuly.github.io/explicit_wait2.html
Wait until the price of the house decreases to $ 100 (the wait must be set at least 12 seconds)
Click on the "Book" button
Solve a math problem we already know (use the previously written code) and submit the solution
To determine when the rental price drops to $ 100, use the text_to_be_present_in_element method from the expected_conditions library.
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
import math
import time

PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=PATH)
try:
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    button = driver.find_element_by_id('book')

    # Expected condition : price must be 100$
    PRICE = WebDriverWait(driver, 12).until(Ec.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()

    # SCROLL PAGE DOWN
    input_field = driver.find_element_by_id('answer')
    driver.execute_script("return arguments[0].scrollIntoView(true);", input_field)
    # Find argument on the page for function calc()
    x = driver.find_element_by_id("input_value").text

    def calc(num):
        return str(math.log(abs(12 * math.sin(int(x)))))


    result = calc(x)
    input_field.send_keys(result)
    button = driver.find_element_by_id('solve')
    button.click()
    # Finnaly block
finally:
    time.sleep(8)
    driver.quit()

