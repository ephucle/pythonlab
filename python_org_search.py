#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
#driver = webdriver.Firefox(executable_path='C:\\Users\\ephucle\\Downloads\\geckodriver.exe')
#driver = webdriver.Chrome()  #test ok
#test use default path of driver
driver = webdriver.Firefox()


driver.get("http://www.python.org")
assert "Python" in driver.title   #The assertion to confirm that title has “Python” word in it
elem = driver.find_element_by_name("q")
elem.clear()
#elem.send_keys("pycon")
elem.send_keys("datetime")

elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(15)
driver.close()


