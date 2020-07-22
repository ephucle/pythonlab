#!/usr/bin/env python3
#how to use
#./csv2xls.py sample.csv sample.xlsx
import sys
import csv
import xlsxwriter


csv_filename = sys.argv[1]
excel_filename = sys.argv[2]
#print(csv_filename)
#print(excel_filename)

workbook = xlsxwriter.Workbook(excel_filename)
worksheet = workbook.add_worksheet()
print(f"Converting  {csv_filename} to {excel_filename} by csv and xlsxwriter module...")

with open(csv_filename) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	#print(csv_reader)
	#<_csv.reader object at 0x7f983fc966d8>
	for row_index, row_data in enumerate(csv_reader):
		#row_data is a list
		#print (row_data)
		#save to excel
		for col_index, data in enumerate(row_data):
			worksheet.write(row_index, col_index, data)

workbook.close()
print(f"Successful convert {csv_filename} to {excel_filename}")