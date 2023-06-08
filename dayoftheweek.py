#! python3
# dayoftheweek.py - check what day and execute intervals based on what day it is.

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from readtestdata import CsvRead
import intervals

# If today is Friday (1 = Mon, 2 = Tue, 3 = Wen ...)
if datetime.today().isoweekday() == 5:
    print("Yes, Today is Friday")
    intervals.fileIntervals()
else:
    print("Today is:", datetime.today().strftime('%A'))
    intervals.fileIntervals()
