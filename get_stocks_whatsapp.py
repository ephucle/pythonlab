#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 04 2020
by Hoang Le P
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime
import sys
#from twilio.rest import Client   #pip install twilio
import tkinter as tk
from tkinter import *
import re
import pandas as pd


def get_price(stock_name = "VIC"):
	path = r'C:\\Users\\ephucle\\Downloads\\chromedriver.exe' #excutable path for chromedriver, can phai tai file nay tu internet

	url = 'http://stockboard.sbsc.com.vn/apps/StockBoard/SBSC/ALL.html' 
	print("Checking stock value from", url)
	#Bảng giá sàn HOSE. https://www.hsx.vn/Modules/Rsde/RealtimeTable/LiveSecurity
	#Bảng giá sàn HNX. https://banggia.hnx.vn/

	#stock_name = "VIC" #VIC Tap Doan Vingroup, cong ty co phan
	print("Stock name:", stock_name)

	driver = webdriver.Chrome(path)

	driver.get(url)
	driver.implicitly_wait(30)  #Added implicitly wait to prevent the code from executing before the page fully loads.
	#print(driver.window_handles)


	search_box = driver.find_element_by_id('favourite-name')

	# we use try and except in case of wrong search query or any other exception
	try:
		search_box.send_keys(stock_name)       #put search query in box
		#time.sleep(5)
		search_box.send_keys(Keys.ENTER)  # press enter button 
		driver.implicitly_wait(30)
		#print(driver.current_url)

		#price1 = driver.find_element_by_id("VIC--3") #gia tham chieu, test ok
		price1 = driver.find_element_by_id(stock_name+"--3") #gia tham chieu, test ok
		price_thamchieu = float(price1.text)
		#print("Gia tham chieu co phieu VIC:", price_thamchieu)
		
		#price2 = driver.find_element_by_id("VIC-8") #gia gia khop lenh
		price2 = driver.find_element_by_id(stock_name+"-8") #gia gia khop lenh
		price_khoplenh = float(price2.text)
		#print("Gia khop lenh co phieu VIC" , price_khoplenh)

		#time.sleep(2) #cho vai giay cho nguoi dung xem ket qua tren mang hinh chrome
		return price_thamchieu, price_khoplenh
	except:
		print('An error occured')
	finally:
		driver.close()




def print_to_textbox(text_string):
	global main_textbox, root
	main_textbox.insert(tk.END, text_string + "\n")
	root.update_idletasks()



def check_stock_value():
	print("button check_stock_value press")
	global df
	#df = df[0:0]  # clear old data in df
	
	global entry_times, root
	global entry_times_var
	
	global tkvar_refresh_duration, check_interval
	
	global check_times
	check_times = int(entry_times.get())
	if check_times == 0:
		print("check done!!")
		print_to_textbox("check done!!")
		return #exit
	
	m = re.search('(\d+)m', tkvar_refresh_duration.get()) 
	if m:
		check_interval = 60* int(m.group(1)) 
		print("check_interval", check_interval)
	else:
		print("manual")
		check_interval = 1
		check_times = 1
		
	print("check_interval",check_interval)
	print("check_times", check_times)
	print("*"*20)
	
	global tkvar_stockcode
	stockcode =tkvar_stockcode.get()
	print("stockcode", stockcode)
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	giathamchieu, giakhoplenh = get_price(stockcode)
	#print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
	print(timestamp)
	print("giathamchieu", stockcode, giathamchieu)
	print("giakhoplenh", stockcode, giakhoplenh)
	
	#print_to_textbox(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
	print_to_textbox(timestamp)
	print_to_textbox("giathamchieu " +  stockcode + " " + str( giathamchieu))
	print_to_textbox("giakhoplenh " + stockcode + " "+ str(giakhoplenh))
	print_to_textbox("*"*10)
	print("*"*10)
	
	#save data to data frame, so that we can save data to csv quickly
	#df = pd.DataFrame(columns = ['datetime', 'stockcode','TC','KL'])
	#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html
	df = df.append({'datetime': timestamp, 'stockcode': stockcode, 'TC':giathamchieu, 'KL':giakhoplenh}, ignore_index=True)
	
	print(df)
	
	check_times -=1
	#update value of times in GUI
	entry_times_var.set(check_times)
	print("Remain num of check", check_times)
	
	print("Waiting", check_interval, " seconds to next check")
	print_to_textbox("Waiting " + str(check_interval) + " seconds to next check")
	
	#sau khoang thoi gian check_interval second, thi check lai
	root.after(check_interval*1000,check_stock_value)
	
	
