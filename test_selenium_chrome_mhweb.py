import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import codecs

trid = "HY59201"

#https://stackoverflow.com/questions/31062789/how-to-load-default-profile-in-chrome-using-python-selenium-webdriver

options = Options() #Chrome Options, Chrome_Options ist deprecated. Use options instead
options.add_argument("user-data-dir=C:\\Users\\ephucle\\AppData\\Local\\Google\\Chrome\\User Data")

#my profile folder
#C:\Users\ephucle\AppData\Local\Google\Chrome\User Data\Default ===> to use it in the script I had to exclude \Default\ so we end up with only 

driver = webdriver.Chrome(executable_path='C:\\Users\\ephucle\\Downloads\\chromedriver.exe', chrome_options=options)

driver.get('https://mhweb.ericsson.se/')

time.sleep(10) # Let the user actually see something!
search_box = driver.find_element_by_name('frm_smartOpenInput')
search_box.send_keys(trid)

#https://stackoverflow.com/questions/10629815/how-to-switch-to-new-window-in-selenium-for-python
window_before = driver.window_handles[0]
#print (window_before)
window_before_title = driver.title
print(window_before_title)

search_box.send_keys(Keys.RETURN)  #press ENTER to start searching, like user behavior
#cho driver download new page
time.sleep(5) # cho doi la hanh phuc

#test ok, da mo duoc tr id ==> mo qua mot cua so moi

window_after = driver.window_handles[1]
#print(window_after)
#then execute the switch to window methow to move to newly opened window
#driver.switch_to_window(window_after)  #move to new window ==>deprecated
driver.switch_to.window(window_after)  #https://www.techbeamers.com/switch-between-windows-selenium-python/

window_after_title = driver.title
print(window_after_title)

#save page (save new window)
output_filepath = "C:\\Users\\ephucle\\Documents\\HY59201.html"

#with open(output_filepath, "w") as f:
file_object = codecs.open(output_filepath, "w", "utf-8")
html = driver.page_source
file_object.write(html)
print("Save successful", output_filepath)

time.sleep(6000) # Let the user actually see something!
driver.quit()

#search field
#<input autocomplete="off" class="rf-au-fnt rf-au-inp rf-plhdr" id="frm_smartOpenInput" name="frm_smartOpenInput" onclick="if (RichFaces.component('frm_smartOpen').items.length > 0) {RichFaces.component('frm_smartOpen').showPopup();}" onkeydown="return page.toolbar.openObjectKeyUp(RichFaces.component('frm_smartOpen'), event);" type="text" tabindex="10">

#"Open button"
#<input id="frm_openObject" name="frm_openObject" onclick="jsf.util.chain(this,event,&quot;page.toolbar.openButtonClick();&quot;,&quot;RichFaces.ajax(\&quot;frm_openObject\&quot;,event,{\&quot;incId\&quot;:\&quot;1\&quot;} )&quot;);return false;" value="Open" onmousedown="RichFaces.component('frm_smartOpen').setValue(jQuery('#frm_smartOpenInput').val());" type="submit" tabindex="11">