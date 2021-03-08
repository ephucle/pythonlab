#!/usr/bin/env python3.8
#ref1 http://lte-plm.rnd.ki.sw.ericsson.se/lte_trsh_wiki/G2P/index.php?n=G2P.TraceAndError

import tkinter as tk
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import filedialog
import os, sys, subprocess, re, platform
import datetime
dir_path = os.path.dirname(os.path.realpath(__file__))
home_path = os.path.expanduser('~')

ltng_path = os.path.join(home_path, "ltng","bin")
decoder_path = os.path.join(home_path, "decoder")



print("Path of current script",dir_path)
print("Path of home folder",home_path)
print("ltng path current setting",ltng_path)

log_path = os.path.join(dir_path, "log")
if not os.path.isdir(log_path):
	print("folder does not exit")
	os.makedirs(log_path)
	print(log_path, "is created")
#sys.exit()

def current_time_stamp():
	#return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
	#return datetime.datetime.now().strftime("%Y%m%d_%H%M%S") #20210115_092615
	return datetime.datetime.now().strftime("%y%m%d_%H%M%S")
	
def get_now():
	'''
	#>>> get_now()
	#'2020-06-26 08:18:43.147639'
	#Using %f with strftime() in Python to get microseconds
	
	'''
	return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def notetype_om_selectionevent(event):
	nodetype=tkvar_nodetype.get()
	button_runtrace.config(state='disabled')
	print (nodetype)
	if nodetype == "ENODB_4G" or nodetype == "ENODB_5G":
		entry_imsi.config(state='disabled') 
		entry_cellid.config(state='disabled') 
	
	if nodetype == "RNC":
		entry_imsi.config(state='normal') 
		entry_cellid.config(state='normal') 

def print_to_textbox(text_string):
	main_textbox.insert(tk.END, text_string + "\n")
	root.update_idletasks()

