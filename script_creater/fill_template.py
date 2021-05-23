#!/usr/bin/env python3
from string import Template

import pandas as pd
import os, sys, re
import tkinter as tk
from tkinter import filedialog, E, W, LEFT

import json
import datetime
from myfunc import ls_name, get_filename, get_file_name_ext


version = "V04_20052023"
#version = "V04_20052023": support package profile, create script with many template as a sametime, create package profile

home_path = os.path.dirname(os.path.realpath(__file__))
print(home_path)

def get_now_stamp():
	'''
	#>>> get_now()
	#'20200514_094015'
	'''
	return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def findallexcellsheet(excel_filepath):
	'''
	return a list of sheet name
	>>> xl = pd.ExcelFile('input_cdd.xlsx')
	>>> xl.sheet_names
	['Sheet1', 'Sheet2', 'Sheet3']
	>>>
	'''
	xl = pd.ExcelFile(excel_filepath)
	return xl.sheet_names



#tim cach MAP tu dong variable sang column nhu MLC

def browse_datainput_button():
	status_label.configure(background=orig_color)
	
	global input_file_path
	#global root_path
	#root_path = filedialog.askdirectory()
	#filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
	input_file_path = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
	

	print("button press!!")
	print(input_file_path)
	
	#update entry for input path
	text_var_inputpath.set(input_file_path)
	
	global sheet_options_list
	sheet_options_list = findallexcellsheet(input_file_path)
	#print(sheet_options_list)
	
	########
	global om_var
	choices = sheet_options_list
	om_var = tk.StringVar(root)
	#om_var.set("02.Select sheet")
	#sheet_select = tk.OptionMenu(root, om_var, *choices)
	global sheet_select
	sheet_select = tk.OptionMenu(root, om_var, *choices,command=lambda _: sheet_select_command())

	sheet_select.grid(row=0, column=3, sticky="ew")
	########
	
	
	#update button label
	input_filename = get_filename(input_file_path)[:20]
	btn_browse_text.set(input_filename)
	browse_button.configure(bg = 'green2')
	text_var_status.set("SELECTED EXCEL FILE")
	foldersplit_checkbox.configure(state='normal')
	
	



def browse_template_button():
	global template_filepath
	
	#root_path = filedialog.askdirectory()
	template_filepath = filedialog.askopenfilename()
	
	print("button press!!")
	print(template_filepath)
	
	
	#update entry for input path
	text_var_templatepath.set(template_filepath)
	#change color after finished
	browse_template_button.configure(bg = 'green2')
	clear_textbox()
	with open(template_filepath) as infile:
		filecontent = infile.read()
		print_to_textbox(filecontent)
	entry_templatefilepath.configure(bg="green2")

def fill_template():

	create_button.configure(bg="yellow")
	print("full template button press!!")
	text_var_status.set("RESET")
	global input_file_path, template_filepath  #bien nay duoc tao ra trong browse_button
	
	#global selected_sheet #dung bien nay de reuse lai trong funtion folder tag
	selected_sheet = om_var.get()
	print("selected_sheet:", selected_sheet)
	global om_folder_var, filenametag_var
	
	df = pd.read_excel(input_file_path, header=0, sheet_name=selected_sheet)
	print("SUMMARY DATA INPUT TABLE:")
	print(df)
	global column_header
	column_headers = list(df.columns.values)
	f = open(template_filepath, "r")
	input_file_content = f.read()
	#global folder_tag
	folder_tag = om_folder_var.get()
	f.close()
	
	folder, template_filename = os.path.split(template_filepath)
	
	#####
	#find all variable in template
	with open(template_filepath) as infile:
		lines = infile.readlines()
		
		#find all variable string
		var_set = set()
		for index, line in enumerate(lines):
			line = line.strip()
			#doi voi truong hop thuong thi dung $variable
			regex = '\$' + "(\w+)"
			variables = re.findall(regex, line)
			
			
			
			#print(variables)
			for item in variables:
				var_set.add(item)
			
		print("----------------all variable string come to here--------------")
		print(var_set)  #{'smtcOffset', 'smtcPeriodicity', 'smtcDuration', 'smtcScs', 'arfcnValueNRDl', 'nRFrequencyId'}
		
	#####
	
	for index, row in df.iterrows():
		data = {}
		for column_name in var_set:
			if column_name in column_headers:
				#print(index,column_name,row[column_name])
				data[column_name] = row[column_name]
		print(data)
		#will turning later
		#rowname = "row"+str(index)
		
		rowname = filenametag_var.get()
		src = Template(input_file_content)
		result = src.substitute(data)
		home_path = os.path.dirname(os.path.realpath(__file__))
		#output_filepath=os.path.join(home_path, "output_script", str(rowname))
		
		#split script follow folder
		templatename, ext = get_file_name_ext(template_filename)
		print("str(row[rowname]", str(row[rowname]))
		if not var_foldersplit.get():
			#output_filepath = os.path.join(home_path, "output_script",template_filename + "_" + rowname)
			output_filepath = os.path.join(home_path, "output_script",templatename + "_" + str(row[rowname]) + "." + ext)
		else:
			#neu folder ko ton tai thi tao them folder
			if not os.path.exists(os.path.join(home_path, "output_script",row[folder_tag])):
				os.mkdir(os.path.join(home_path, "output_script",row[folder_tag]))
			output_filepath = os.path.join(home_path, "output_script",row[folder_tag], templatename + "_" + str(row[rowname]) + "."+ ext)
		
		global var_mergefile
		if var_mergefile.get():
			output_text_file = open(output_filepath, "a")
			
		else :
			output_text_file = open(output_filepath, "w")
		output_text_file.write(result)
		output_text_file.close()
		print("write successful", data, "to", output_filepath)
		
		

	text_var_status.set("FINISHED!!!")
	create_button.configure(bg="green2")
	status_label.configure(bg="green2")


