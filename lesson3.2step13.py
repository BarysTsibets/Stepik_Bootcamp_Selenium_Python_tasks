from selenium import webdriver
import unittest
import time

PATH = r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe'


class TestTraining(unittest.TestCase):
    # def test_link1(self):
    #     link = "http://suninjuly.github.io/registration1.html"
    #     driver = webdriver.Chrome(executable_path=PATH)
    #     driver.get(link)
    #
    #     f_name = driver.find_element_by_css_selector(
    #         'div.form-group.first_class>input[placeholder="Input your first name"]')
    #     f_name.send_keys("Ivan")
    #     l_name = driver.find_element_by_css_selector(
    #         'div.form-group.second_class>input[placeholder="Input your last name"]')
    #     l_name.send_keys("Petrov")
    #     email = driver.find_element_by_css_selector(
    #         'div.form-group.third_class>input[placeholder="Input your email"]')
    #     email.send_keys('aaaa@gmail.com')
    #     button = driver.find_element_by_css_selector("button.btn")
    #     button.click()
    #     time.sleep(1)
    #     welcome_text = driver.find_element_by_tag_name("h1").text
    #     self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
    #                      f"{welcome_text} must be == 'Congratulations! You have successfully registered!'")
    #     time.sleep(2)
    #     driver.quit()

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        driver = webdriver.Chrome(executable_path=PATH)
        driver.get(link)

        f_name = driver.find_element_by_css_selector(
            'div.form-group.first_class>input[placeholder="Input your first name"]')
        f_name.send_keys("Ivan")
        l_name = driver.find_element_by_css_selector(
            'div.form-group.second_class>input[placeholder="Input your last name"]')
        l_name.send_keys("Petrov")
        email = driver.find_element_by_css_selector(
            'div.form-group.third_class>input[placeholder="Input your email"]')
        email.send_keys('aaaa@gmail.com')
        button = driver.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text = driver.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         f"{welcome_text} must be == 'Congratulations! You have successfully registered!'")
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    unittest.main()
