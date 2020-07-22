#!/usr/bin/env python3

# importing whole module 
import datetime, pytz
from tkinter import * 
from tkinter.ttk import *  #to support widget Label

# creating tkinter window 
root = Tk() 
root.title('Clock')

def convert_datetime_timezone(dt, tz1, tz2):
	'''
	dt = 2019-12-18 09:49:31
	'''
	tz1 = pytz.timezone(tz1)
	tz2 = pytz.timezone(tz2)
	
	#format input dt
	dt = datetime.datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
	dt = tz1.localize(dt)
	dt = dt.astimezone(tz2)
	#dt1 = dt.strftime("%Y-%m-%d %H:%M:%S")
	#show hour only
	dt1 = dt.strftime("%H:%M:%S")
	return dt1

def update_time_labels(): 
	'''
	This function is used to  display time on the label
	'''
	current_dt_hcm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	current_dt_hcm_hours = datetime.datetime.now().strftime("%H:%M:%S")
	current_dt_kst = convert_datetime_timezone(current_dt_hcm,"Asia/Ho_Chi_Minh","Asia/Seoul")
	current_dt_swd = convert_datetime_timezone(current_dt_hcm,"Asia/Ho_Chi_Minh","Europe/Stockholm")
	
	text = "VN " + current_dt_hcm_hours
	text += "\n" + "KR " + current_dt_kst
	text += "\n" + "SW " + current_dt_swd
	
	lbl.config(text = text)
	lbl.after(1000, update_time_labels)


# Styling the label widget so that clock will look more attractive , using fix font
lbl  = Label(root, font = ('Consolas', 40, 'bold'), background = 'purple', foreground = 'white')

# Placing clock at the centre of the tkinter window 
lbl.pack(anchor = 'center')

#call funtion to update label every 1000ms
update_time_labels()

mainloop()