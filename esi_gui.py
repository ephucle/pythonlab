#!/usr/bin/env python3.8

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os, sys
from decode_esi_multidcgm import *
import concurrent.futures
import time, datetime, re

count_decode_done_for_gpg = 0 
def current_time_stamp():
	return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

def read_file(filename, target_count):
	global count_decode_done_for_gpg
	while count_decode_done_for_gpg < target_count:
		time.sleep(10)  #nghi 10s, doc file 1 lan
		print(current_time_stamp(), "start reading file")
		
		temp_count = 0
		with open(filename) as infile:
			lines = [line.strip() for line in infile.readlines()]
			for line in lines:
				
				if "GPG File has been successfully decrypted and saved to" in line or "Failed. Please try again" in line:
					temp_count += 1
		count_decode_done_for_gpg = temp_count
		print(current_time_stamp(), "end reading file")
		print(current_time_stamp(),"count  count_decode_done_for_gpg inside readfile func", count_decode_done_for_gpg)
		
		
		
		

def descypt():
	#CLEAR LOG TEXT BOX
	log_textbox.delete('1.0', END)
	log_textbox.insert(tk.END, ">>> Start decode ESI log:"+"\n")
	
	all_dcgm_names = dcgm_paths_listbox.get(0, tk.END)
	sel_idx = dcgm_paths_listbox.curselection()
	dcgm_filenames = [all_dcgm_names[index] for index in sel_idx]
	log_textbox.insert(tk.END, ">>> Selected DCGM:"+"\n")
	log_textbox.insert(tk.END, "\n".join(dcgm_filenames)+"\n")
	global root_path
	print("root_path inside descypt", root_path)
	dcgm_filepaths = [os.path.join(root_path,filename) for filename in dcgm_filenames]
	print(dcgm_filepaths)
	
	#test ok
	global esi_du, esi_ru
	esi_du = var1.get()
	esi_ru = var2.get()
	
	if esi_du == 0 and esi_ru == 0:
		esi_du =1
	print("esi_du:", esi_du)
	print("esi_ru:", esi_ru)
	
	
	
	output_filepaths = []
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
		
		logfiles_path , esi_du_filepath, esi_ru_filepaths = extract_logfiles(dcgm_file_path, nodename, target_folder_path,esi_du, esi_ru)
		if count_dcgm == 1:
			moshell_script_path = create_moshell_script(root_path, nodename, target_folder_path, esi_du_filepath, esi_ru_filepaths , esi_du, esi_ru,append_flag=False)
			
		else:
			moshell_script_path = create_moshell_script(root_path, nodename, target_folder_path, esi_du_filepath, esi_ru_filepaths, esi_du, esi_ru,append_flag=True)
			
		count_dcgm +=1
		count_gpg_file = 0
		with open(moshell_script_path) as infile:
			lines = [line.strip() for line in infile.readlines()]
			for line in lines:
				if "gpg " in line:
					count_gpg_file += 1
					log_textbox.insert(tk.END, line + "\n")
					
		root.update_idletasks()
		
		print(">>> No of gpg file need to decode", count_gpg_file)
		#doan nay da manual test ok
		
		#test update trang thai progress bar
		#progress['value'] = 20
		#root.update_idletasks() 
	
	#start decode ESI
	print(">>> Content of amos script:")
	
	print("*"*30)
	with open(moshell_script_path) as infile:
		amos_script_content = infile.read()
		print(amos_script_content)
	print("*"*30)
	
	log_textbox.insert(tk.END, ">>> Create moshell script successful\n")
	progress['value'] = 30
	root.update_idletasks()

	log_textbox.insert(tk.END, ">>> Start test ThreadPoolExecutor\n")
	root.update_idletasks()
	
	##################################threading ##################################
	#using thread, running decode esi, and check moshell output log at the same time
	
	print(current_time_stamp(),"Start test ThreadPoolExecutor")
	
	output_filepath = os.path.join(root_path , "moshell_output_log.txt")  #moshell log file
	
	global count_decode_done_for_gpg
	#reset it every time
	count_decode_done_for_gpg = 0
	
	no_of_thread = 2
	print("count_decode_done_for_gpg BEFORE", count_decode_done_for_gpg)
	with concurrent.futures.ThreadPoolExecutor(max_workers=no_of_thread) as executor:
		executor.submit(decode_esi_by_gpg, nodename, target_folder_path, moshell_script_path, modump_path, root_path) 
		executor.submit(read_file, output_filepath, count_gpg_file)  #target, count toi so count_gpg_file, thi xong
	print(current_time_stamp(),"End test ThreadPoolExecutor")
	print("count_decode_done_for_gpg AFTER", count_decode_done_for_gpg)
	#############################################################################################
	
	#output_filepath = decode_esi_by_gpg(nodename, target_folder_path, moshell_script_path, modump_path, root_path)
	print("output moshell log:", output_filepath)
	
	
	log_textbox.insert(tk.END, "moshell output path:" + output_filepath+"\n")
	
	progress['value'] = 95
	root.update_idletasks()
	
	#remove common modump, #remove logfiles.zip , #remove amos script
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
	for path in output_filepaths:
		with open (path) as infile:
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
	progress['value'] = 100
	root.update_idletasks()
	
