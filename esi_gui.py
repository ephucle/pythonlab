#!/usr/bin/env python3.8
import tkinter as tk
from tkinter import *
from tkinter.ttk import Progressbar
from pathlib import Path
from tkinter import filedialog
import os, sys
from decode_esi_multidcgm import *
import concurrent.futures
import time, datetime, re

count_decode_done_for_gpg = 0 
def current_time_stamp():
	return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

#def read_file(filename, target_count):
def read_file():
	global count_gpg_file
	global count_decode_done_for_gpg, output_filepath
	
	#print("START READFILE FUNC,count_gpg_file", count_gpg_file)
	#print("START READFILE FUNC, count_decode_done_for_gpg", count_decode_done_for_gpg)
	while count_decode_done_for_gpg < count_gpg_file:
		time.sleep(3)  #nghi 10s, doc file 1 lan ==> ko nen dung sleep ben trong gui
		#if os.path.isfile(output_filepath):
		try:
			successfully_lines = [line for line in open(output_filepath) if "GPG File has been successfully decrypted" in line or '''>>>>>> Failed. Please try again.''' in line]
			count_decode_done_for_gpg = len(successfully_lines)
			print("count_decode_done_for_gpg during read_file funtion:", count_decode_done_for_gpg)
		except FileNotFoundError:
			time.sleep(3) #cho 3 giay thi kiem tra lai file
		
		percent_finished = int(100*(count_decode_done_for_gpg/count_gpg_file))
		print("percent_finished", percent_finished)
		#barVar.set(percent_finished)