def createtrace():
	#clear main text box for new cmd
	main_textbox.delete('1.0', END)
	
	nodetype = tkvar_nodetype.get()
	nodename = nodename_var.get()
	imsi = imsi_var.get()
	cellid = cellid_var.get()
	m = re.search('^\d{15}$', imsi)
	check_imsi_length = False
	if m:
		print("IMSI number is corrected, length 15")
		check_imsi_length = True
	else:
		print("IMSI number is NOT corrected, length # 15")
	
	
	global trace_cmd_filepath
	trace_cmd_filepath = os.path.join(log_path, "trace_"+nodetype+".mos")
	f = open(trace_cmd_filepath, "w")
	#print_to_textbox ("Button trace is pressed !!")
	if nodetype == "RNC"  and not imsi == "":
		if check_imsi_length:
			f.write("#RNC TRACE" + "\n")
			f.write("lh mod te default" + "\n")
			f.write("lh mod ueidtrace off -ue -all" + "\n")
			f.write("lh mod uerandtrace off -cell -all" + "\n")
			f.write("lh mod ueidtrace -ue imsi "+ imsi+  "\n")
			f.write("lh mod te e bus_send bus_receive UE_ASN_RRC" + "\n")
			f.write("lh mod te e bus_send bus_receive UE_ASN_RANAP" + "\n")
			f.write("lh mod te e bus_send bus_receive UE_ASN_RNSAP" + "\n")
			f.write("lh mod te e bus_send bus_receive UE_ASN_NBAP" + "\n")
			f.write("lh mod te e all UE_UEH_EXCEPTION" + "\n")
			f.write("lh mod te e trace4 UE_GENERAL" + "\n")
			f.write("lh mod te e trace1 trace3 UE_IU_IF" + "\n")
			f.write("lh mod te e trace3 trace6 trace7 UE_CON_HANDL" + "\n")
			f.write("mon-" + "\n")
			f.write("mon mod" + "\n")
			f.write("l-" + "\n")
		else:
			print_to_textbox("IMSI number is not corrected, check IMSI length")
	
	if nodetype == "RNC"  and not cellid == "":
		f.write("$password = rnc" +"\n")
		f.write("lh mod te default" +"\n")
		f.write("lh mod ueidtrace off -ue -all" +"\n")
		f.write("lh mod uerandtrace off -cell -all" +"\n")
		f.write("lh mod uerandtrace on -cell "+ cellid +  "\n")
		f.write("lh mod uerandtrace max -unlim" +"\n")
		f.write("lh mod te e bus_send bus_receive UE_ASN_RRC" +"\n")
		f.write("lh mod te e bus_send bus_receive UE_ASN_RANAP" +"\n")
		f.write("lh mod te e bus_send bus_receive UE_ASN_RNSAP" +"\n")
		f.write("lh mod te e bus_send bus_receive UE_ASN_NBAP" +"\n")
		f.write("lh mod te e all UE_UEH_EXCEPTION" +"\n")
		f.write("lh mod te e trace4 UE_GENERAL" +"\n")
		#f.write("lh mod te e trace1 trace3 UE_IU_IF" +"\n")
		#f.write("lh mod te e trace3 trace6 trace7 UE_CON_HANDL" +"\n")
		f.write("mon-" +"\n")
		f.write("mon mod" +"\n")
		

	
	if nodetype == "ENODB_5G":
		f.write( "#5G eNB CPM has functional traces" + "\n")
		f.write( "#Cell and sector traces:" + "\n")
		f.write( "lh mp te default " + "\n")
		f.write( "te e all Ft_X2AP_ASN" + "\n")
		f.write( "te e all Ft_RRC_ASN" + "\n")
		f.write( "te e all Ft_S1AP_ASN" + "\n")
		f.write( "te e all Ft_X2_COMMON_SIGNALING" + "\n")
		f.write( "te e all Ft_ENDC_SETUP" + "\n")
		f.write( "te e all Ft_ENDC_RELEASE" + "\n")
		f.write( "te e all Ft_ENDC" + "\n")
		f.write( "te e all Ft_NR_RRC_ASN" + "\n")
		f.write( "te e all Ft_NR_LEG_RELEASE" + "\n")
		f.write( "te filter set '[1] <> \$0A' Ft_S1AP_ASN" + "\n")
		f.write( "ue enable -allcell -allUe -timeout 720" + "\n")
		f.write( "te save *" + "\n")
	if nodetype == "ENODB_4G":
		f.write( "#4G eNB CPM has functional traces" + "\n")
		f.write("lh mp te e all Ft_X2AP_ASN" + "\n")
		f.write("lh mp te e all Ft_RRC_ASN" + "\n")
		f.write("lh mp te e all Ft_S1AP_ASN" + "\n")
		f.write("lh mp te e all Ft_X2_COMMON_SIGNALING" + "\n")
		f.write("lh mp ue enable -allcell -allUe -timeout 720" + "\n")
		f.write("#G2 paging filter" + "\n")
		f.write("lh mp te filter set '[1] <> $0A' Ft_S1AP_ASN" + "\n")
		f.write("#G1 paging filter"  + "\n")
		f.write("lh mp te filter set \"[1] <> $0A\" Ft_S1AP_ASN" + "\n")
		f.write("mon-" + "\n")
		f.write("mon mp" + "\n")
		f.write("l-" + "\n")
		
	
	current_datetime = current_time_stamp()
	raw_filepath  = os.path.join(log_path , nodename+"_"+current_datetime+"_r.log")
	dec_filepath  = os.path.join(log_path , nodename+"_"+current_datetime+"_d.log")
	flow_filepath = os.path.join(log_path , nodename+"_"+current_datetime+"_f.log")
	
	ltngdecoder_path = os.path.join(ltng_path, "ltng-decoder")
	ltngflow_path = os.path.join(ltng_path, "ltng-flow")
	
	wcdmadecoder = os.path.join(decoder_path, "decoder.pl")
	wcdmaflow = os.path.join(decoder_path, "flow.pl")
	if nodetype == "ENODB_5G" or nodetype == "ENODB_4G":
		f.write("! $moncommand | tee " + raw_filepath + " | "+ ltngdecoder_path +" -s | tee " + dec_filepath + " | "+ ltngflow_path + " | tee "+ flow_filepath + "\n")
	if nodetype == "RNC" and check_imsi_length:
		f.write("! $moncommand | tee " + raw_filepath + " | "+ wcdmadecoder +" --w18b | tee " + dec_filepath + " | "+ wcdmaflow + " -colour | tee "+ flow_filepath + "\n")
	f.close()
	
	with open (trace_cmd_filepath) as infile:
		all_lines = infile.read()
		#clear terminal screen
		print('\033c')
		print(all_lines)
		print_to_textbox (all_lines)
	
	button_runtrace.config(state='normal')   #enable nut RUN
	button_runtrace.config(bg='spring green')
	output_scriptpath_var.set("Output PATH: "+trace_cmd_filepath)
	outputscript_label.config(bg="spring green")

