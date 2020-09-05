#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 12:05:37 2020

@author: somvi
@edit by Hoang Le P
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
#from twilio.rest import Client   #pip install twilio


def get_price():
    path = r'C:\\Users\\ephucle\\Downloads\\chromedriver.exe' #excutable path for chromedriver, can phai tai file nay tu internet
    url = 'https://www.hsx.vn/Modules/Rsde/RealtimeTable/LiveSecurity' 
    #Bảng giá sàn HOSE. https://www.hsx.vn/Modules/Rsde/RealtimeTable/LiveSecurity
    #Bảng giá sàn HNX. https://banggia.hnx.vn/

    topic = "VIC" #VIC Tap Doan Vingroup, cong ty co phan
    driver = webdriver.Chrome(path)
    
    driver.get(url)
    driver.implicitly_wait(30)  #Added implicitly wait to prevent the code from executing before the page fully loads.
    print(driver.window_handles)


    search_box = driver.find_element_by_id('favourite-name')
    
    # we use try and except in case of wrong search query or any other exception
    try:
        search_box.send_keys(topic)       #put search query in box
        #time.sleep(5)
        search_box.send_keys(Keys.ENTER)  # press enter button 
        driver.implicitly_wait(30)
        print(driver.current_url)
        
     
        #classes = driver.find_element_by_id("quote-header-info") #get the div for stock info
        price = driver.find_element_by_id("VIC--3") #get stock value
        print("Stock value of VIC:", price)
        print("Stock value of VIC --->:", price.text)

        
        time.sleep(500)
        #price_span = classes.find_elements_by_tag_name("span")   #get span for prive value
        
        #price = price_span[3].text 
        
        #time.sleep(5)
        
        #return price
        
    except:
        print('An error occured')
        
    finally:
        driver.close()
        
#def send_message(msg):
#    client = Client(username='*****', password='**********',
#                account_sid='*********')
#    from_number = 'whatsapp:*******'
#    to_number = 'whatsapp:*********'
#    
#    client.messages.create(body=msg, from_=from_number, to=to_number)
#    print('successfull')
        
if __name__ == "__main__":
    get_price()
    #price = float(get_price())
    #print(f'{price} is the current price')
    #
    #upper_limit = float(20.00)
    #lower_limit = float(07.00)
    #
    #
    #if price>upper_limit:
    #    msg = "sell the stocks for benefit as it is " + str(price)
    #elif price<lower_limit:
    #    msg = 'sell the stocks or you will be in loss as it is ' + str(price)
    #else:
    #    msg = 'price is between the desired range i.e ' + str(price)   
    #    
    #    
    ##send_message(msg)
    #print(msg)
    
    
    
    
    



#<input id="favourite-name" type="text" style="height:16px;width:140px" autocomplete="off" class="ac_input">

#<td id="VIC--3" class="board-number ss-basic mainColumn">89.9</td>