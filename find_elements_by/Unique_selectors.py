from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fname   = '.first_block .first'
    lname   = '.first_block .second'
    email   = '.first_block .third'
    phone   = '.second_block .first'
    address =' .second_block .second'

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

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()