#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

import os, sys
from decode_esi_multidcgm import *
def descypt():
	#CLEAR LOG TEXT BOX
	log_textbox.delete('1.0', END)
	
	log_textbox.insert(tk.END, ">>> Start decode ESI log:"+"\n")
	#dcgm_filenames = dcgm_paths_listbox.get(0, tk.END)
	
	all_dcgm_names = dcgm_paths_listbox.get(0, tk.END)
	sel_idx = dcgm_paths_listbox.curselection()
	dcgm_filenames = [all_dcgm_names[index] for index in sel_idx]
	log_textbox.insert(tk.END, ">>> Selected DCGM:"+"\n")
	log_textbox.insert(tk.END, "\n".join(dcgm_filenames)+"\n")
	global root_path
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
	
	count = 0
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
		
		#test update trang thai progress bar
		progress['value'] = 20
		root.update_idletasks() 
	
	#start decode ESI
	print(">>> Content of amos script:")
	
	print("*"*30)
	with open(moshell_script_path) as infile:
		amos_script_content = infile.read()
		print(amos_script_content)
	print("*"*30)
	
	log_textbox.insert(tk.END, ">>> Create moshell script successful\n")
	progress['value'] = 30  # so 50% o day chua chinh xac lam
	root.update_idletasks()
	
	
	log_textbox.insert(tk.END, ">>> Running GPG....\n")
	output_filepath = decode_esi_by_gpg(nodename, target_folder_path, moshell_script_path, modump_path)
	output_filepaths.append(output_filepath)
	
	progress['value'] = 95
	root.update_idletasks()
	
	#remove common modump
	os.remove(modump_path)
	print(f"{modump_path} has just been removed" )
	
	
	#remove logfiles.zip
	os.remove(logfiles_path)
	
	#remove amos script
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
					count += 1
	
	if count == 0 :
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
	progress['value'] = 100
	log_textbox.insert(tk.END, "\n" + "Decode DONE!!!"+"\n")
	root.update_idletasks()
def CurSelet(event):
	widget = event.widget
	
	all_items = widget.get(0, tk.END)
	sel_idx = widget.curselection()
	sel_list = [all_items[item] for item in sel_idx]
	print(sel_list)
	
	#thu cho show sel_list vao text box de test
	for dcgm_filename in sel_list:
		log_textbox.insert(tk.END, dcgm_filename)

def var_states():
	'''print state of selection box du_esi and ru_esi to terminal'''
	print("du_esi:", var1.get())
	print("ru_esi:", var2.get())
	#print("du_esi: %d,\ru_esi: %d" % (var1.get(), var2.get()))
def browse_button():
	global folder_path
	select_folder_path = filedialog.askdirectory()
	
	print(select_folder_path)
	folder_path.set(select_folder_path)
	
	#delete listbox
	dcgm_paths_listbox.delete(0, END)
	#update list box
	dcgm_filenames = [ file for file in os.listdir(select_folder_path) if os.path.isfile(os.path.join(select_folder_path, file)) and "_dcgm.zip" in file]
	for item in dcgm_filenames:
		dcgm_paths_listbox.insert(END, item)

root = tk.Tk()
#https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/
root.geometry("550x650")
#https://stackoverflow.com/questions/36575890/how-to-set-a-tkinter-window-to-a-constant-size/36575951
root.resizable(0, 0) #Don't allow resizing in the x or y direction


#set root_path to home folder, work for both window and linux
#https://stackoverflow.com/questions/13923079/tkinter-home-directory
root_path = os.path.expanduser('~')

button = tk.Button(root,text = "Select DCGM folder",command=browse_button).grid(row=0, column=0,sticky=W)

#default value to home folder
folder_path = StringVar(root, value=root_path)
lb1 = Label(root, textvariable = folder_path).grid(row=1, column=0, sticky=W)

#root_path_entry = tk.Entry(root, textvariable=default_dcgm_path, width=75).grid(row=2, column=0, sticky=W)

dcgm_paths_listbox = Listbox(root, width = 77, selectmode = tk.MULTIPLE)
dcgm_paths_listbox.bind('<<ListboxSelect>>',CurSelet)

dcgm_paths_listbox.grid(row=3, column=0, sticky=W)

log_textbox = Text(root, height=20, width=90)  #height = 20 row
log_textbox.grid(row=9, column=0, sticky=W)
#log_textbox.insert(tk.END, "Just a text Widget\nin two lines\n")


dcgm_filenames = [ file for file in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, file)) and "_dcgm.zip" in file]
for item in dcgm_filenames:
	dcgm_paths_listbox.insert(END, item)



# Progress bar widget , https://www.geeksforgeeks.org/progressbar-widget-in-tkinter-python/
progress = Progressbar(root, orient = HORIZONTAL,  length = 500, mode = 'determinate')
progress.grid(row=4, column=0, sticky=W)

#https://www.python-course.eu/tkinter_checkboxes.php
var1 = IntVar(value=1)  #default select for esi_du
var2 = IntVar()
du_checkbox = Checkbutton(root, text="DU ESI", variable=var1).grid(row=5, column=0, sticky=W)
#default select

ru_checkbox = Checkbutton(root, text="RU ESI", variable=var2).grid(row=6, column=0, sticky=W)
button = tk.Button(root,text = "Decrypt",command=descypt).grid(row=7, column=0,sticky=W)
button_quit = tk.Button(root,text = "Quit", command=quit).grid(row=8, column=0, sticky=W)


root.mainloop()