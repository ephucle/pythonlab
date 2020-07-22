#!/usr/bin/env python3
import resource
import os
import re
from timeit import default_timer as timer
#version 1.1, 20200407_1645 
#go to line 123 by g123 or l123
#co gang thiet ke theo kieu function, va call

#version 1.2, 20200412_1503
#replace re.search by re.match to speed up big file handling


def less_file (file_path):
	''' read file like less command in linux'''
	os.system('clear')
	
	# vi read 2 file nr va enb, nen dung dong nay de phan biet
	
	print ("READING" ,file_path, "...")
	print(f'>>> File Size is {os.stat(file_path).st_size / (1024 * 1024)} MB')

	txt_file = open(file_path, encoding = "ISO-8859-1")
	
	#tim so line cua file
	
	for i, line in enumerate(txt_file):
		pass
	print (">>> Total lines:",i + 1)
	txt_file.close()
	
	#open again, dirty code
	txt_file = open(file_path, encoding = "ISO-8859-1")
	
	line_no = 0 
	while(1):
	
		#moi lan co user input khac s/S thi in them 30 dong
		for i in range(30):
			
			line = txt_file.readline()
			line_no += 1
			print(line_no, line.strip())
		user_input = input('Press input, [Enter ==> read more | g456 or l456 ==> go to line 456 | Press s/S/q ==> Exit] >>>')
		m = re.match('[lg](\d+)', user_input)
		if user_input == 's' or user_input == 'S' or user_input == 'q':
			txt_file.close()
			break
		elif m:
			target_line = int(m.group(1))
			go2line_file(file_path, target_line)
			break
		else:
			pass



def go2line_file(file_path, line_no):

	'''funtion: print 150 line from line_no'''

	txt_file = open(file_path, encoding = "ISO-8859-1")
	
	#chi doc 150 dong tu dong duoc chi dinh, thu tu line: line dau tien la line 1
	
	#them dong --- de cho de doc
	print ("-"*60)
	for i, line in enumerate(txt_file):
		#if i >= line_no and i < line_no + 200:
		if line_no - 1 <= i < line_no + 150:
			print(i+1, line.strip())



def merge_two_file(filenames):
	#https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/
	# Python program to 
	# demonstrate merging of 
	# two files 
	  
	# Creating a list of filenames 
	#filenames = ['file1.txt', 'file2.txt'] 
  
	# Open file3 in write mode 
	target_file_path = '/mnt/c/working/02-Project/16-SKT_5G_Project/07-Databases/03-MHWEB/combine_file.txt'
	with open(target_file_path, 'w', encoding = "ISO-8859-1") as outfile: 

		# Iterate through list 
		for names in filenames: 

			# Open each file in read mode 
			with open(names, encoding = "ISO-8859-1") as infile: 

				# read the data from file1 and 
				# file2 and write it in file3 
				outfile.write(infile.read()) 
	  
			# Add '\n' to enter data of file2 
			# from next line 
			outfile.write("\n")
	return target_file_path

def picklines(file_path, line_no, width):
	'''
	lay truoc do width dong va sau do width dong
	 return list of tube :  [(line_index, line_content)...]
	 '''
	result = []
	whatlines = list(range(line_no - width, line_no + width))
	with open(file_path, encoding = "ISO-8859-1") as thefile:
		
		#return [(i+1, x) for i, x in enumerate(thefile) if i in whatlines]
		for i, x in enumerate(thefile):
			if i in whatlines:
				result.append((i+1,x))
			if i > line_no + width:
				#save time, no need to scan all big file  ==> cai tien dang ke 20s ve 0.2s
				break
	return result
			

def pick_first_tr(tr_id, file_path):
	'''
	print first TR found in MHWEB offline file
	return list of line of tr content
	'''
	thefile = open(file_path, encoding = "ISO-8859-1")
	for i, line in enumerate(thefile):
		pass
	total_line = i+1
	
	
	found_first_line = False
	with open(file_path, encoding = "ISO-8859-1") as thefile:
		for i, line in enumerate(thefile):
			#print de biet toi line nao
			if i%3400000 == 0:
				print ('Reading until position:', int(100*(i/total_line)), '%')
			
			line = line.strip()
			#<value>HY29889</value></column>
			match_string = '<value>' + tr_id + '</value></column>'
			#m = re.search(match_string, line)
			m = re.match(match_string, line)
			if m and found_first_line == False:
				first_line_index = i - 1
				first_line = line
				found_first_line = True
			
			
				
			
			#khong co cai nao dung???
			pat = r'<value>'  + r'[a-zA-Z]{2}[0-9]{5}' + r'</value></column>'
			m1 = re.match(pat, line)
			
			
			if m1 and found_first_line == True and i > first_line_index +1 :
				second_line_index = i-2
				break
	
	
	#print (first_line_index, second_line_index)
	#print line from first_line_index to second_line_index
	tr_content=[]
	if found_first_line:
		with open(file_path, encoding = "ISO-8859-1") as thefile:
			for i, line in enumerate(thefile):
				if i >= first_line_index and i <=second_line_index:
					#print(i+1 ,line.strip())
					tr_content.append(line.strip())
				if i > second_line_index:
					thefile.close()
					break
	else:
		print ("no_content_found")
				
	return tr_content
		
	
def main():
	
	file_path = "/mnt/c/working/02-Project/16-SKT_5G_Project/07-Databases/03-MHWEB/combine_file.txt"
	#less_file(file_path)
	
	#go2line_file(file_path,2000)
	
	#test picklines function
	
	start = timer()
	
	
	#pick_first_tr('HY29889' , file_path)
	
	#pick_first_tr('HY29946' , file_path)
	pick_first_tr('HY11944' , file_path)
	
	
	end = timer()
	duration = end - start
	print ("duration:", duration)
	
		
		
if __name__ == "__main__":
	main()