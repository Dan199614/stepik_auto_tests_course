from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math

site = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(site)
    rezult = sum([int(browser.find_element(By.ID, "num1").text),int(browser.find_element(By.ID, "num2").text)])
    Select(browser.find_element(By.ID, "dropdown")).select_by_value(str(rezult))
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
