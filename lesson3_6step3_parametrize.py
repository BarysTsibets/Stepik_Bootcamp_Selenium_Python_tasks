from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

import time
import math
import pytest
PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'



@pytest.fixture
def driver():
    print(f"Browser open...")
    driver = webdriver.Chrome(executable_path=PATH)
    yield driver
    driver.quit()
    print(f"Browser closed...")


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1'])
class TestAliens:
    def test_answer_solution(self, driver, link):
        driver.get(f"{link}")
        answer = math.log(int(time.time()))
        field = driver.find_element_by_id('ember89')
        field.send_keys(answer)
        driver.find_element_by_class_name('submit-submission').click()
        result = WebDriverWait(driver, 5).until(ES.text_to_be_present_in_element((By.ID, "ember114")))
        # result2 = driver.find_element_by_id("ember114")

        assert "Correct!" in result.text


