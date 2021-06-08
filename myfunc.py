#!/usr/bin/env python3
#my mini func, to reuse everywhere which I need. Save time, save my memory. No need to remember anything
import re, os, sys
import time
import datetime
import subprocess
from collections import Counter
import platform
# timer.py
#https://realpython.com/python-timer/
class TimerError(Exception):
	"""A custom exception used to report errors in use of Timer class"""

class Timer:
	'''
	#example how to use:
	#>>> t =Timer()
	#>>> t.start()
	#>>> t.stop()
	#>>> Elapsed time: 10.0668 seconds  [00:00:10]
	'''
	def __init__(self):
		self._start_time = None

	def start(self):
		"""Start a new timer"""
		if self._start_time is not None:
			raise TimerError("Timer is running. Use .stop() to stop it")
			

		self._start_time = time.perf_counter()
		print(">>> The action start at:", get_now())

	def stop(self):
		"""Stop the timer, and report the elapsed time"""
		if self._start_time is None:
			raise TimerError("Timer is not running. Use .start() to start it")

		elapsed_time = time.perf_counter() - self._start_time
		seconds = elapsed_time % (24 * 3600) 
		hour = seconds // 3600
		seconds %= 3600
		minutes = seconds // 60
		seconds %= 60
		
		self._start_time = None
		#print(f">>> Elapsed time: {elapsed_time:0.4f} seconds")
		print(">>> Elapsed time: %0.4f seconds  [%02d:%02d:%02d]" % (elapsed_time,hour, minutes, seconds))


def call_moshell(dcgm_path):
	'''
	from myfunc import call_moshell
	dcgm_path = '/mnt/c/cygwin/home/ephucle/moshell_logfiles/logs_moshell/dcg/gHIL2861/210531_112344/gHIL2861_modump.zip'
	call_moshell(dcgm_path)
	ephucle@VN-00000267:/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab$ python3 test_call_moshell_func.py
	Start moshell to  /mnt/c/cygwin/home/ephucle/moshell_logfiles/logs_moshell/dcg/gHIL2861/210531_112344/gHIL2861_modump.zip
	
	#####################################################################
	#            Welcome to MoShell 21.0f (LPA108514/1_R21F)            #
	#                Finn Magnusson, Jan Pettersson                     #
	#           http://newtran01.au.ao.ericsson.se/moshell              #
	#            Contact: Finn.Magnusson@ericsson.com                   #
	#                     Joakim.xo.Ostlund@ericsson.com                #
	#####################################################################
		Copyright (c) Ericsson AB 2001-2021 - All Rights Reserved
	'''
	moshell_path = subprocess.getoutput('which moshell')
	full_script = moshell_path + " " + dcgm_path
	print ("Start moshell to ", dcgm_path)
	call(full_script)

def get_filename(filepath):
	path, filename = os.path.split(filepath)
	return filename

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


	
def get_file_name_ext(filepath):
	'''
	#get_file_name_ext()
	>>> name, ext = get_file_name_ext('./folder/helloworld.txt')
	>>> print(name, ext)
	helloworld txt
	'''
	path, filename = os.path.split(filepath)
	allitem = filename.split(".")
	ext = allitem[-1]
	name = filename[:len(filename)-len(ext)-1]
	return name, ext

def get_today():
	'''
	#>>> get_today()
	#'2020-05-14'
	'''
	return datetime.date.today().strftime("%Y-%m-%d")

def get_now():
	'''
	#>>> get_now()
	#'2020-06-26 08:18:43.147639'
	#Using %f with strftime() in Python to get microseconds
	
	'''
	#return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

def get_now_stamp():
	'''
	#>>> get_now()
	#'20200514_094015'
	'''
	return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def cut_left(cutter, text):
	'''
	>>> cut_left(" and ", "Left and Right")
	'Left'
	'''
	list1 = re.split(cutter, text)
	left_text  = list1[0]
	return left_text

def cut_right(cutter, text):
	'''
	>>> cut_right(" : ", "Left : Right Text")
	'Right Text'
	'''
	list1 = re.split(cutter, text)
	right_text  = list1[1]
	return right_text