def runtrace():
	print("run trace button is pressed !!")
	moshell_path = subprocess.getoutput('which moshell')
	nodename = nodename_var.get()
	full_script = moshell_path + " " + nodename + " " + trace_cmd_filepath
	print (">>> moshell  trace script: ",full_script)
	print (">>>", get_now(),"Running trace script by moshell...")
	
	#this help to save command result to variable
	#command = os.popen(full_script)
	#crash_log_export = command.read()
	#print(crash_log_export)
	#command.close()
	
	#this help to see result online when run command
	os.system(full_script)  

def ping_check():
	print("ping button is pressed!!")
	ipaddress = nodename_var.get()
	print("ipaddress:" ,ipaddress)
	ping_result_var = StringVar(root, value="")
	ping_label = Label(root, textvariable = ping_result_var)
	ping_label.grid(row=1, column=0, sticky=W, padx = 320)
	
	if ping(ipaddress):
		print("ICMP Ping is OK")
		ping_result_var.set('PING-----OK')
		root.update_idletasks()
	else:
		print("ICMP Ping is NOK")
		ping_result_var.set('PING---NOK')
		root.update_idletasks()

def OnEntryClick_imsi(event):
	print("Entry IMSI is clicked")
	entry_cellid.delete(0, 'end')
	entry_cellid.config(state='disabled') 
	entry_imsi.config(state='normal')
	
def OnEntryClick_cellid(event):
	print("Entry CELLID is clicked")
	entry_imsi.delete(0, 'end')
	entry_imsi.config(state='disabled')
	entry_cellid.config(state='normal')
	
