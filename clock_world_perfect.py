#!/usr/bin/env python3.8
import tkinter as tk
import datetime, pytz

mainWindow = tk.Tk()
mainWindow.title("CLOCK")
def convert_datetime_timezone(dt, tz1, tz2):
	'''
	dt = 09:49:31
	'''
	tz1 = pytz.timezone(tz1)
	tz2 = pytz.timezone(tz2)
	
	dt = datetime.datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
	dt = tz1.localize(dt)
	dt = dt.astimezone(tz2)
	dt1 = dt.strftime("%H:%M:%S")
	return dt1



def update_clock_label():
    current_dt_hcm_hours = datetime.datetime.now().strftime("%H:%M:%S")
    lb.config(text = current_dt_hcm_hours)
    mainWindow.after(250,update_clock_label)

def update_clock_label2():
    current_dt_hcm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_dt_kst = convert_datetime_timezone(current_dt_hcm,"Asia/Ho_Chi_Minh","Asia/Seoul")
    lb2.config(text = current_dt_kst)
    mainWindow.after(250,update_clock_label2)

def update_clock_label3():
    current_dt_hcm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_dt_sweden = convert_datetime_timezone(current_dt_hcm,"Asia/Ho_Chi_Minh","Europe/Stockholm")
    lb3.config(text = current_dt_sweden)
    mainWindow.after(250,update_clock_label3)



lb = tk.Label(mainWindow, font = ('Consolas', 40, 'bold'), background = 'purple', foreground = 'white')
lb.grid(row=2, column = 0)
lb2 = tk.Label(mainWindow, font = ('Consolas', 40, 'bold'), background = 'blue', foreground = 'white')
lb2.grid(row=3, column = 0)
lb3 = tk.Label(mainWindow, font = ('Consolas', 40, 'bold'), background = 'green', foreground = 'white')
lb3.grid(row=4, column = 0)
#loop1
update_clock_label()

#loop2
update_clock_label2()

#loop3
update_clock_label3()

mainWindow.mainloop()