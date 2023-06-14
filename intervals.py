#! python3
# intervals.py - Automatically file intervals every day and submits every Friday

import time
import datetime
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from readtestdata import CsvRead
from sendEmail import *
from decouple import config

def fileIntervals():

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    driver.get('https://yondutech.intervalsonline.com/')
    driver.maximize_window()

    #Timestamp - Start
    print('The script run at ' + str(datetime.datetime.now()))

    #Login Scenario
    #find username textfield and input valid username
    driver.implicitly_wait(10)  # seconds
    try:
        #test_data = CsvRead('intervals_accounts.csv').read()
        #store username
        #username_testdata = test_data['username']

        #Get username from .env file
        username_testdata = config('username_intervals', default='')

        print("CHECK: Username is " + str(username_testdata))

        usernameElem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )
        usernameElem.send_keys(username_testdata)
    except NoSuchElementException as exception:
        print('An Error Occurred: Username Textfield Element Not Found.', type(exception).__name__, "-", exception)
        

    # Find password textfield and input valid password
    driver.implicitly_wait(10)  # seconds
    try:
        #test_data = CsvRead('intervals_accounts.csv').read()
        #store password
        #password_testdata = test_data['password']
        
        #Get password from .env file
        password_testdata = config('password_intervals', default='')
        
        print("CHECK: Password is " + str(password_testdata))

        passwordElem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )
        passwordElem.send_keys(password_testdata)
    except NoSuchElementException as exception:
        print('An Error Occured: Password Textfield Element Not Found.', type(exception).__name__, "-", exception)

    # Find Login Button and submit
    driver.implicitly_wait(10)  # seconds
    try:
        submitElem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'f_regular_submit')))
        submitElem.click()
    except NoSuchElementException as exception:
        print('An Error Occured: Login/Submit Button Element not found.', type(exception).__name__, "-", exception)

    # TODO File Interval Per Day
    # Click Time Tab; Navigate to Time Page
    driver.implicitly_wait(10)  # seconds
    try:
        timeElem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Time')))
        timeElem.click()
    except NoSuchElementException as exception:
        print('An Error Occured: Time Button Element not found.', type(exception).__name__, "-", exception)

    # Click Add Time Button
    driver.implicitly_wait(10)  # seconds
    try:
        addTimeElem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[value="Add Time"]')))
        addTimeElem.click()

    except NoSuchElementException as exception:
        print('An Error Occured: Add Time Button Element not found.', type(exception).__name__, "-", exception)

    # Input Details on Form
    # Input Hours in Time Textfield
    driver.implicitly_wait(10)  # seconds
    try:
        timeElem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'ftime'))
        )
        timeElem.send_keys('8')
    except NoSuchElementException as exception:
        print('An Error Occured: Time Textfield Element Not Found.', type(exception).__name__, "-", exception)

    # Select Client
    driver.implicitly_wait(10)  # seconds
    try:
        clientElem = Select(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'add_time_list_clients'))
        ))
        #select by select_by_visible_text() method
        clientElem.select_by_visible_text('MTS')
    except NoSuchElementException as exception:
        print('An Error Occured: Client Dropdown Element Not Found.', type(exception).__name__, "-", exception)

    #Select Project
    driver.implicitly_wait(10)  # seconds
    try:
        ModuleElem = Select(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'add_time_list_projects'))
        ))
        #select by select_by_visible_text() method
        ModuleElem.select_by_visible_text('MTS_GoRaffle')
    except NoSuchElementException as exception:
        print('An Error Occured: Module Dropdown Element Not Found.', type(exception).__name__, "-", exception)

    #Select Module
    driver.implicitly_wait(10)  # seconds
    try:
        ModuleElem = Select(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'add_time_list_modules'))
        ))
        #select by select_by_visible_text() method
        ModuleElem.select_by_visible_text('Quality Assurance')
    except NoSuchElementException as exception:
        print('An Error Occured: Module Dropdown Element Not Found.', type(exception).__name__, "-", exception)


    # Select Work Type
    driver.implicitly_wait(10)  # seconds
    try:
        WorkTypeElem = Select(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'add_time_list_budget'))
        ))
        #select by select_by_visible_text() method
        WorkTypeElem.select_by_visible_text('Development')
    except NoSuchElementException as exception:
        print('An Error Occured: Work Type Dropdown Element Not Found.', type(exception).__name__, "-", exception)

    # Input Description of Work in Textarea
    driver.implicitly_wait(10)  # seconds
    try:
        #test_data = CsvRead('intervals_accounts.csv').read()
        #store password
        #taskdescription_testdata = test_data['description']

        #Get task description from .env file
        taskdescription_testdata = config('description', default='')

        print("CHECK: Task/s: " + str(taskdescription_testdata))

        descriptionElem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'f_addtimeDescription'))
        )
        descriptionElem.send_keys(taskdescription_testdata)
    except NoSuchElementException as exception:
        print('An Error Occured: Textarea Element Not Found.', type(exception).__name__, "-", exception)

    # Click Save Button
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

        # Add logs to .txt file after every successful filing
        # Log date and time of filing
        file = open(
            r'C:\Users\Appletini\Documents\python_scripts\log_intervals.txt', 'a')

        file.write(f'{datetime.datetime.now()} - The script run successfully. \n')

        # Send results in email
        # call sendIntervalsEmail function from sendEmail Module
        sendIntervalsEmail()

    except NoSuchElementException as exception:
        print('An Error Occured: Save Button Element not found.', type(exception).__name__, "-", exception)

    # Timestamp - Completed
    print('The script completed at ' + str(datetime.datetime.now()))
    