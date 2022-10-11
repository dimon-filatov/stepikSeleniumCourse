from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select

try:
    # link = 'http://suninjuly.github.io/selects1.html'
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.ID, 'num1').text
    b = browser.find_element(By.ID, 'num2').text
    result = int(a) + int(b)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(result))

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
