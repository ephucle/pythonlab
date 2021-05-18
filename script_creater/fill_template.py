#!/usr/bin/env python3
from string import Template

import pandas as pd
import os, sys, re

import tkinter as tk
from tkinter import filedialog, E, W, LEFT

#path of current script

#script_path = os.path.realpath(__file__)
#print(script_path)
home_path = os.path.dirname(os.path.realpath(__file__))
print(home_path)
#sys.exit()

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
	global input_file_path
	#global root_path
	#root_path = filedialog.askdirectory()
	input_file_path = filedialog.askopenfilename()
	print("button press!!")
	print(input_file_path)
	
	#update entry for input path
	text_var_inputpath.set(input_file_path)
	
	global sheet_options_list
	sheet_options_list = findallexcellsheet(input_file_path)
	#print(sheet_options_list)
	global om_var
	om_var.set('')
	sheet_select['menu'].delete(0, 'end')
	new_choices = sheet_options_list
	for choice in new_choices:
		sheet_select['menu'].add_command(label=choice, command=tk._setit(om_var, choice))



def browse_template_button():
	global template_filepath
	
	#root_path = filedialog.askdirectory()
	template_filepath = filedialog.askopenfilename()
	
	print("button press!!")
	print(template_filepath)
	
	
	#update entry for input path
	text_var_templatepath.set(template_filepath)
	
	

def fill_template():
	print("full template button press!!")
	text_var_status.set("RESET")
	global input_file_path, template_filepath  #bien nay duoc tao ra trong browse_button
	
	global selected_sheet #dung bien nay de reuse lai trong funtion folder tag
	selected_sheet = om_var.get()
	print("selected_sheet:", selected_sheet)
	global om_folder_var
	
	df = pd.read_excel(input_file_path, header=0, sheet_name=selected_sheet)
	print("SUMMARY DATA INPUT TABLE:")
	print(df)
	global column_header
	column_headers = list(df.columns.values)
	f = open(template_filepath, "r")
	input_file_content = f.read()
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
			regex = '\$' + "(\w+)"
			variables = re.findall(regex, line)
			print(variables)
			for item in variables:
				var_set.add(item)
		print("----------------all variable string--------------")
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
		rowname = "row"+str(index)
		src = Template(input_file_content)
		result = src.substitute(data)
		home_path = os.path.dirname(os.path.realpath(__file__))
		#output_filepath=os.path.join(home_path, "output_script", str(rowname))
		
		#split script follow folder
		if not var_foldersplit.get():
			output_filepath = os.path.join(home_path, "output_script",template_filename + "_" + rowname)
		else:
			#neu folder ko ton tai thi tao them folder
			if not os.path.exists(os.path.join(home_path, "output_script",row[folder_tag])):
				os.mkdir(os.path.join(home_path, "output_script",row[folder_tag]))
			
			#rule dat script name, co row, co template name
			output_filepath = os.path.join(home_path, "output_script",row[folder_tag], template_filename + "_" + rowname)
		output_text_file = open(output_filepath, "w")
		output_text_file.write(result)
		output_text_file.close()
		print("Successful create script", output_filepath)
		

	text_var_status.set("FINISHED!!!")


def folder_option_status_change():
	print("option_status_change")
	print(var_foldersplit.get())
	folder_split_select =  var_foldersplit.get()
	global input_file_path
	selected_sheet = om_var.get()
	df = pd.read_excel(input_file_path, header=0, sheet_name=selected_sheet)
	
	choices = list(df.columns.values)
	global om_folder_var
	#om_folder_var = tk.StringVar(root)
	#om_folder_var.set("Select tag")
	folder_select = tk.OptionMenu(root, om_folder_var, *choices)
	
	if folder_split_select:
		try:
			folder_select.grid(row=2, column=3, sticky="ew")
		except:
			text_var_status.set("Select Input file first")
	
root = tk.Tk()
root.title("SCRIPTING_TOOL_V01")
#root.geometry("550x550")





text_var_inputpath = tk.StringVar()
text_var_templatepath = tk.StringVar()
text_var_status = tk.StringVar()
text_var_status.set("STATUS: ")

global om_folder_var
om_folder_var = tk.StringVar(root)
om_folder_var.set("6.Select tag")

##row1
tk.Button(root, text ="01.EXCEL", command = browse_datainput_button).grid(row=0, column=1)
choices = ('select a sheet', '..')
om_var = tk.StringVar(root)
om_var.set("02.Select sheet")
sheet_select = tk.OptionMenu(root, om_var, *choices)
sheet_select.grid(row=0, column=2, sticky="ew")
##end row1

##row2
tk.Button(root, text ="03.TEMPL", command = browse_template_button).grid(row=1, column=1)
tk.Entry(root, textvariable = text_var_templatepath).grid(row=1, column=2, sticky="ew")
##end row2

#row3
var_foldersplit = tk.IntVar(value=0)
sector0_checkbox = tk.Checkbutton(root, text="04.FOLDER SPLIT", variable=var_foldersplit, command = folder_option_status_change).grid(row=2,sticky="w", column=2)


#end row 3

##row4
tk.Button(root, text ="05.CREATE",     command = fill_template).grid(row=3, column=1)
##end row4

##row5
tk.Label(root, textvariable =text_var_status,).grid(row=4, column=1, columnspan=2)
##end row5
root.mainloop()
