from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)


    name = browser.find_element_by_css_selector("[name='firstname']")
    name.send_keys("name")

    lastname = browser.find_element_by_css_selector("[name='lastname']")
    lastname.send_keys("surname")

    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("email@email.email")

    current_dir = os.path.abspath(os.path.dirname("/Users/alexey/"))
    file_path = os.path.join(current_dir, 'text.txt')

    file_button = browser.find_element_by_id("file")
    file_button.send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn-primary")
    button.click()
finally:
    time.sleep(7)
    browser.quit()