def gui():
	global root
	root = tk.Tk()
	root.title("TRACETOOL_RANIT_ERICSSON_" + current_time_stamp())
	root.geometry("600x470")
	
	#cac bien de canh chinh GUI
	tab1_width = 80
	column2_width = 20
	
	
	
	# NODE TYPE, row 0
	label_upper = Label(text="NODE TYPE").grid(row=0, column=0, sticky=W, padx=5)
	global tkvar_nodetype
	tkvar_nodetype = StringVar(root)
	choices = {
	'RNC',
	'ENODB_4G',
	'ENODB_5G',
	}
	tkvar_nodetype.set('RNC') # set the default option
	notetype_om = OptionMenu(root, tkvar_nodetype, *choices, command=notetype_om_selectionevent)
	notetype_om.grid(row = 0, column =0, sticky=W,padx = tab1_width)
	
	#NODENAME, ROW1
	label_nodename = Label(text="NODE NAME")
	label_nodename.grid(row=1, column=0, sticky=W, padx=5)
	global nodename_var
	nodename_var = StringVar(value="169.254.2.2")
	entry_nodename = Entry(root, width=column2_width, textvariable=nodename_var)
	entry_nodename.grid(row = 1, column=0, sticky=W, padx = tab1_width)
	
	#PING
	button_pingtest = tk.Button(root,text = "PING TEST", command=ping_check, bg="yellow")
	button_pingtest.grid(row=1, column=0, sticky=W, padx=250)
	
	#IMSI, ROW2
	label_imsi = Label(text="IMSI")
	label_imsi.grid(row=2, column=0, sticky=W, padx=5)
	global imsi_var, entry_imsi
	imsi_var = StringVar(value="452041234512345")
	entry_imsi = Entry(root, width=column2_width, textvariable=imsi_var)
	entry_imsi.grid(row = 2, column=0, sticky=W, padx = tab1_width)
	#entry_imsi.bind("<KeyRelease>", OnEntryClick_imsi) #keyup 
	entry_imsi.bind("<1>", OnEntryClick_imsi) #left mouse button click 
	
	
	#CELLID, ROW2
	label_cell = Label(text="CELLID")
	label_cell.grid(row=2, column=0, sticky=W, padx=250)
	global cellid_var, entry_cellid
	cellid_var = StringVar(value="12345")
	entry_cellid = Entry(root, width=column2_width , textvariable=cellid_var)
	entry_cellid.grid(row = 2, column=0, sticky=W, padx = tab1_width + 230)
	entry_cellid.bind("<1>", OnEntryClick_cellid) #keyup 
	
	#BUTTON CREATE TRACE COMMAND, ROW4
	button_createtrace = tk.Button(root,text = "CREATE TRACE CMD", command=createtrace, bg="yellow")
	button_createtrace.grid(row=4, column=0, sticky=W, padx=5)
	
	#BUTTON CREATE TRACE COMMAND, ROW4
	global button_runtrace
	#button_runtrace = tk.Button(root,text = "RUN TRACE", command=runtrace, bg="spring green")
	button_runtrace = tk.Button(root,text = "RUN TRACE", command=runtrace)
	button_runtrace.grid(row=4, column=0, sticky=W, padx=150)
	button_runtrace.config(state='disabled')   #moi khoi tao thi disable nut nay
	
	#main text box, ROW5
	global main_textbox
	main_textbox = Text(root, height=15, width=column2_width + 60)
	main_textbox.grid(row=5, column=0, sticky=W, padx =5, pady = 2)
	
	#BUTTON QUIT, ROW6
	#button_quit = tk.Button(root,text = "Quit", command=quit, bg="LightBlue1").grid(row=6, column=0, sticky=W, padx=5)
	#using root.destroy to avoid is issue when buid app by installer
	button_quit = tk.Button(root,text = "Quit", command=root.destroy, bg="tomato").grid(row=6, column=0, sticky=W, padx=5)
	
	if os.path.isdir(decoder_path):
		wcdmadecoder_var = StringVar(root, value="3G Decoder: "+decoder_path)
	else :
		wcdmadecoder_var = StringVar(root, value="3G Decoder: "+ "is not existed")
	
	wcdmadecoder_label = Label(root, textvariable = wcdmadecoder_var)
	wcdmadecoder_label.grid(row=7, column=0, sticky=W, padx = 5)
	
	if os.path.isdir(ltng_path):
		ltngdecoder_var = StringVar(root, value="LTNG: "+ltng_path)
	else:
		ltngdecoder_var = StringVar(root, value="LTNG: "+"is not existed")
	ltngdecoder_label = Label(root, textvariable = ltngdecoder_var)
	ltngdecoder_label.grid(row=8, column=0, sticky=W, padx = 5)

	#LABEL OUTPUT SCRIPT, ROW 9
	global output_scriptpath_var, outputscript_label
	output_scriptpath_var = StringVar(root, value="Output PATH: ")
	outputscript_label = Label(root, textvariable = output_scriptpath_var)
	outputscript_label.grid(row=9, column=0, sticky=W, padx = 5)
	
	#LABEL CURRENT SYSTEM, ROW 10
	global current_system_var, current_system_label
	current_system_var = StringVar(root, value="Current system: " + platform.system())
	current_system_label = Label(root, textvariable = current_system_var)
	current_system_label.grid(row=10, column=0, sticky=W, padx = 5)
	
	root.mainloop()


if __name__ == "__main__":
	
	gui()