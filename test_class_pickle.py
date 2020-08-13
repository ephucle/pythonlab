#!/usr/bin/env python3
import pickle

class Account:
	def __init__(self, id, balance):
		self.id = id
		self.balance = balance
	def deposit(self, amount):
		self.balance += amount
	def withdraw(self, amount):
		self.balance -= amount

myac = Account('123', 100)
myac.deposit(800)
myac.withdraw(500)
print(myac.id, myac.balance)  #'123', 400

#save to file, luu 400 vao file
fd = open( "archive", "wb" ) 
pickle.dump( myac, fd)
fd.close()

#show lai ket qua sau khi luu
import myfunc
myfunc.call('ls -l | grep -i "archive"')

myac.deposit(200)
print(myac.id, myac.balance)  #'123', 600

#doc lai gia tri cu
fd = open( "archive", "rb" ) 
myac = pickle.load( fd )
fd.close()

#gia tri duoc luu trong file
print(myac.id, myac.balance)  #'123', 400