def save_to_csv():
	print("Button save_to_csv press")
	from pathlib import Path
	HERE = Path(__file__).parent  #path of running script
	global df
	df.to_csv(HERE / 'stock.csv')
	print("Save successfule to", HERE / 'stock.csv')
	print_to_textbox("Save successfule to" + str( HERE / 'stock.csv'))
	
def gui():
	global root
	root = tk.Tk()
	root.title("VN Stock Check")
	root.geometry("300x280")
	
	# Dictionary with options
	global tkvar_stockcode
	tkvar_stockcode = StringVar(root)
	choices = {
	'VIC',
	'VNM',
	'HVN',
	'BID',
	'FPT'
	}
	tkvar_stockcode.set('VIC') # set the default option
	stockcode_om = OptionMenu(root, tkvar_stockcode, *choices)
	stockcode_om.grid(row = 0, column =0, sticky=W,padx = 5)
	
	global entry_interval,entry_times
	
	label_interval = Label(text="Refresh")
	label_interval.grid(row=0, column=0, sticky=W, padx=70)
	
	#entry_interval_var = tk.IntVar(value=10)
	#entry_interval = Entry(root, width=5)
	#entry_interval.insert(0, 30)  #default check every 30 second
	#entry_interval.grid(row = 0, column=0, sticky=W, padx = 120)
	
	global tkvar_refresh_duration
	tkvar_refresh_duration = StringVar(root)
	choices = [
	'manual',
	'1m',
	'5m',
	'15m',
	'60m'
	]
	tkvar_refresh_duration.set('1m') # set the default option
	refresh_om = OptionMenu(root, tkvar_refresh_duration, *choices)
	refresh_om.grid(row = 0, column =0, sticky=W,padx = 120)
	
	label_times = Label(text="times")
	label_times.grid(row=0, column=0, sticky=W, padx=210)
	global entry_times_var
	entry_times_var = IntVar(value=3)
	
	entry_times = Entry(root, width=5, textvariable=entry_times_var)
	#entry_times.insert(0, 10)  #default check 10 time
	
	entry_times.grid(row = 0, column=0, sticky=W, padx = 250)
	
	button_check = Button(text="check stock", command = check_stock_value)
	button_check.grid(row=1, column=0, sticky=W, padx=5)
	
	button_save_to_csv = Button(text="save to csv", command = save_to_csv)
	button_save_to_csv.grid(row=1, column=0, sticky=W, padx=100)
	
	#main_textbox = Text(root, height=15, width=50, padx = 5, pady =5)
	global main_textbox
	main_textbox = Text(root, width=30, height=10)
	main_textbox.grid(row=2, column=0, sticky=W, padx=5, pady=5)
	
	root.mainloop()

if __name__ == "__main__":
	global df
	df = pd.DataFrame(columns = ['datetime', 'stockcode','TC','KL'])
	gui()



#<input id="favourite-name" type="text" style="height:16px;width:140px" autocomplete="off" class="ac_input">


#gia tham chieu
#<td id="VIC--3" class="board-number ss-basic mainColumn">89.9</td>

#gia khop lenh
#<td id="VIC-8" class="board-number ss-down mainColumn mainColumnBold">93.8</td>