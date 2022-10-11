from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x = int(browser.find_element(By.ID, 'input_value').text)
    calculate = math.log(abs(12 * math.sin(x)))
    browser.find_element(By.ID, 'answer').send_keys(calculate)
    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    button.click()

finally:
    time.sleep(20)
    browser.quit()
