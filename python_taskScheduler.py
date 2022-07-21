#! python3
# python_taskScheduler.py - test task scheduler if it runs every 5 mins

import datetime

file = open(r'C:\Users\Appletini\Documents\python_scripts\task.txt', 'a')

file.write(f'{datetime.datetime.now()} - The script run \n')