def folder_option_status_change():
	print("option_status_change")
	print(var_foldersplit.get())
	folder_split_select =  var_foldersplit.get()
	global input_file_path
	global om_folder_var
	selected_sheet = om_var.get()
	df = pd.read_excel(input_file_path, header=0, sheet_name=selected_sheet)
	choices = list(df.columns.values)
	#create folder option menu
	folder_select = tk.OptionMenu(root, om_folder_var, *choices)
	if var_foldersplit.get():
		try:
			folder_select.grid(row=3, column=3, sticky="ew")
		except:
			text_var_status.set("Select Input file first")
	if not var_foldersplit.get():
		om_folder_var.set("")
	
	foldersplit_checkbox.configure(bg="green2")

def save_profile_press():
	global template_filepath,input_file_path,var_foldersplit,var_mergefile
	selected_sheet = om_var.get()
	folder_tag = om_folder_var.get()
	package_name = text_var_packagename.get()
	print("save_profile_press!!")
	#init a dict
	data = {}
	path,template_filename = os.path.split(template_filepath)
	profile_filename = template_filename + "_" + get_now_stamp()+".json" ##'20200514_094015'
	data['template_filepath'] = template_filepath
	data['input_file_path'] = input_file_path
	data['selected_sheet'] = selected_sheet
	data['folder_tag'] = folder_tag
	data['foldersplit']=var_foldersplit.get()
	data['filenametag'] = filenametag_var.get()
	data['mergefile'] = var_mergefile.get()
	
	print("data to be save as below")
	print(data)
	
	with open(os.path.join(home_path,'profile',profile_filename), 'w') as outfile:
		json.dump(data, outfile)
	#text_var_status.set("Save profile to "+ profile_filename)
	
	#####################
	data2 = {}
	path,template_filename = os.path.split(template_filepath)
	
	package_filename = package_name + ".json"
	package_filepath = os.path.join(home_path,'profile','profile_package',package_filename)
	data2['package_name'] = package_name
	
	#data2['profiles_filepath'] = [template_filename]
	
	
	print("package data to be save as below")
	print(data2)
	#neu file ko ton tai thi tao moi
	if not os.path.exists(package_filepath):
		data2['profiles_filepath'] = [template_filename]
		with open(package_filepath, 'w') as outfile:
			json.dump(data2, outfile)
	else: #neu file co ton tai
		with open(package_filepath) as json_file:
			data_dict = json.load(json_file)
			print(data_dict)
		#profile_package_name = data_dict['package_name']
		profiles_filepath = data_dict['profiles_filepath']
		if template_filepath not in profiles_filepath:
			profiles_filepath.append(template_filepath)
		
		data2['profiles_filepath'] = profiles_filepath
	#save new package profile or update it with new data
	with open(package_filepath, 'w') as outfile:
		json.dump(data2, outfile)
	text_var_status.set("Saved profile to: "+ profile_filename+" | Saved package to: "+ get_filename(package_filename))
	#####################
	
	#update option menu profile with new profile
	global om_profile_var
	om_profile_var.set('')
	profile_select['menu'].delete(0, 'end')
	profile_files = ls_name(os.path.join(home_path,'profile'))
	new_choices = profile_files
	for choice in new_choices:
		profile_select['menu'].add_command(label=choice, command=tk._setit(om_profile_var, choice))