def decrypt():
	#CLEAR LOG TEXT BOX
	log_textbox.delete('1.0', END)
	log_textbox.insert(tk.END, ">>> Start decode ESI log:"+"\n")

	all_dcgm_names = dcgm_paths_listbox.get(0, tk.END)
	sel_idx = dcgm_paths_listbox.curselection()
	dcgm_filenames = [all_dcgm_names[index] for index in sel_idx]
	if len(dcgm_filenames) > 0:
		log_textbox.insert(tk.END, ">>> Selected DCGM:"+"\n")
		log_textbox.insert(tk.END, "\n".join(dcgm_filenames)+"\n")
	else:
		log_textbox.insert(tk.END, ">>> Please selected at least a DCGM"+"\n")
		
		
	global root_path
	print("root_path inside decrypt", root_path)
	dcgm_filepaths = [os.path.join(root_path,filename) for filename in dcgm_filenames]
	print(dcgm_filepaths)
	
	#test ok
	global esi_du, esi_ru
	esi_ru = 0
	esi_du = var1.get()
	
	esi_ru0 = vars0.get()
	esi_ru1 = vars1.get()
	esi_ru2 = vars2.get()
	esi_ru3 = vars3.get()
	esi_ru4 = vars4.get()
	esi_ru5 = vars5.get()
	
	
	
	selected_sector = (esi_ru0,esi_ru1,esi_ru2,esi_ru3, esi_ru4, esi_ru5)
	if any(selected_sector):
		esi_ru = 1
	if esi_du == 0 and esi_ru == 0:
		esi_du =1
	print("esi_du:", esi_du)
	print("esi_ru:", esi_ru)
	print("esi_ru0:", esi_ru0)
	print("esi_ru1:", esi_ru1)
	print("esi_ru2:", esi_ru2)
	print("esi_ru3:", esi_ru3)
	print("esi_ru4:", esi_ru4)
	print("esi_ru5:", esi_ru5)
	
	print("selected_sector",selected_sector)
	#sys.exit()
	
	input_nodenames = set()
	
	count_success = 0
	success_output_list = []
	success_nodenames = set()
	
	#lay 1 dcgm va extract modump, de dung chung cho tat ca
	modump_path = extract_modump(dcgm_filepaths[0], root_path)
	
	count_dcgm = 1
	for dcgm_file_path in dcgm_filepaths:
		#print(path)
		temp_path, dcgm_filename = os.path.split(dcgm_file_path)
		print(temp_path, dcgm_filename, sep = "|")
		#extract nodename from dcgm filename
		nodename =  re.match("(\S+)_\d{6}_\d{6}_\S+_dcgm.zip", dcgm_filename).group(1)
		
		input_nodenames.add(nodename)
		
		target_folder_path = create_target_folder(nodename, root_path)
		#extract du and ru esi , save path to esi_du_filepath, esi_ru_filepaths
		logfiles_path , esi_du_filepath, esi_ru_filepaths = extract_logfiles(dcgm_file_path, nodename, target_folder_path,esi_du, esi_ru, selected_sector = selected_sector)
		if count_dcgm == 1:
			moshell_script_path = create_moshell_script(root_path, nodename, target_folder_path, esi_du_filepath, esi_ru_filepaths , esi_du, esi_ru,append_flag=False)
			
		else:
			moshell_script_path = create_moshell_script(root_path, nodename, target_folder_path, esi_du_filepath, esi_ru_filepaths, esi_du, esi_ru,append_flag=True)
			
		count_dcgm +=1
		global count_gpg_file
		count_gpg_file = 0
		log_textbox.insert(tk.END, ">>> gpg file:" + "\n")
		with open(moshell_script_path) as infile:
			lines = [line.strip() for line in infile.readlines()]
			for line in lines:
				if "gpg " in line: #
					count_gpg_file += 1
					gpg_filepath = line.split()[-1]
					#log_textbox.insert(tk.END, line + "\n")
					log_textbox.insert(tk.END, gpg_filepath + "\n")
					
		root.update_idletasks()
		log_textbox.insert(tk.END, "******" + "\n")
		print(">>> No of gpg file need to decode", count_gpg_file)
	
	#start decode ESI
	print(">>> Content of amos script:")
	
	print("*"*30)
	with open(moshell_script_path) as infile:
		amos_script_content = infile.read()
		print(amos_script_content)
	print("*"*30)
	
	log_textbox.insert(tk.END, ">>> Create moshell script successful\n")
	#progress['value'] = 30
	#root.update_idletasks()
	barVar.set(30)

	#log_textbox.insert(tk.END, ">>> Start test ThreadPoolExecutor\n")
	root.update_idletasks()
	
	##################################threading ##################################
	#using thread, running decode esi, and check moshell output log at the same time
	
	print(current_time_stamp(),"Start test ThreadPoolExecutor")
	global output_filepath
	output_filepath = os.path.join(root_path , "moshell_output_log.txt")  #moshell log file
	
	global count_decode_done_for_gpg
	#reset it every time
	count_decode_done_for_gpg = 0
	
	no_of_thread = 2
	print("count_decode_done_for_gpg BEFORE ThreadPoolExecutor", count_decode_done_for_gpg)
	with concurrent.futures.ThreadPoolExecutor(max_workers=no_of_thread) as executor:
		executor.submit(decode_esi_by_gpg, nodename, target_folder_path, moshell_script_path, modump_path, root_path) 
		executor.submit(read_file)  #target, count toi so count_gpg_file, thi xong
	print("End test ThreadPoolExecutor")
	print("count_decode_done_for_gpg AFTER ThreadPoolExecutor", count_decode_done_for_gpg)
	#############################################################################################
	
	#output_filepath = decode_esi_by_gpg(nodename, target_folder_path, moshell_script_path, modump_path, root_path)
	print("output moshell log:", output_filepath)
	
	
	log_textbox.insert(tk.END, "moshell output path:" + output_filepath+"\n")
	
	#progress['value'] = 95
	#root.update_idletasks()
	
	barVar.set(95)
	
	#remove common modump, #remove logfiles.zip , #remove amos script
	print("Cleaning temp log file")
	os.remove(modump_path)
	os.remove(logfiles_path)
	os.remove(moshell_script_path)
	
	
	#remove esi log
	if esi_du:
		os.remove(esi_du_filepath)
	if esi_ru:
		for path in esi_ru_filepaths:
			os.remove(path)
	
	#summary decode result
	with open (output_filepath) as infile:
		lines = (line.strip() for line in infile.readlines())
		for line in lines:
			m = re.match("GPG File has been successfully decrypted and saved to (\S+)", line) 
			if m:
				success_output_file = m.group(1) 
				temp_path = success_output_file.partition("/rcslogs/")[0]
				temp_path2 , nodename_date = os.path.split(temp_path)
				nodename = nodename_date.partition("_")[0]
				success_nodenames.add(nodename)
				
				success_output_list.append(success_output_file)
				count_success += 1
	
	if count_success == 0 :
		print(f">>> Failed to decoded ALL dcgm:")
		print(CRED+ "\n".join(dcgm_filepaths)+ CEND)
		
		log_textbox.insert(tk.END, "Failed to decoded ALL dcgm\n")
		log_textbox.insert(tk.END, "\n".join(list(input_nodenames)) +"\n")
		
	else:
		
		print(">>> Successful decode ALL ESI files, as below")
		log_textbox.insert(tk.END, "Successful decode ALL ESI files, as below:\n")
		print("\n".join(success_output_list))
		log_textbox.insert(tk.END, "\n".join(success_output_list) + "\n")
		
		if len(success_nodenames) < len(input_nodenames):  #truong hop nay chi decode thanh cong vai esi, fail vai esi
			print("Detail:")
			print("#"*20)
			print("Failure nodes:")
			
			fail_nodes = input_nodenames.difference(success_nodenames)
			fail_nodes = list(fail_nodes)
			
			print(CRED + "\n".join(fail_nodes) + CEND)
			log_textbox.insert(tk.END, "\nDetail:\n")
			log_textbox.insert(tk.END, "\nFailure nodes:\n" + "\n".join(fail_nodes)+"\n")
			
			print("Success nodes:")
			success_nodenames = list(success_nodenames)
			
			print(CRED + "\n".join(success_nodenames) + CEND)
			log_textbox.insert(tk.END, "\nSuccess decode node:\n" + "\n".join(success_nodenames)+"\n")
			print("#"*20)
	
	log_textbox.insert(tk.END, "\n" + "Decode procedure finished!"+"\n")
	os.remove(output_filepath)
	barVar.set(100)
	
