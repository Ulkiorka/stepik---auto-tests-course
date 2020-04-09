import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    num_x = browser.find_element_by_id("input_value").text
    y = calc(num_x)
    answer = browser.find_element_by_id("answer").send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
