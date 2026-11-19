from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math, os

site = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(site)
    input1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']:required")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']:required")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']:required")
    input3.send_keys("exaple@mail.ru")
    input4 = browser.find_element(By.CSS_SELECTOR, "input[name='file']:required")
    input4.send_keys(os.path.join(os.getcwd(), "test.txt"))
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
