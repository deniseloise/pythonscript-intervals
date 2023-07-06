#! python3
# file_multiple_intervals.py - Automatically file intervals every day and submits every Friday

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
import intervals_functions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Intervals:
    #TODO Check if driver can be used in intervals_functions.py methods
    # init method or constructor
    def __init__(self, driver):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=self.options)
        self.wait = WebDriverWait(driver, 10)

    def file_multiple_entries():
        #Call Intervals Login Function from intervals_functions module
        intervals_functions.intervals_login()
        
        #Hover and click Add Multiple Time Entries Header tab link
        intervals_functions.hover_over_link_text_element_then_click('Time','Add multiple time entries')

        #Click and Select Client/Project dropdown list
        intervals_functions.send_keys_dropdown('//*[@id="f_time[0][projectid]-dropt"]/div[1]','//*[@id="f_time[0][projectid]-dropt"]/div[2]/div[3]/input','MTS_GoRaffle')

        #Click and Select Module dropdown list
        intervals_functions.send_keys_dropdown('//*[@id="f_time[0][moduleid]-dropt"]/div[1]','//*[@id="f_time[0][moduleid]-dropt"]/div[2]/div[3]/input','Quality Assurance')

        #Click and Select Work Type dropdown list
        intervals_functions.send_keys_dropdown('//*[@id="f_time[0][worktypeid]-dropt"]/div[1]','//*[@id="f_time[0][worktypeid]-dropt"]/div[2]/div[3]/input','Development')

        #Click Time Box and Copy hours (4 times)
        intervals_functions.copy_hours('input.has-width.required.input.input-time','8','//*[@id="timeTable"]/tbody/tr[1]/td[5]/div/div[2]/textarea','Startup + MTS Development Tasks')
        
        #Click Submit Time Entries
        intervals_functions.scroll_to_element_click('button.btn.save.mr10')

        #Click Submit For Approval
        intervals_functions.submit_for_approval('//div[@id="time_index_buttons_top"]/input[1]')

Intervals.file_multiple_entries()