def clear_textbox():
	log_textbox.delete("1.0","end")
def loadprofile():
	print("loadprofile press!!!")
	log_textbox.delete("1.0","end")
	#print profile name to text box
	print_to_textbox("profile selected:")
	profile_filename_selected = om_profile_var.get()
	print_to_textbox(profile_filename_selected)
	
	#open profile to load content, load back data to variable
	global home_path
	with open(os.path.join(home_path,"profile",profile_filename_selected)) as json_file:
		data_dict = json.load(json_file)
		print(data_dict)
		#print_to_textbox(str(data_dict))
		template_filepath = data_dict["template_filepath"]
		input_file_path = data_dict["input_file_path"]
		selected_sheet = data_dict["selected_sheet"]
		folder_tag = data_dict["folder_tag"]
		foldersplit = data_dict['foldersplit']
		filenametag = data_dict['filenametag']
		mergefile = data_dict['mergefile']
		
		print_to_textbox("Excel Input: "+get_filename(input_file_path))
		print_to_textbox("Sheet Name: "+selected_sheet)
		print_to_textbox("Template Input: "+get_filename(template_filepath))
		print_to_textbox("Folder_tag: "+folder_tag)
		print_to_textbox("foldersplit: "+str(foldersplit))
		print_to_textbox("filenametag: "+str(filenametag))
		print_to_textbox("mergefile: "+str(mergefile))
		
		print_to_textbox("-------------------------")
		
		input_filename = get_filename(input_file_path)[:20]
		btn_browse_text.set(input_filename)
		browse_button.configure(bg = 'green2')
	
	################
	#selected_sheet = om_var.get()
	print("selected_sheet:", selected_sheet)
	
	
	df = pd.read_excel(input_file_path, header=0, sheet_name=selected_sheet)
	print("SUMMARY DATA INPUT TABLE:")
	print(df)
	global column_header
	column_headers = list(df.columns.values)
	
	
	f = open(template_filepath, "r")
	input_file_content = f.read()
	
	f.close()
	
	folder, template_filename = os.path.split(template_filepath)
	
	#####
	#find all variable in template
	with open(template_filepath) as infile:
		lines = infile.readlines()
		
		#find all variable string
		var_set = set()
		for index, line in enumerate(lines):
			line = line.strip()
			regex = '\$' + "(\w+)"
			variables = re.findall(regex, line)

			for item in variables:
				var_set.add(item)
			
		print("----------------all variable string_from load profile--------------")
		print(var_set)  #{'smtcOffset', 'smtcPeriodicity', 'smtcDuration', 'smtcScs', 'arfcnValueNRDl', 'nRFrequencyId'}
		
	#####
	
	for index, row in df.iterrows():
		data = {}
		for column_name in var_set:
			if column_name in column_headers:
				#print(index,column_name,row[column_name])
				data[column_name] = row[column_name]
		print(data)
		#will turning later
		#rowname = "row"+str(index)
		rowname = filenametag
		
		src = Template(input_file_content)
		result = src.substitute(data)
		#home_path = os.path.dirname(os.path.realpath(__file__))
		#output_filepath=os.path.join(home_path, "output_script", str(rowname))
		
		#split script follow folder
		templatename, ext = get_file_name_ext(template_filename)
		if not foldersplit:
			#output_filepath = os.path.join(home_path, "output_script",template_filename + "_" + rowname)
			output_filepath = os.path.join(home_path, "output_script",templatename + "_" + str(row[rowname]) + "." + ext)
		else:
			#neu folder ko ton tai thi tao them folder
			if not os.path.exists(os.path.join(home_path, "output_script",str(row[folder_tag]))):
				os.mkdir(os.path.join(home_path, "output_script",row[folder_tag]))
			
			#rule dat script name, co row, co template name
			#output_filepath = os.path.join(home_path, "output_script",row[folder_tag], template_filename + "_" + rowname)
			output_filepath = os.path.join(home_path, "output_script",row[folder_tag], templatename + "_" + row[rowname] + "."+ ext)
		
		#if var_mergefile.get():
		if mergefile:
		
			output_text_file = open(output_filepath, "a")
		else :
			output_text_file = open(output_filepath, "w")
		output_text_file.write(result)
		output_text_file.close()
		print("write successful", data, "to", output_filepath)

		
		print_to_textbox("write successful script "+  output_filepath)
		

	text_var_status.set("FINISHED!!!")
	#create_button.configure(bg="green2")
	loadprofile_button.configure(bg="green2")
	status_label.configure(bg="green2")
	################

