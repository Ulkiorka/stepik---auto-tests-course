from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    sum = str(int(num1) + int(num2))

    browser.find_element_by_id("dropdown").click()
    browser.find_element_by_css_selector("[value='" +sum+ "']").click()

    #select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_value(sum)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