def CurSelet(event):
	widget = event.widget
	
	all_items = widget.get(0, tk.END)
	sel_idx = widget.curselection()
	sel_list = [all_items[item] for item in sel_idx]
	print(sel_list)
	
	#thu cho show sel_list vao text box de test
	
	log_textbox.delete('1.0', END)
	for dcgm_filename in sel_list:
		log_textbox.insert(tk.END, dcgm_filename+"\n")

def var_states():
	'''print state of selection box du_esi and ru_esi to terminal'''
	print("du_esi:", var1.get())
	print("ru_esi:", var2.get())
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

root = tk.Tk()
#https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/
root.geometry("550x650")
#https://stackoverflow.com/questions/36575890/how-to-set-a-tkinter-window-to-a-constant-size/36575951
#root.resizable(0, 0) #Don't allow resizing in the x or y direction


#set root_path to home folder, work for both window and linux
#https://stackoverflow.com/questions/13923079/tkinter-home-directory
global root_path
root_path = os.path.expanduser('~')

#this is for speed up testing during code ==> remove when finished
root_path = os.path.join(root_path,"test_esi")

print("initial root_path: ", root_path)

button = tk.Button(root,text = "Select DCGM folder",command=browse_button).grid(row=0, column=0,sticky=W)

#default value to home folder
folder_path = StringVar(root, value=root_path)
lb1 = Label(root, textvariable = folder_path).grid(row=1, column=0, sticky=W)

#root_path_entry = tk.Entry(root, textvariable=default_dcgm_path, width=75).grid(row=2, column=0, sticky=W)

dcgm_paths_listbox = Listbox(root, width = 77, selectmode = tk.MULTIPLE)
dcgm_paths_listbox.bind('<<ListboxSelect>>',CurSelet)

dcgm_paths_listbox.grid(row=3, column=0, sticky=W)

log_textbox = Text(root, height=15, width=85, padx = 10, pady =10)  #height = 20 row
log_textbox.grid(row=9, column=0, sticky=W)
#log_textbox.insert(tk.END, "Just a text Widget\nin two lines\n")


dcgm_filenames = [ file for file in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, file)) and "_dcgm.zip" in file]
for item in dcgm_filenames:
	dcgm_paths_listbox.insert(END, item)



# Progress bar widget , https://www.geeksforgeeks.org/progressbar-widget-in-tkinter-python/
progress = Progressbar(root, orient = HORIZONTAL,  length = 540, mode = 'determinate')
progress_var = DoubleVar() #here you have ints but when calc. %'s usually floats

progress.grid(row=4, column=0, sticky=W, padx = 5, pady = 5)

#https://www.python-course.eu/tkinter_checkboxes.php
var1 = IntVar(value=1)  #default select for esi_du
var2 = IntVar()
du_checkbox = Checkbutton(root, text="DU ESI", variable=var1).grid(row=5, column=0, sticky=W)
#default select

ru_checkbox = Checkbutton(root, text="RU ESI", variable=var2).grid(row=6, column=0, sticky=W)
button = tk.Button(root,text = "Decrypt",command=descypt).grid(row=7, column=0,sticky=W)
button_quit = tk.Button(root,text = "Quit", command=quit).grid(row=8, column=0, sticky=W)


root.mainloop()