def CurSelet(event):
	widget = event.widget
	
	all_items = widget.get(0, tk.END)
	sel_idx = widget.curselection()
	sel_list = [all_items[item] for item in sel_idx]
	print(sel_list)

	#log_textbox.delete('1.0', END)
	log_textbox.insert(tk.END, "*************"+"\n")
	for dcgm_filename in sel_list:
		log_textbox.insert(tk.END, dcgm_filename+"\n")

def var_states():
	'''print state of selection box du_esi and ru_esi to terminal'''
	print("du_esi:", var1.get())
	#print("ru_esi:", var2.get())
	#print("du_esi: %d,\ru_esi: %d" % (var1.get(), var2.get()))
def browse_button():
	global folder_path
	global root_path
	root_path = filedialog.askdirectory()
	
	print("root_path after browse_button:",root_path)
	folder_path.set(root_path)
	
	#update dcgm_paths_listbox
	dcgm_paths_listbox.delete(0, END)
	dcgm_filenames = [ file for file in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, file)) and "_dcgm.zip" in file]
	for item in dcgm_filenames:
		dcgm_paths_listbox.insert(END, item)

def print_to_textbox(text_string):
	log_textbox.insert(tk.END, text_string + "\n")
	root.update_idletasks()

def OptionMenu_SelectionEvent(event): # I'm not sure on the arguments here, it works though
	global root_path
	global folder_path
	
	## do something
	print("Option menu selected")
	selected_path = tkvar_fav_dir.get()
	
	print("value selected:",selected_path)
	#neu path ton tai tren may client thi set root path ve gia tri duoc chon
	if os.path.isdir(selected_path):
		root_path = Path(selected_path)
		folder_path.set(root_path)  #set label
		#update dcgm_paths_listbox
		dcgm_paths_listbox.delete(0, END)
		dcgm_filenames = [ file for file in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, file)) and "_dcgm.zip" in file]
		dcgm_filenames.sort()
		for item in dcgm_filenames:
			dcgm_paths_listbox.insert(END, item)

root = tk.Tk()
root.title("ESI decrypt tool")
root.geometry("550x550")


