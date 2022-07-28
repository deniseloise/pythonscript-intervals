#! python3
# intervals.py - Automatically files intervals every friday at 4:30 pm.

import time
import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from readtestdata import CsvRead

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://yondutech.intervalsonline.com/')
driver.maximize_window()

#Timestamp - Start
print('The script run at ' + str(datetime.datetime.now()))

#Login Scenario
#find username textfield and input valid username
driver.implicitly_wait(10)  # seconds
try:
    test_data = CsvRead('intervals_accounts.csv').read()
    #store username
    username_testdata = test_data['username']
    print("CHECK: Username is " + str(username_testdata))

    usernameElem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )
    usernameElem.send_keys(username_testdata)
except NoSuchElementException as exception:
    print('FAILED: Username Textfield Element Not Found.')

# Find username textfield and input valid password
driver.implicitly_wait(10)  # seconds
try:
    test_data = CsvRead('intervals_accounts.csv').read()
    #store password
    password_testdata = test_data['password']
    print("CHECK: Password is " + str(password_testdata))

    passwordElem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    passwordElem.send_keys(password_testdata)
except NoSuchElementException as exception:
    print('FAILED: Password Textfield Element Not Found.')

# Find Login Button and submit
driver.implicitly_wait(10)  # seconds
try:
    submitElem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'f_regular_submit')))
    submitElem.click()
except NoSuchElementException as exception:
    print('FAILED: Login/Submit Button Element not found.')

# TODO File Interval Per Day
# Click Time Tab; Navigate to Time Page
driver.implicitly_wait(10)  # seconds
try:
    timeElem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Time')))
    timeElem.click()
except NoSuchElementException as exception:
    print('FAILED: Time Button Element not found.')

 # Click Add Time Button
driver.implicitly_wait(10)  # seconds
try:
    addTimeElem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[value="Add Time"]')))
    addTimeElem.click()

except NoSuchElementException as exception:
    print('FAILED: Add Time Button Element not found.')

# Input Details on Form
# Input Hours in Time Textfield
driver.implicitly_wait(10)  # seconds
try:
    timeElem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'ftime'))
    )
    timeElem.send_keys('8')
except NoSuchElementException as exception:
    print('FAILED: Time Textfield Element Not Found.')

# Select Client
driver.implicitly_wait(10)  # seconds
try:
    clientElem = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'add_time_list_clients'))
    ))
    #select by select_by_visible_text() method
    clientElem.select_by_visible_text('Tech Council')
except NoSuchElementException as exception:
    print('FAILED: Client Dropdown Element Not Found.')

#Select Module
driver.implicitly_wait(10)  # seconds
try:
    ModuleElem = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'add_time_list_modules'))
    ))
    #select by select_by_visible_text() method
    ModuleElem.select_by_visible_text('Quality Assurance')
except NoSuchElementException as exception:
    print('FAILED: Module Dropdown Element Not Found.')


# Select Work Type
driver.implicitly_wait(10)  # seconds
try:
    WorkTypeElem = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'add_time_list_budget'))
    ))
    #select by select_by_visible_text() method
    WorkTypeElem.select_by_visible_text('Development')
except NoSuchElementException as exception:
    print('FAILED: Work Type Dropdown Element Not Found.')

# Click Billable Checkbox
driver.implicitly_wait(10)  # seconds
try:
    billableElem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'f_addtimeBillable')))
    billableElem.click()
except NoSuchElementException as exception:
    print('FAILED: Billable Checkbox Element not found.')

# Input Description of Work in Textarea
driver.implicitly_wait(10)  # seconds
try:
    test_data = CsvRead('intervals_accounts.csv').read()
    #store password
    taskdescription_testdata = test_data['description']
    print("CHECK: Task/s: " + str(taskdescription_testdata))

    descriptionElem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'f_addtimeDescription'))
    )
    descriptionElem.send_keys(taskdescription_testdata)
except NoSuchElementException as exception:
    print('FAILED: Textarea Element Not Found.')

# Click Submit Button
driver.implicitly_wait(10)  # seconds
try:
    SaveButtonElem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'addTimeSubmitButton')))
    SaveButtonElem.click()
    driver.implicitly_wait(60)  # seconds

    # Screenshot
    # Timestamp for screenshot file name
    timenow = "screenshot_intervals_" + \
        str(datetime.datetime.now().strftime("%Y_%b_%d-%I_%M_%S_%p"))
    print('The script run at ' + str(datetime.datetime.now()))
    # Save screenshot
    driver.save_screenshot(
        "C:/Users/Appletini/Documents/python_scripts/screenshots/" + timenow + ".png")

    # TODO Add logs to .txt file after every successful filing
    # Log date and time of filing
    file = open(
        r'C:\Users\Appletini\Documents\python_scripts\log_intervals.txt', 'a')

    file.write(f'{datetime.datetime.now()} - The script run successfully. \n')
except NoSuchElementException as exception:
    print('FAILED: Save Button Element not found.')

# Timestamp - Completed
print('The script completed at ' + str(datetime.datetime.now()))


# TODO Send results in email
