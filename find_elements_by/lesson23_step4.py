from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
def calc(number):
    return str(math.log(abs(12*math.sin(int(number)))))

def click_button():
    button = browser.find_element_by_tag_name("button")
    button.click()

try:
    browser = webdriver.Chrome()
    browser.get(link)
    click_button()

    confirm = browser.switch_to.alert
    confirm.accept()

    num_x = browser.find_element_by_id("input_value").text
    y = calc(num_x)
    answer = browser.find_element_by_id("answer").send_keys(y)
    click_button()

finally:
    time.sleep(7)
    browser.quit()
