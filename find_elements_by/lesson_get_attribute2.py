from  selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    image = browser.find_element_by_id("treasure")
    x = image.get_attribute("valuex")
    y = calc(x)

    textarea = browser.find_element_by_id("answer")
    textarea.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_radio.click()

    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