def cut_mid(cutter_left, cutter_right, text):
	'''
	>>> cut_mid("@ ", " :", " something @ Target Text : anything")
	'Target Text'
	'''
	text1 = cut_right(cutter_left, text)
	text2 = cut_left(cutter_right, text1)
	return text2
	
def rm_duplicate_and_count(list_of_string):
	'''
	>>> rm_duplicate_and_count(['text1', 'text2', 'text3', 'text1', 'text2', 'text2', 'text4', 'text3', 'text2', 'text3'])
	[('text2', 4), ('text3', 3), ('text1', 2), ('text4', 1)]
	'''
	dict_result = {}
	
	set_of_item = set()
	
	for item in list_of_string:
		set_of_item.add(item)
	#khoi tao gia tri
	for item in set_of_item:
		dict_result[item] = 0
	
	for item in list_of_string:
		dict_result[item] += 1
	
	list_of_tube = list(dict_result.items())
	
	#sort by count
	#list_of_tube2 = sorted(list_of_tube, key=lambda x: x[1], reverse=True)
	
	list_of_tube.sort(reverse=True, key=lambda x: x[1])

	return list_of_tube


def remove_duplicated_item_in_list(list_of_item):
	#this function is using for new_crash tool, pls dont remove
	list_after_remove_duplicated  = list(dict.fromkeys(list_of_item))
	return list_after_remove_duplicated

def cut_lines(first_line, second_line, text):
	result_text = ''
	lines = re.split("\n", text)
	
	#find start line, and end line index
	for i, line in enumerate(lines):
		#print (i, line)
		if re.search(first_line, line):
			first_line_index = i
		if re.search(second_line, line) and i > first_line_index :
			second_line_index = i
			break
	#get line content
	for i, line in enumerate(lines):
		if first_line_index <= i <= second_line_index:
			result_text += line+"\n"
	
	return result_text

def ls(folder_path):
	'''
	>>> ls('/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab/test_dir')
	['/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab/test_dir/file1', '/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab/test_dir/file2', '/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab/test_dir/file3', '/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab/test_dir/1/file11', '/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab/test_dir/1/file12', '/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab/test_dir/2/file21', '/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab/test_dir/2/file210', '/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab/test_dir/3/file31', '/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab/test_dir/3/file33']

	
	'''
	filepaths = []
	for path, subdirs, files in os.walk(folder_path):
		for name in files:
			if "~$" not in name:
				filepaths.append(os.path.join(path,name))
	sorted(filepaths)
	#sort theo ngay thang modify, cai moi nhat cho len dau
	#sorted(filepaths, key=lambda t: os.stat(t).st_mtime, reverse=True)
	
	return filepaths



def ls_name(folder_path, e=""):
	'''
	e = except_filter_folder 
	get of file name of a folder
	sort file by decent modify time, newest file on the first
	'''
	filenames = []
	filepaths = []
	if e == "":
		for path, subdirs, files in os.walk(folder_path):
			for name in files:
				if "~$" not in name:
					filepaths.append(os.path.join(path,name))
					#filenames.append(name)
		#sorted(filenames)
		
		sorted_by_mtime_ascending = sorted(filepaths, key=lambda t: os.stat(t).st_mtime, reverse=True)
		for filepath in sorted_by_mtime_ascending:
			filenames.append(get_filename(filepath))
		return filenames
	else:
		for path, subdirs, files in os.walk(folder_path):
			for name in files:
				if "~$" not in name and e not in path:
					filepaths.append(os.path.join(path,name))
					#filenames.append(name)
		sorted_by_mtime_ascending = sorted(filepaths, key=lambda t: os.stat(t).st_mtime, reverse=True)
		for filepath in sorted_by_mtime_ascending:
			filenames.append(get_filename(filepath))
		return filenames





