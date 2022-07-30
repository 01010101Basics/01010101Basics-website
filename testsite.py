#import chromedriver_binary  # Adds chromedriver binary to path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException        

driver = webdriver.Chrome('C:/codebase/webdriver/chromedriver.exe')


import os
import json


driver.get("http://10.0.0.16:82/")
elem = driver.find_element(By.XPATH, "HTML/BODY")

def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

chk = check_exists_by_xpath("HTML/BODY")

assert "No results found." not in driver.page_source

if chk == True :
    print("The test was successful!")

else: 
    print("The test failed")


driver.quit()
