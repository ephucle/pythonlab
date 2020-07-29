#!/usr/bin/env python
#usage
#./ping.py '8.8.8.8' 53
#result: Test TCP connection to 8.8.8.8:53:True

import argparse
import socket
import sys
import sqlite3 
import datetime

def create_sqlite_table():
	conn = sqlite3.connect('hosts.db')
	c = conn.cursor()
	# Create table
	#check if table exist
	c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='hosts' ''')
	if c.fetchone()[0]==1:
		print("Table existed")
		
	else:
		print("start to create table:")
		#c.execute('''CREATE TABLE hosts (host text, port INTEGER, status INTEGER)''')
		c.execute('''CREATE TABLE hosts (host text, port INTEGER, status INTEGER, daytime text)''')
		
		conn.commit()
		print("Successful create sqlite hosts.db with table hosts")
	conn.close()

def get_all_database():
	result = []
	conn = sqlite3.connect('hosts.db')
	c = conn.cursor()
	for row in c.execute('SELECT * FROM hosts ORDER BY host'):
		#print(row)
		result.append(row)
	return result

def get_by_host(hostname):
	#get row from database
	result = []
	conn = sqlite3.connect('hosts.db')
	c = conn.cursor()
	#https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
	for row in c.execute("SELECT * FROM hosts WHERE host=?", (hostname,)):
		#print(row) #('8.8.8.8', 53, 1)
		result.append(row)
	return result

def insert_database(data =('8.8.8.8',53,1)):
	conn = sqlite3.connect('hosts.db')
	c = conn.cursor()
	c.execute("INSERT INTO hosts VALUES (?,?,?,?)", data)
	
	conn.commit()
	conn.close()
	

	
create_sqlite_table()
#print("All data in sqlite database:")
#all_hosts = get_all_database()
#print(type(all_hosts))
#print(all_hosts)

#insert_database(data = ('8.8.8.8',53,1,2020-07-29 16:14:45))
#insert_database(data = ('8.8.4.4',53,1,2020-07-29 16:14:45))
#print("after insert")
#print_database()

print("get data of host '8.8.8.8'")
host_data = get_by_host('8.8.8.8')
print(host_data)
#sys.exit()


parser = argparse.ArgumentParser()
parser.add_argument("host", help="host name or ip address", type=str)
parser.add_argument("port", help="port", type=int)




def internet(host="8.8.8.8", port=53, timeout=3):
	"""
	Host: 8.8.8.8 (google-public-dns-a.google.com)
	OpenPort: 53/tcp
	Service: domain (DNS/TCP)
	"""
	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		return 1
	except socket.error as ex:
		print(ex)
		return 0




#host = "8.8.8.8"
#port = 53
#test_result = internet(host, port)
#print(f"Test TCP connection to {host}:{port}:{test_result}")

#host = "vnexpress.net"
#port = 443
#test_result = internet(host, port)
#print(f"Test TCP connection to {host}:{port}:{test_result}")



args = parser.parse_args()
host = args.host
port = args.port
print(f"host= {host}, port= {port}") #8.8.8.8, 53

current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
connection_status = internet(host, port)
print(f"Test TCP connection to {host}:{port}:{connection_status}")
insert_database(data = (host,port,connection_status, current))

#print all database
#print(get_all_database())
#
##test code
#ephucle@VN-00000267:/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab$ ./ping.py "8.8.4.4" 53
#Table existed
#get data of host '8.8.8.8'
#[('8.8.8.8', 53, 1, '2020-07-29 16:15:37')]
#host= 8.8.4.4, port= 53
#Test TCP connection to 8.8.4.4:53:1
#[('8.8.4.4', 53, 1, '2020-07-29 16:15:46'), ('8.8.8.8', 53, 1, '2020-07-29 16:15:37'), ('tuoitre.vn', 443, 1, '2020-07-29 16:14:28'), ('vnexpress.net', 443, 1, '2020-07-29 16:14:45')]
