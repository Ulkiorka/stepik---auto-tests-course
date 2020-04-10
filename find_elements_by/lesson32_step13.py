from selenium import webdriver
import unittest
import time
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

fname = '.first_block .first'
lname = '.first_block .second'
email = '.first_block .third'
phone = '.second_block .first'
address = ' .second_block .second'
browser = webdriver.Chrome()


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser.get(link1)

        input1 = browser.find_element_by_css_selector(fname)
        input2 = browser.find_element_by_css_selector(lname)
        input3 = browser.find_element_by_css_selector(email)
        input4 = browser.find_element_by_css_selector(phone)
        input5 = browser.find_element_by_css_selector(address)

        input1.send_keys("Ivan")
        input2.send_keys("Ivanov")
        input3.send_keys("email@mail.com")
        input4.send_keys("8-800-2000-000")
        input5.send_keys("Moscow, Kremlin")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "uccessfully registered")

    def test_abs2(self):
        browser.get(link2)

        input1 = browser.find_element_by_css_selector(fname)
        input2 = browser.find_element_by_css_selector(lname)
        input3 = browser.find_element_by_css_selector(email)
        input4 = browser.find_element_by_css_selector(phone)
        input5 = browser.find_element_by_css_selector(address)

        input1.send_keys("Ivan")
        input2.send_keys("Ivanov")
        input3.send_keys("email@mail.com")
        input4.send_keys("8-800-2000-000")
        input5.send_keys("Moscow, Kremlin")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "uccessfully registered")

if __name__ == "__main__":
    unittest.main()