def print_to_textbox(text_string):
	'''this funtion help to add string to text box'''
	log_textbox.insert(tk.END, text_string + "\n")
	root.update_idletasks()

def show_profile_to_textbox():
	profile_filename_selected = om_profile_var.get()
	print(om_profile_var.get())
	print_to_textbox(om_profile_var.get())
	#open profile to load content, load back data to variable
	global home_path
	clear_textbox()
	with open(os.path.join(home_path,"profile",profile_filename_selected)) as json_file:
		data_dict = json.load(json_file)
		print(data_dict)
		
		template_filepath = data_dict["template_filepath"]
		input_file_path = data_dict["input_file_path"]
		selected_sheet = data_dict["selected_sheet"]
		folder_tag = data_dict["folder_tag"]
		foldersplit = data_dict['foldersplit']
		filenametag = data_dict['filenametag']
		mergefile = data_dict['mergefile']
		
		print_to_textbox("Excel Input: "+get_filename(input_file_path))
		print_to_textbox("Sheet Name: "+selected_sheet)
		print_to_textbox("Template Input: "+get_filename(template_filepath))
		print_to_textbox("Folder_tag: "+folder_tag)
		print_to_textbox("foldersplit: "+str(foldersplit))
		print_to_textbox("filenametag: "+str(filenametag))
		print_to_textbox("mergefile: "+str(mergefile))
		
		print_to_textbox("-------------------------")
	profile_select.configure(bg="green2")
	loadprofile_button.configure(state='normal')

def filenametag_select_command():
	print("filenametag_select_command selected !!")
	filenametag_select.configure(bg="green2")

def sheet_select_command():
	print("sheet_select_command selected!!!")
	sheet_select.configure(bg="green2")
	global input_file_path
	selected_sheet = om_var.get()
	df = pd.read_excel(input_file_path, header=0, sheet_name=selected_sheet)
	
	#create filename tag option menu
	choices = list(df.columns.values)
	global filenametag_select, filenametag_var
	filenametag_var = tk.StringVar(root)
	filenametag_var.set("04.FILENAME_TAG")
	filenametag_select = tk.OptionMenu(root, filenametag_var, *choices,command=lambda _: filenametag_select_command())
	filenametag_select.grid(row=2, column=2, sticky="ew", columnspan=1)
	#end create filename tag menu
	
	####create checkbox merge file, cung row voi filename tag
	global var_mergefile
	var_mergefile = tk.IntVar(value=1)
	mergefile = tk.Checkbutton(root, text="MERGE FILE", variable=var_mergefile, command = mergefile_option_status_change)
	mergefile.grid(row=2,sticky="w", column=3)
	####
	#chi enable nut create sau khi chon xong file excel bang nut brow, va select sheet
	create_button.configure(state='normal')

def mergefile_option_status_change():
	print("mergefile_option_status_change ticked !!")
	print(var_mergefile.get())


def show_profile_package_to_textbox():
	print("profile package option menu selected")
	profile_package_filename_selected = om_profile_package_var.get()
	print(profile_package_filename_selected)
	clear_textbox()
	print_to_textbox("Profile package selected: "+profile_package_filename_selected)
	#open profile to load content, load back data to variable
	global home_path
	
	with open(os.path.join(home_path,"profile","profile_package",profile_package_filename_selected)) as json_file:
		data_dict = json.load(json_file)
		print(data_dict)
		profile_package_name = data_dict['package_name']
		profiles_filepath = data_dict['profiles_filepath']
		print(profile_package_name)
		print(profiles_filepath)
		print_to_textbox("profile_package_name "+profile_package_name)
		
		print_to_textbox("-----------------------------------------")
		print_to_textbox("profile_filepaths: ")
		for profile_filepath in profiles_filepath:
			#print_to_textbox(profile_filepath)
			print_to_textbox(get_filename(profile_filepath))

	profile_package_select.configure(bg="green2")
	text_var_status.set("STATUS: PACKAGE SELECTED")
	loadprofile_package_button.configure(state='normal')