#set root_path to home folder, work for both window and linux
#https://stackoverflow.com/questions/13923079/tkinter-home-directory
global root_path
root_path = os.path.expanduser('~')

#this is for speed up testing during code ==> remove when finished
#root_path = os.path.join(root_path,"test_esi")
#root_path = os.path.join(root_path,"abc")

print("initial root_path: ", root_path)

button = tk.Button(root,text = "Select DCGM folder",command=browse_button).grid(row=0, column=0,sticky=W)

# Dictionary with options
tkvar_fav_dir = StringVar(root)
choices = {
	'favorite path',
	root_path, 
	'/mnt/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM',
	'/cygdrive/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM'
}

tkvar_fav_dir.set('favorite_path') # set the default option
favorite_path_optionmenu = OptionMenu(root, tkvar_fav_dir, *choices, command = OptionMenu_SelectionEvent)
favorite_path_optionmenu.grid(row = 0, column =0, sticky=W,padx = 150)

#default value to home folder
folder_path = StringVar(root, value=root_path)
lb1 = Label(root, textvariable = folder_path).grid(row=1, column=0, sticky=W)

#root_path_entry = tk.Entry(root, textvariable=default_dcgm_path, width=75).grid(row=2, column=0, sticky=W)

dcgm_paths_listbox = Listbox(root, width = 77, selectmode = tk.MULTIPLE)
dcgm_paths_listbox.bind('<<ListboxSelect>>',CurSelet)

dcgm_paths_listbox.grid(row=3, column=0, sticky=W)



try:
	dcgm_filenames = [ file for file in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, file)) and "_dcgm.zip" in file]
except FileNotFoundError:
	print("pls select a corrected dcgm folder")
	sys.exit()

for item in dcgm_filenames:
	dcgm_paths_listbox.insert(END, item)



# Progress bar widget , https://www.geeksforgeeks.org/progressbar-widget-in-tkinter-python/
#progress = Progressbar(root, orient = HORIZONTAL,  length = 540, mode = 'determinate')

barVar = tk.DoubleVar()
barVar.set(0)
progress = Progressbar(root, orient = HORIZONTAL,  length = 540, mode = 'determinate', variable=barVar)


progress.grid(row=4, column=0, sticky=W, padx = 5, pady = 5)

#https://www.python-course.eu/tkinter_checkboxes.php
var1 = IntVar(value=1)  #default select for esi_du

du_checkbox = Checkbutton(root, text="DU ESI", variable=var1).grid(row=5, column=0, sticky=W, padx=5)



vars0 = IntVar()
vars1 = IntVar()
vars2 = IntVar()
vars3 = IntVar()
vars4 = IntVar()
vars5 = IntVar()
sector0_checkbox = Checkbutton(root, text="RU0_2048", variable=vars0).grid(row=6, column=0, sticky=W, padx=5)
sector1_checkbox = Checkbutton(root, text="RU1_2049", variable=vars1).grid(row=6, column=0, sticky=W, padx=80)
sector2_checkbox = Checkbutton(root, text="RU2_2050", variable=vars2).grid(row=6, column=0, sticky=W, padx=155)
sector3_checkbox = Checkbutton(root, text="RU3_2051", variable=vars3).grid(row=6, column=0, sticky=W, padx=230)
sector4_checkbox = Checkbutton(root, text="RU4_2052", variable=vars4).grid(row=6, column=0, sticky=W, padx=305)
sector5_checkbox = Checkbutton(root, text="RU5_2053", variable=vars5).grid(row=6, column=0, sticky=W, padx=380)


button = tk.Button(root,text = "Decrypt",command=decrypt).grid(row=7, column=0,sticky=W)
button_quit = tk.Button(root,text = "Quit", command=quit).grid(row=8, column=0, sticky=W)

log_textbox = Text(root, height=15, width=85, padx = 10, pady =10)  #height = 20 row
log_textbox.grid(row=9, column=0, sticky=W)

# Dictionary with options
tkvar = StringVar(root)
choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
tkvar.set('Pizza') # set the default option
pmd_optionmenu = OptionMenu(root, tkvar, *choices)
pmd_optionmenu.grid(row = 7, column =0, sticky=W,padx = 75)


root.mainloop()