#!/usr/bin/python
import tkinter as tk

import os, sys
import json
import matplotlib.pyplot as plt
import datetime
import xlsxwriter
import time

from matplotlib.figure import Figure 

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

from datetime import datetime as dt


# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, './speedtest-cli-master')

import file


def call(cmd):
	'''

	'''
	os.system(cmd)

def run_speedtest():
	
	#tao 1 workbook moi de export file, tranh truong hop ghi file 2 lan lien tuc ko duoc
	now = dt.now()
	dt_string = now.strftime("%d%m%Y_%H%M%S")
	workbook = xlsxwriter.Workbook('speedtest'+dt_string+'.xlsx')
	worksheet = workbook.add_worksheet()
	worksheet.write('A1', "Times" )
	worksheet.write('B1', "DL")
	worksheet.write('C1', "UL")
	
	
	#label1["text"] = "RUNNING"
	#force update gui
	#top.update_idletasks()
	global output_filename
	num_of_session = int(entry_nosessions.get())

	#create raw file	
	#remove temp file before test
	if os.path.exists(output_filename):
		os.remove(output_filename)
	
	for i in range (num_of_session):
		label1["text"] = "RUNNING: " +str(i+1)+"/"+str(num_of_session)
	#force update gui
		top.update_idletasks()
		print("Download or Upload, sequence: ",i, "/",num_of_session)
		
		global var_direction
		global server_dict,var_server
		serverid = server_dict[var_server.get()]
		if var_direction.get() ==1:
			call('python ./speedtest-cli-master/speedtest.py --server '+serverid+' --no-upload --json >> '+ output_filename)
		if var_direction.get() ==2:
			call('python ./speedtest-cli-master/speedtest.py --server '+serverid +' --no-download --json >> '+ output_filename)
		if var_direction.get() ==3:
			call('python ./speedtest-cli-master/speedtest.py --server '+ serverid +' --json >> '+ output_filename)		
	
		time.sleep(0.5) # Sleep for 1 seconds

	#print("finished download")
	label1["text"] = "IDLE"
	top.update_idletasks()

	file1 = open(output_filename, 'r')
	lines = file1.readlines()
 

	# Strips the newline character
	download_Mbps = []
	upload_Mbps = []
	times = []
	line_index = 1
	for line in lines:
		line_index +=1
		line = line.strip()
		line_json = json.loads(line)
	
		timestamp = 				line_json['timestamp']  #2021-03-25T06:46:41Z
		d1 = datetime.datetime.strptime(timestamp,"%Y-%m-%dT%H:%M:%S.%fZ")
		new_format = "%Y-%m-%d %H:%M:%S"
	
		download_json_text = line_json['download'] 
		download_json_float = float(download_json_text)/1000000

		download_Mbps.append(download_json_float)
		times.append(d1.strftime(new_format))
		
		upload_json_text = line_json['upload'] 
		upload_json_float = float(upload_json_text)/1000000

		upload_Mbps.append(upload_json_float)
		
		
	
		print(d1.strftime(new_format) ,download_json_float,upload_json_float )
		worksheet.write('A'+str(line_index), d1.strftime(new_format) )
		worksheet.write('B'+str(line_index), download_json_float)
		worksheet.write('C'+str(line_index), upload_json_float)
	#close workbook, save file
	workbook.close()
	
	avg_dl = round(sum(download_Mbps)/len(download_Mbps),2)
	max_dl = round(max(download_Mbps),2)
	min_dl = round(min(download_Mbps),2)
	
	avg_ul = round(sum(upload_Mbps)/len(download_Mbps),2)
	max_ul = round(max(upload_Mbps),2)
	min_ul = round(min(upload_Mbps),2)
	
	from time import gmtime, strftime
	report_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	#'2009-01-05 22:14:39'
	
	L3 = tk.Label(top, text="************\nResult Summary:\nServer: "+var_server.get()  +", " +report_time+ " UTC \nDownload (Mbps) : Avg " + str(avg_dl) + " max: " +str(max_dl) + "  min: "+ str(min_dl)  +  "\nUpload (Mbps) : Avg " + str(avg_ul) + " max: " +str(max_ul) + " min: "+ str(min_ul))
	L3.pack()

	print ("***************************")
    # the figure that will contain the
	fig = Figure(figsize = (6, 6), dpi = 100)
	# adding the subplot 
	plot1 = fig.add_subplot(111)
	plot1.set_title("Download and Upload Bandwidth")
    # plotting the graph 
	plot1.plot(times, download_Mbps,marker="o") 
	plot1.plot(times, upload_Mbps,marker="x") 
	# containing the Matplotlib figure 
	plot1.set_xlabel("Time")
	plot1.set_ylabel("Bandwidth Mbps")
	#plot1.set_xticks(rotation=90)
	
	
	canvas = FigureCanvasTkAgg(fig,master = top) 
	canvas.draw()
	# placing the canvas on the Tkinter window 
	canvas.get_tk_widget().pack()
	
	

	
	
def sel():
   global var_direction
   temp = ""
   if var_direction.get()==1: temp = "Download"
   if var_direction.get()==2: temp = "Upload"
   if var_direction.get()==3: temp = "Download & Upload"
   
   	
   	
   selection = "You selected the option " + temp
   direction_label.config(text = selection)

#output_filename = dt_string + "output.json"
output_filename = "output.json"

top = tk.Tk()
count = 0



# Code to add widgets will go here...
L1 = tk.Label(top, text="No of speedtest session")
L1.pack()
v = tk.StringVar(top, value='3')
entry_nosessions = tk.Entry(top, bd =5,textvariable=v)


entry_nosessions.pack()
#server selection

L2 = tk.Label(top, text="OOKLA Speedtest Server")
L2.pack()
var_server = tk.StringVar(top)
var_server.set("Viettel Network")
server_om = tk.OptionMenu(top, var_server, "Viettel Network", "VNPT-NET", "MOBIFONE", "FPT Telecom")
global server_dict
server_dict = {"Viettel Network":"9903", "VNPT-NET":"6085", "MOBIFONE":"9174", "FPT Telecom":"2552"}
server_om.pack()

#control upload/download
var_direction = tk.IntVar()
#set default value 
var_direction.set(1)
R1 = tk.Radiobutton(top, text="DL", variable=var_direction, value=1,
                  command=sel)
R1.pack( anchor = tk.CENTER,pady=15)

R2 = tk.Radiobutton(top, text="UL", variable=var_direction, value=2,
                  command=sel)
R2.pack( anchor = tk.CENTER,pady=15)

R3 = tk.Radiobutton(top, text="DU", variable=var_direction, value=3,
                  command=sel)
R3.pack( anchor = tk.CENTER,pady=15)
direction_label = tk.Label(text="")
direction_label.pack()

button1 = tk.Button(text = "Run speedtest", command =run_speedtest,bg='green')
button1.pack(pady=15)
label1 = tk.Label(text ="Idle status")
label1.pack()
#global num_of_session


top.mainloop()