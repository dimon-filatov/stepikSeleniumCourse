import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/wait1.html"
    browser.get(link)
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    time.sleep(20)
    browser.quit()