def split_llog(file_path, cutter1, cutter2):
	'''
	return list of llog
	
	
	'''
	#cutter1 = "No:\s+"
	#cutter2 = "Extra:\s+"
	
	result = []
	lines = [line.rstrip() for line in open(file_path)]
	start = 0
	
	total_line = len(lines)
	line_index = 0
	while line_index <= total_line:
		#use this variable to scan all file
		line_index += 1
		for i,line in enumerate(lines):
			#m1 = re.search("No:\s+",line)
			m1 = re.search(cutter1,line)
			if m1 and i > start:
				first_tag = i
			#m2 = re.search('Extra:\s+',line)
			m2 = re.search(cutter2,line)
			if m2 and i > first_tag and i > start:
				second_tag = i
				llog_detail = ""
				for j,linex in enumerate(lines):
					if first_tag  <= j <=  second_tag:
						llog_detail += linex+"\n"
					if j > second_tag:
						break
				result.append(llog_detail)
				start = i+1
				break
	
	#print (result)
	#print("No of llog found:", len(result))
	return result
	

def split_llog2(file_path, cutter1="No:\s+", cutter2="Extra:\s+"):
	'''
	return list of llog
	
	
	'''
	#cutter1 = "No:\s+"
	#cutter2 = "Extra:\s+"
	
	result = []
	lines = [line.rstrip() for line in open(file_path)]
	start = 0
	
	total_line = len(lines)
	line_index = 0
	while line_index <= total_line:
		#use this variable to scan all file
		line_index += 1
		for i,line in enumerate(lines):
			#m1 = re.search("No:\s+",line)
			m1 = re.search(cutter1,line)
			if m1 and i > start:
				first_tag = i
			#m2 = re.search('Extra:\s+',line)
			m2 = re.search(cutter2,line)
			if m2 and i > first_tag and i > start:
				second_tag = i
				llog_detail = ""
				for j,linex in enumerate(lines):
					if first_tag  <= j <=  second_tag:
						llog_detail += linex+"\n"
					if j > second_tag:
						break
				#result.append(llog_detail)
				yield llog_detail
				start = i+1
				break
	return result

def check_if_text_in_file(text, file_path):
	'''
	#>>> check_if_text_in_file('HY42864','./log/tr.txt')
	#True
	#>>> check_if_text_in_file('HY42865','./log/tr.txt')
	#False
	#>>>
	'''
	found = False
	with open(file_path, encoding = "ISO-8859-1") as thefile:
		for i, line in enumerate(thefile):
			m = re.search(text, line)
			if m:
				found = True
				break
		return found

def remove_duplicate_and_count(list_of_item):
	'''
	>> remove_duplicate_and_count([1,2,3, 1,2,3])
	[(1, 2), (2, 2), (3, 2)]
	>>> remove_duplicate_and_count('aabbbcccddd')
	[('b', 3), ('c', 3), ('d', 3), ('a', 2)]
	'''
	c = Counter(list_of_item)
	return c.most_common()



def pwd():
	return os.getcwd()


def cd(path):
	'''
	https://thispointer.com/how-to-change-current-working-directory-in-python/
	>>> pwd()
	'/mnt/c/cygwin/home/ephucle/tool_script/python/tr_tool'
	>>> cd('/mnt/c/cygwin/home/ephucle/tool_script/python/')
	'''
	os.chdir(path)


def ll():
	'''
	tu dong sap xep theo thu tu thoi gian, file cu nhat o hang duoi cung

	'''

	subprocess.run(["ls", "-ltr"])

def date():
	'''
	#>>> date()
	#'2020-05-26 10:16:17'
	#>>> date()
	#'2020-05-26 10:16:22'
	#>>> date()
	#'2020-05-26 10:16:23'
	'''
	return get_now()

def cat(filepath):
	'''
	#example:
	#>>> cat('swmapping.txt')

	'''
	with open(filepath) as infile:
		for i, line in enumerate(infile):
			print (line.strip())

def less(filepath):
	'''
	DESCRIPTION
	Using linux less to read the file
	'''
	call('less '+ filepath)

