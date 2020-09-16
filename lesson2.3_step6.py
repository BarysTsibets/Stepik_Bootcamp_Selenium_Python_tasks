"""   topic:   Switch_to    window_handles[1]

Open the page http://suninjuly.github.io/redirect_accept.html
Press the button
Switch to new tab
Pass the captcha for the robot and get the answer number"""
from selenium import webdriver
import time
import math

PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'
try:
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get('http://suninjuly.github.io/redirect_accept.html')
    button = driver.find_element_by_class_name('trollface.btn.btn-primary')
    button.click()
    # Switch to the new window
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    x = driver.find_element_by_id('input_value').text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    result = driver.find_element_by_id('answer')
    result.send_keys(y)
    driver.find_element_by_class_name('btn.btn-primary').click()
finally:
    time.sleep(10)
    driver.quit()

