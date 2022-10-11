import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.window(browser.window_handles[1])
    calculate = math.log(abs(12 * math.sin(int(browser.find_element(By.ID, 'input_value').text))))
    browser.find_element(By.ID, 'answer').send_keys(calculate)
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(20)
    browser.quit()