def search(text):
	'''
	search all text in CURRENT working FOLDER, all sub folder, print text and file path
	using this function to search source code quickly from python terminal
	HELP to search source code in current working folder quickly. save time to look up source code
	'''
	filepaths = ls('./')
	
	#filename ma co chua cac patten ben duoi thi khong can xu ly
	filter_pattern = '(pyc|xlsx|zip|mhweb_data.csv)'
	
	for filepath in filepaths:
		#ko search cac file ko phai la file text
		#if "pyc" not in filepath and "xlsx" not in filepath and "zip" not in filepath and "mhweb_data.csv" not in filepath :
		if not re.search(filter_pattern, filepath):
			with open(filepath, encoding='ISO-8859-1') as infile:
				for i, line in enumerate(infile):
					#line = line.decode('utf-8','ignore').encode("utf-8")
					#khong phan biet chu hoa, chu thuong
					if re.search(text,line, re.IGNORECASE):
						print(filepath,line.strip())

def call(cmd):
	'''
	#call linux shell command by os.system
	#>>> call('ls -l | wc')
	#
	#>>> call('date')
	#Wed May 27 08:39:03 DST 2020
	#
	#>>> call('pwd')
	#/mnt/c/cygwin/home/ephucle/tool_script/python


	'''
	os.system(cmd)

def callpy(python_file_path):
	'''
	>>> callpy('test_global_scope.py')
	3 [44, 2, 3]
	'''
	cmd = "python " + python_file_path
	os.system(cmd)
	

def nano(filepath):
	'''
	edit text file by nano tool of linux
	nano('test.txt')
	'''
	call('nano '+ filepath)

def have_special_character(string):
	'''
	>>> have_special_character('"')
	False
	>>> have_special_character('&')
	True
	>>> have_special_character('>')
	True
	>>> have_special_character('?')
	True
	>>> have_special_character(')')
	True
	>>> have_special_character('(')
	True
	>>> have_special_character('#')
	True
	>>> have_special_character('"')
	False
	'''
	# Make own character set and pass  
	# this as argument in compile method 
	regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 

	# Pass the string in search  
	# method of regex object.     
	if(regex.search(string) == None): 
		return False
	else: 
		return True

