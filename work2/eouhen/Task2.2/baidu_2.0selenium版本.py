# Author : AnnieHathaway
import calendar

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import requests

chrome_service = ChromeService(executable_path='D:/ChromeDriver/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://baike.baidu.com/calendar/")
wait = WebDriverWait(driver, 10)
ele = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="calendar"]/ul[2]/li[4]')))
ActionChains(driver).move_to_element(ele).perform()
ele.click()
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'selected')))
a = element.find_element(By.CLASS_NAME, "abstract")
abstract_text = a.text

ele = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'event')))
b = ele.find_element(By.CLASS_NAME, "event_cnt")
detail = b.text
# 打印结果
print("摘要:", abstract_text)
print(detail)

"""events = driver.find_elements(By.XPATH, '//*[@id="calendar"]/ul[2]/li')
print(events)"""

"""# 获取日期文本
date_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'day')))
date = date_element.text

# 获取图片的URL
img_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
img_url = img_element.get_attribute("src")

# 获取摘要文本
abstract_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "abstract")))
abstract_text = abstract_element.text"""




