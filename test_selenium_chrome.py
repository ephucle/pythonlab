#!/usr/bin/env python3
import time
from selenium import webdriver
import os

path_of_driver = 'C:\\Users\\ephucle\\Downloads\\chromedriver.exe'
if not os.path.isfile(path_of_driver):
	print(path_of_driver, "is not found in this system")
	print("you can switch to window and run this script")
	raise FileNotFoundError  #exit

#driver = webdriver.Chrome(path_of_driver)  # Optional argument, if not specified will search path.
driver = webdriver.Chrome()



driver.get('http://www.google.com/');
search_box = driver.find_element_by_name('q')
search_box.send_keys('Hello World')
search_box.submit()
time.sleep(20) # Let the user actually see something!
driver.quit()


#dung cong cu inspect cua chrome de time ra name="q"
#<input class="gLFyf gsfi" maxlength="2048" name="q" type="text" jsaction="paste:puy29d" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwic-r26rsTrAhWFlEsFHbo1CMgQ39UDCAQ">