def rm_special_characters(string):
	'''
	#for some special case, need to remove special character from string, link df = .str.contains(sign_regex)]
	#https://stackoverflow.com/questions/23996118/replace-special-characters-in-a-string-python/23996414
	special chacacter: !@#$%^&*()[]{};:,./<>?\|`~-=_+
	>>> rm_special_characters("#123")
	'.123'
	>>> rm_special_characters("()")
	'..'
	>>> rm_special_characters("[text]")
	'.text.'
	>>> rm_special_characters("<html>head<\html>")
	'.html.head..html.'
	'''
	string = string.translate ({ord(c): "." for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
	return string

def main():
	#https://docs.python.org/3/library/doctest.html
	import doctest
	doctest.testmod()

def _func_filter_2020_crash(text):
	if "ENDC_DU_Crash_Alarm_PKG_Daily_Report_2020" in text:
		return True
	else:
		return False

def get_latest_crash_report_filename():
	'''
	get_latest_crash_report_filename()
	'ENDC_DU_Crash_Alarm_PKG_Daily_Report_20200629.xlsx'
	'''
	all_crash_report_file = ls('/mnt/c/working/02-Project/16-SKT_5G_Project/06-ProjectTasks/03-DailyReport')
	all_crash_report_file = list(filter(_func_filter_2020_crash,all_crash_report_file))
	latest_crash_report_file = all_crash_report_file[-1]
	filepath, filename = os.path.split(latest_crash_report_file)
	return filename

def get_latest_trmapping_filepath():
	'''
	auto choose latest tr mapping file
	>>> get_latest_trmapping_filepath()
	'/mnt/c/working/02-Project/16-SKT_5G_Project/06-ProjectTasks/00_TRMappingTool/SKT_5G_CD_Crash_Report_Tool_PA9_9_66.xlsm'
	'''
	all_tr_mapping_file = ls('/mnt/c/working/02-Project/16-SKT_5G_Project/06-ProjectTasks/00_TRMappingTool/')
	latest_tr_mapping_filepath = all_tr_mapping_file[-1]
	return latest_tr_mapping_filepath

def walk(dirname):
    '''
    >>> walk('./test')
    ./test/folder1/file1.txt
    ./test/folder1/file2.txt
    ./test/folder1/folder1_sub/file7.txt
    ./test/folder1/folder1_sub/file8.txt
    ./test/folder2/file3.txt
    ./test/folder2/file4.txt
    ./test/helloworld.py2
    ./test/helloworld.py3
    ./test/tmp.txt
    >>>
    '''
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print (path)
        else:
            walk(path)


def get_parameters(object):
	return object.__dict__
def get_methods(object):
	method_list = [func for func in dir(object) if callable(getattr(object, func))]
	return method_list


def __parse_mounts():
    """ Return a map of Windows roots to their corresponding Linux root and a
        map of Linux roots to their corresponding Windows root.

        >>> linux_roots, windows_roots = parse_mounts()
        >>> linux_roots["C:"]
        '/mnt/c'
        >>> windows_roots["/mnt/c"]
        'C:'
    """
    # Map a Windows root to a Linux root
    linux_roots = {}
    # Map a Linux root to a Windows root
    windows_roots = {}
    
    with open("/proc/mounts", "rb") as fd:
        for line in fd.read().splitlines():
            source, target, type_, _ = line.split(b" ", 3)
            
            if type_ != b"drvfs":
                continue
            
            # Decode the string (backslash-escaped octal values)
            source = source.decode("unicode-escape")
            # If the root is a fully qualified drive letter, remove the final "\"
            source = re.sub(r"^([a-zA-Z]:)(\\$)", r"\1", source)
            
            target = target.decode("unicode-escape")
            
            linux_roots[source] = target
            windows_roots[target] = source

    return linux_roots, windows_roots

def __find_root(roots, path, separator):
    """ Return the root matching the given path followed by a separator. """

    candidates = [
        x for x in roots
        if path == x or path.startswith("{}{}".format(x, separator))]
    if not candidates:
        raise Exception("No root found for {}".format(path))
    elif len(candidates) > 1:
        raise Exception("Multiple roots found for {}".format(path))

    return candidates[0]

def convert_w(linux_path):
    """ Convert a Linux path to a Windows path. 
    >>> convert_w('/mnt/c/working/02-Project/16-SKT_5G_Project/07-Databases/03-MHWEB/combine_file.txt')
    'C:\\working\\02-Project\\16-SKT_5G_Project\\07-Databases\\03-MHWEB\\combine_file.txt'
    >>> convert_w('/mnt/c/cygwin/home/ephucle/tool_script/python/tr_tool')
    'C:\\cygwin\\home\\ephucle\\tool_script\\python\\tr_tool'
    """

    windows_roots = __parse_mounts()[1]
    linux_root = __find_root(windows_roots, linux_path, "/")
    linux_leaf = linux_path[len(linux_root):]

    windows_root = windows_roots[linux_root]
    windows_leaf = linux_leaf.replace("/", "\\")

    return "".join([windows_root, windows_leaf])

def convert_u(windows_path):
    """ Convert an absolute Windows path to a Linux path. 
    >>> convert_u('C:\\Users\\ephucle')
    '/mnt/c/Users/ephucle'
    """

    linux_roots = __parse_mounts()[0]
    windows_root = __find_root(linux_roots, windows_path, "\\")
    windows_leaf = windows_path[len(windows_root):]

    if not windows_leaf.startswith("\\"):
        raise Exception("Cannot convert relative Windows path")

    linux_root = linux_roots[windows_root]
    linux_leaf = windows_leaf.replace("\\", "/")

    return "".join([linux_root, linux_leaf])

def convert_m(linux_path):
    """ Convert a Linux path to a Windows path with forward slashes. 
    >>> convert_m('/mnt/c/Users/ephucle')
    'C:/Users/ephucle'
    """
    windows_roots = __parse_mounts()[1]
    linux_root = __find_root(windows_roots, linux_path, "/")
    linux_leaf = linux_path[len(linux_root):]
    windows_root = windows_roots[linux_root]

    return "".join([windows_root, linux_leaf])

def get_mtime(filepath):
	'''
	>>> get_mtime('./myfunc.py')
	1598935275.1095223
	'''
	return os.stat(filepath).st_mtime

if	__name__ == '__main__':
	main()