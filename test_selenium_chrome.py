import time
from selenium import webdriver

#driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver = webdriver.Chrome('C:\\Users\\ephucle\\Downloads\\chromedriver.exe')  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(20) # Let the user actually see something!
driver.quit()


#dung cong cu inspect cua chrome de time ra name="q"
#<input class="gLFyf gsfi" maxlength="2048" name="q" type="text" jsaction="paste:puy29d" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwic-r26rsTrAhWFlEsFHbo1CMgQ39UDCAQ">