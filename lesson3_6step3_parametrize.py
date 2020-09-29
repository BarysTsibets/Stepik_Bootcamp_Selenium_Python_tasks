from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import time
import math
import pytest


@pytest.fixture
def driver():
    print(f"Browser open...")
    driver = webdriver.Chrome(
        executable_path=r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe')
    yield driver
    driver.quit()
    print(f"Browser closed...")


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1' ])
class TestAliens:
    def test_answer_solution(self, driver, link):
        # Running Chrome
        driver.get(f"{link}")

        # Explicit waiting until the page will be completely loaded
        open_lag = WebDriverWait(driver, 5).until(ES.element_to_be_clickable((By.CSS_SELECTOR,
        '[class="textarea string-quiz__textarea ember-text-area ember-view"]')))

        # Calculating answer
        answer = math.log(int(time.time()+1))
        field = driver.find_element_by_css_selector(
            '[class="textarea string-quiz__textarea ember-text-area ember-view"]')
        field.send_keys(str(answer))
        driver.find_element_by_class_name('submit-submission').click()

        # Explicit waiting until result be completely loaded
        result = WebDriverWait(driver, 5).until(ES.visibility_of_element_located((By.CSS_SELECTOR, '[class="smart-hints__hint"]'),))
        assert "Correct!" in result.text


