from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    browser.switch_to.window(browser.window_handles[1])
    x1 = browser.find_element(By.ID, "input_value")
    x = x1.text
    y = calc(x)
    r = browser.find_element(By.ID, "answer")
    r.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(4)
    browser.quit()



import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("https://suninjuly.github.io/cats.html")

try:

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    time.sleep(4)
    browser.quit()