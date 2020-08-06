#!/usr/bin/env python
import sqlite3 
class SimpleSqlite:
	def __init__(self, filename):
		self.filename = filename
	def get_table_names(self):
		'''
		>>> s = SimpleSqlite('hosts.db')
		>>> print(s.get_table_names())
		['hosts', 'hostnames', 'pingresults']

		'''
		conn = sqlite3.connect(self.filename)
		c = conn.cursor()
		rows = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
		table_names = []
		for row in rows:
			#print(row)
			table_names.append(*row)
		#('hosts',)    #*row help to unpack tuble
		#('hostnames',)
		return table_names #['hosts', 'hostnames']
	def create_table(self, table_name, fields = '(host TEXT, port INTEGER, status INTEGER, daytime TEXT)' ):
		conn = sqlite3.connect(self.filename)
		c = conn.cursor()
		#check if table exist
		#c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='hosts' ''')
		c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ''',(table_name,))
		if c.fetchone()[0]==1:
			print("Table existed")
			
		else:
			print("start to create table:")
			#c.execute('''CREATE TABLE hosts (host text, port INTEGER, status INTEGER, daytime text)''')
			c.execute("CREATE TABLE "+ table_name + " " + fields)
			
			conn.commit()
			print(f"Successful create table {table_name} in {self.filename}")
		conn.close()

	def get_all_database(self):
		result = []
		conn = sqlite3.connect('hosts.db')
		c = conn.cursor()
		for row in c.execute('SELECT * FROM hosts ORDER BY host'):
			#print(row)
			result.append(row)
		return result

	def get_table_detail(self,table_name):
		#get row from database
		result = []
		conn = sqlite3.connect(self.filename)
		c = conn.cursor()
		#https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
		#for row in c.execute("SELECT * FROM hosts WHERE host=?", (hostname,)):
		for row in c.execute("SELECT * FROM "+ table_name ):
			result.append(row)
		return result

	def insert_database(self, table_name, data =('8.8.8.8',53,1)):
		conn = sqlite3.connect(self.filename)
		c = conn.cursor()
		#c.execute("INSERT INTO hosts VALUES (?,?,?,?)", data)
		c.execute("INSERT INTO " + table_name + " VALUES (?,?,?,?)", data)
		conn.commit()
		conn.close()

#s = SimpleSqlite('expenses.db')
s = SimpleSqlite('hosts.db')
table_names = s.get_table_names()

print(table_names)

s.create_table("pingresults", '(host TEXT, port INTEGER, status INTEGER, daytime TEXT)')

print("tables after insert",s.get_table_names())

print("all detail on table hosts")
rows = s.get_table_detail('hosts')
for row in rows:
	print(row)

if __name__ == "__main__":
	import doctest
	doctest.testmod()