def loadprofile_procedure(profile_filepath):
	print("creating script for profile", profile_filepath)
	#log_textbox.delete("1.0","end")
	#print profile name to text box
	print_to_textbox("creating script for profile:" + profile_filepath)
	with open(profile_filepath) as json_file:
		data_dict = json.load(json_file)
		print(data_dict)
		template_filepath = data_dict["template_filepath"]
		input_file_path = data_dict["input_file_path"]
		selected_sheet = data_dict["selected_sheet"]
		folder_tag = data_dict["folder_tag"]
		foldersplit = data_dict['foldersplit']
		filenametag = data_dict['filenametag']
		mergefile = data_dict['mergefile']
		
		print_to_textbox("Excel Input: "+get_filename(input_file_path))
		print_to_textbox("Sheet Name: "+selected_sheet)
		print_to_textbox("Template Input: "+get_filename(template_filepath))
		print_to_textbox("Folder_tag: "+folder_tag)
		print_to_textbox("foldersplit: "+str(foldersplit))
		print_to_textbox("filenametag: "+str(filenametag))
		print_to_textbox("mergefile: "+str(mergefile))
		print_to_textbox("-------------------------")
		
		input_filename = get_filename(input_file_path)[:20]
	
	
	print("selected_sheet:", selected_sheet)
	df = pd.read_excel(input_file_path, header=0, sheet_name=selected_sheet)
	print("SUMMARY DATA INPUT TABLE:")
	print(df)
	global column_header
	column_headers = list(df.columns.values)
	
	
	f = open(template_filepath, "r")
	input_file_content = f.read()
	
	f.close()
	
	folder, template_filename = os.path.split(template_filepath)
	
	#find all variable in template
	with open(template_filepath) as infile:
		lines = infile.readlines()
		
		#find all variable string
		var_set = set()
		for index, line in enumerate(lines):
			line = line.strip()
			regex = '\$' + "(\w+)"
			variables = re.findall(regex, line)

			for item in variables:
				var_set.add(item)
			
		print("----------------all variable string_from load profile--------------")
		print(var_set)

	#substitute data from each row of excel into to template
	for index, row in df.iterrows():
		data = {}
		for column_name in var_set:
			if column_name in column_headers:
				#print(index,column_name,row[column_name])
				data[column_name] = row[column_name]
		print(data)
		rowname = filenametag
		
		src = Template(input_file_content)
		result = src.substitute(data)

		#split script follow folder
		templatename, ext = get_file_name_ext(template_filename)
		if not foldersplit:
			output_filepath = os.path.join(home_path, "output_script",templatename + "_" + str(row[rowname]) + "." + ext)
		else:
			#neu folder ko ton tai thi tao them folder
			if not os.path.exists(os.path.join(home_path, "output_script",str(row[folder_tag]))):
				os.mkdir(os.path.join(home_path, "output_script",row[folder_tag]))
			
			#rule dat script name, co row, co template name
			output_filepath = os.path.join(home_path, "output_script",row[folder_tag], templatename + "_" + row[rowname] + "."+ ext)
		
		if mergefile:
			output_text_file = open(output_filepath, "a")
		else :
			output_text_file = open(output_filepath, "w")
		output_text_file.write(result)
		output_text_file.close()
		print("write successful", data, "to", output_filepath)
		print_to_textbox("write successful script "+  output_filepath)

#########################

def loadprofile_package():
	#cho vang cai nut de biet la bat dau ==> de troubleshooting
	loadprofile_package_button.configure(bg = 'yellow')
	print("loadprofile_package button press!!")
	profile_package_filename_selected = om_profile_package_var.get()
	print(profile_package_filename_selected)
	clear_textbox()
	print_to_textbox("Profile package selected: "+profile_package_filename_selected)
	#open profile to load content, load back data to variable
	global home_path
	
	with open(os.path.join(home_path,"profile","profile_package",profile_package_filename_selected)) as json_file:
		data_dict = json.load(json_file)
		print(data_dict)
		profile_package_name = data_dict['package_name']
		profiles_filepath = data_dict['profiles_filepath']
		print(profile_package_name)
		print(profiles_filepath)
		print_to_textbox("profile_package_name "+profile_package_name)
		print_to_textbox("-----------------------------------------")
		print_to_textbox("profile_filepaths: ")
		for profile_filepath in profiles_filepath:
			print_to_textbox(profile_filepath)
			loadprofile_procedure(profile_filepath)
	
	#cho xanh cai nut , de biet la chay thanh cong
	loadprofile_package_button.configure(bg = 'green2')

