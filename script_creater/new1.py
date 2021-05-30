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
	df = df.rename(columns=lambda x: x.strip())
	
	#remove decription data in CIQ template if exit
	i = df[((df.Parameter == 'Area'))].index
	df= df.drop(i)
	#thay doi ":" bang dau ":"
	df.columns = df.columns.str.replace(r"[:]", "_")
	
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
			
			#####
			regex2 = '\$\{' + "(\w+)"+'\}'
			variables2 = re.findall(regex2, line)
			#print(variables2)
			for item in variables2:
				var_set.add(item)
			#####
			
			#####
			regex3 = '%' + "([\w:]+)"+'%' #cai tien co dau : ben trong variable
			variables3 = re.findall(regex3, line)
			#print(variables3)
			for item in variables3:
				var_set.add(item)
			#####
			
		print("----------------all variable string come to here--------------")
		print(var_set)  #{'smtcOffset', 'smtcPeriodicity', 'smtcDuration', 'smtcScs', 'arfcnValueNRDl', 'nRFrequencyId'}
		
	#####
	
	#update input_file_content (replace variable from %string% to ${string}
	regex = '%' + "([\w:]+)"+'%'  #update to support : inside variablename
	variables_percent = re.findall(regex, input_file_content)
	print("#######################################")
	print("variables_percent:",variables_percent)
	print("#######################################")

	for var in variables_percent:
		#print (var)
		new_var = var.replace(":","_")  #phai thay ":" bang "_" vi substitudte ko duoc
		print (new_var)
		#new_s = re.sub('%'+var+'%','${'+var+'}',input_file_content)
		new_s = re.sub('%'+var+'%','${'+new_var+'}',input_file_content)
		input_file_content = new_s

	#print(input_file_content), da test template new ok
	#with open('./output_script/temp_template.xml','w') as outfile:
	#	outfile.write(input_file_content)
	#sys.exit()
	
	for index, row in df.iterrows():
		data = {}
		for column_name in var_set:
			column_name = column_name.replace(":","_")  #remove ":" in column
			if column_name in column_headers:
				data[column_name] = row[column_name]
		print(data)
		

		
		rowname = filenametag_var.get()
		src = Template(input_file_content)
		if not data: #EMPTY or no vaiable
			result = input_file_content
		else:
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
			if not os.path.exists(os.path.join(home_path, "output_script",str(row[folder_tag]))):
				os.mkdir(os.path.join(home_path, "output_script",str(row[folder_tag])))
			output_filepath = os.path.join(home_path, "output_script",str(row[folder_tag]), templatename + "_" + str(row[rowname]) + "."+ ext)
		
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
