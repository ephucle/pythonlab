#!/usr/bin/env python3
from zipfile import ZipFile
import sys

args = sys.argv
args = args[1::]

zip_output_filename, *input_filenames = args

#print(zip_output_filename)
#print(input_filenames)

#ephucle@VN-00000267:/mnt/c/cygwin/home/ephucle/tool_script/python$ ./zip.py test1.zip links.py json_request.py
#args ['test1.zip', 'links.py', 'json_request.py']
#zip_output_filename test1.zip
#input_filenames ['links.py', 'json_request.py']

#start zip
#https://docs.python.org/3/library/zipfile.html
with ZipFile(zip_output_filename, 'w') as myzip:
	for file in input_filenames:
		myzip.write(file)
print(f"successful zip {input_filenames} to {zip_output_filename}")