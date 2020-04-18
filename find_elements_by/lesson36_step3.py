import pytest
from selenium import webdriver
import time
import math

def answer():
    return str(math.log(int(time.time())))

@pytest.fixture(scope = "function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(12)
    yield browser
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test(browser, number):
        link = f"https://stepik.org/lesson/{number}/step/1"
        browser.get(link)
        textarea = browser.find_element_by_css_selector(".textarea")
        textarea.send_keys(answer())
        button = browser.find_element_by_tag_name("button")
        button.click()
        phrase = browser.find_element_by_css_selector(".smart-hints__hint")
        assert phrase.text == "Correct!"