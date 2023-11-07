import io
import time
import os
import numpy as np
from PIL import Image
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://movie.douban.com/top250")

if not (os.path.exists('./screenshots_folder')):
    os.mkdir('./screenshots_folder')
screenshots_folder = './screenshots_folder'
page_height = driver.execute_script('return document.body.scrollHeight')
window_height = driver.execute_script('return window.screen.height')
window_width = driver.execute_script('return window.screen.width')

print(page_height, window_height)

screenshots_numbers = page_height // window_height - 1
driver.set_window_size(window_width, window_height)

# 创建一个列表来存储每个截图的NumPy数组
screenshot_arrays = []

for i in range(screenshots_numbers):
    driver.execute_script("window.scrollBy(0, {})".format(i * window_height))
    time.sleep(0.5)

    # 获取截图并将其转换为NumPy数组
    screenshot = driver.get_screenshot_as_png()
    screenshot_image = Image.open(io.BytesIO(screenshot))
    screenshot_array = np.array(screenshot_image)

    screenshot_arrays.append(screenshot_array)

# 将多个截图的NumPy数组拼接成一个长截图的NumPy数组
combined_image_array = np.concatenate(screenshot_arrays, axis=0)

# 将NumPy数组转换为Pillow的Image对象
combined_image = Image.fromarray(combined_image_array)

combined_image.save('./combined_screenshot.png')

driver.quit()
