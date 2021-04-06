#!/usr/bin/env python3
import re
from beautifultable import BeautifulTable
table = BeautifulTable()
table.column_headers = ["EMAIL ADD","USERNAME","HOST"]

with open('email_address_list.txt') as infile:
	for line in infile:
		line = line.strip()
		#print(line)
		m = re.search('([\S]*)@([\S]*)',line)
		if m:
			#print(line, "| USERNAME:",m.group(1)," | HOST:",m.group(2))
			table.append_row([line, m.group(1) ,  m.group(2)])
			
print(table)