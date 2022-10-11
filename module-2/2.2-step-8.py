from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys('Petr')
    browser.find_element(By.NAME, 'lastname').send_keys('Petrov')
    browser.find_element(By.NAME, 'email').send_keys('petr@petrov.kz')
    directory = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(directory, 'petrov.txt')
    browser.find_element(By.NAME, 'file').send_keys(file_dir)
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(20)
    browser.quit()
