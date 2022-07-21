#! python3
# screenshotsample.py - takes screenshot; saves it in directory then opens it.

import time
import datetime
import os
from selenium import webdriver
from PIL import Image

# Here Chrome  will be used
driver = webdriver.Chrome()

# URL of website
url = "https://yondutech.intervalsonline.com/"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Opening the website
driver.get(url)
driver.maximize_window()

#Timestamp for screenshot file name
timenow = "screenshot_intervals_" + str(datetime.datetime.now().strftime("%Y_%b_%d-%I_%M_%S_%p"))
print('The script run at ' + str(datetime.datetime.now()))

driver.save_screenshot("C:/Users/Appletini/Documents/python_scripts/screenshots/" + timenow + ".png")
 
# Loading the image
image = Image.open("C:/Users/Appletini/Documents/python_scripts/screenshots/" + timenow + ".png")
 
# Showing the image
image.show()