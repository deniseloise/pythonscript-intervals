from selenium.common.exceptions import NoSuchElementException

try:
  res = 190 / 0
except Exception as error:
  #print('FAILED: Username Textfield Element Not Found.')
  print("An error occurred:", type(error).__name__, "-", error) # An error occurred: name 'x' is not defined