"""   Task Robot-power: Attaching file
Open the page http://suninjuly.github.io/file_input.html
Fill in text fields: first name, last name, email
Upload file. The file must have a .txt extension.
Press the "Submit" button
"""
from selenium import webdriver
import os
import time
PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'
try:
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get("http://suninjuly.github.io/file_input.html")

    f_name = driver.find_element_by_name("firstname")
    f_name.send_keys("Kim")
    l_name = driver.find_element_by_name('lastname')
    l_name.send_keys("Kardashian")
    email = driver.find_element_by_name("email")
    email.send_keys("123@test.com")

    """Attaching file on the web page"""
    element = driver.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)

    submit = driver.find_element_by_class_name("btn.btn-primary")
    submit.click()
finally:
    time.sleep(8)
    driver.quit()
