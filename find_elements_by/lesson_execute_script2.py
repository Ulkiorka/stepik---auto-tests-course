from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    text_area = browser.find_element_by_id("answer")
    text_area.send_keys(y)
    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()
    button = browser.find_element_by_tag_name('button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()
    button.click()

finally:
    time.sleep(7)
    browser.quit()