root = tk.Tk()
root.title("SCRIPTING_"+version)
#root.geometry("550x550")





text_var_inputpath = tk.StringVar()
text_var_templatepath = tk.StringVar()
text_var_status = tk.StringVar()
text_var_status.set("STATUS: PLS SELECT EXCEL OR CHOOSE PROFILE")
text_var_packagename = tk.StringVar()

global om_folder_var
om_folder_var = tk.StringVar(root)
#om_folder_var.set("6.Select tag")
om_folder_var.set("")

##row1
btn_browse_text = tk.StringVar()
btn_browse_text.set("01.EXCEL")
browse_button = tk.Button(root, textvariable=btn_browse_text, command = browse_datainput_button)
browse_button.grid(row=0, column=0, columnspan=3, sticky="ew")
orig_color = browse_button.cget("background")  #to help reset color

#folder tag duoc tao dong sau select excel file
###end row1

##row2
browse_template_button= tk.Button(root, text ="03.TEMPL", command = browse_template_button)
browse_template_button.grid(row=1, column=1)
entry_templatefilepath = tk.Entry(root, textvariable = text_var_templatepath)
entry_templatefilepath.grid(row=1, column=2, sticky="ew", columnspan=2)
##end row2

#row3

#row3, filename tag duoc tao ra dong, sau khi select sheet
#endrow3

#row4
var_foldersplit = tk.IntVar(value=0)
foldersplit_checkbox = tk.Checkbutton(root, text="05.FOLDER SPLIT", variable=var_foldersplit, command = folder_option_status_change)
foldersplit_checkbox.grid(row=3,sticky="w", column=2)

foldersplit_checkbox.configure(state='disabled')
#end row 4

##row5
create_button= tk.Button(root, text ="05.CREATE",     command = fill_template)
create_button.grid(row=4, column=1)
create_button.configure(state='disabled')
##end row5

##row6
tk.Button(root, text ="06.BACKUP",     command = save_profile_press).grid(row=5, column=1)

tk.Label(root, text="package_name").grid(row=5, column=2, sticky="w")
entry_packagename = tk.Entry(root, textvariable = text_var_packagename)
entry_packagename.grid(row=5, column=2, sticky="e")
##end row6

##row7
profile_files = ls_name(os.path.join(home_path,'profile'))
choices = profile_files
om_profile_var = tk.StringVar(root)
om_profile_var.set("07.Select a profile")
#profile_select = tk.OptionMenu(root, om_profile_var, *choices)
profile_select = tk.OptionMenu(root, om_profile_var, *choices,command=lambda _: show_profile_to_textbox())
#mymenu = OptionMenu(root, optionvar, *t, command=lambda _: update())
profile_select.grid(row=6, column=2, sticky="ew", columnspan=2)
#end row7

##row8
profile_package_files = ls_name(os.path.join(home_path,'profile','profile_package'))
choices = profile_package_files
om_profile_package_var = tk.StringVar(root)
om_profile_package_var.set("07_1.Select a profile package")
profile_package_select = tk.OptionMenu(root, om_profile_package_var, *choices,command=lambda _: show_profile_package_to_textbox())
#mymenu = OptionMenu(root, optionvar, *t, command=lambda _: update())
profile_package_select.grid(row=7, column=2, sticky="ew", columnspan=2)
#end row8

#row9
log_textbox = tk.Text(root, height=15)
log_textbox.grid(row=8, column=2, sticky="ew",columnspan=2)
#end row9

#row10
loadprofile_button= tk.Button(root, text ="08.LOAD PROFILE & CREATE SCRIPT",     command = loadprofile)
loadprofile_button.grid(row=9, column=2, sticky="ew", columnspan=2)
loadprofile_button.configure(state='disabled')
#end row10

#row11
loadprofile_package_button= tk.Button(root, text ="08_1.LOAD PROFILE PACKAGE & CREATE SCRIPT",     command = loadprofile_package)
loadprofile_package_button.grid(row=10, column=2, sticky="ew", columnspan=2)
loadprofile_package_button.configure(state='disabled')


#end row11

##row12
status_label = tk.Label(root, textvariable =text_var_status,)
status_label.grid(row=11, column=1, columnspan=3)
##end row12



root.mainloop()
