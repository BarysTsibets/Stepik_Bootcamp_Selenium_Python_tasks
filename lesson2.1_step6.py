from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"
PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'
try:
    browser = webdriver.Chrome(executable_path=PATH)
    browser.get(link)

    # check the value of the checked attribute of people_radio
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    # check the value of the checked attribute of robots_radio
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots_radio: ", robots_checked)
    assert robots_checked is None

    # check the value of the disabled attribute of the Submit button
    button = browser.find_element_by_css_selector('.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None

    # check the value of the disabled attribute of the Submit button after a timeout
    time.sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit after 10sec: ", button_disabled)
    assert button_disabled is not None

finally:
    browser.quit()
