#!/usr/bin/env python3
import sys
import math

def cale(n):
	e = math.e
	string = str(e)
	#e = round(math.e,n)
	list1 = string.split(".")	
	e_string = list1[0] + '.' + list1[1][:n]
	return e_string
	#return e

def cale2(n):
	#https://en.wikipedia.org/wiki/E_(mathematical_constant)
	#https://oeis.org/A001113
	temp ="2.71828182845904523536028747135266249775724709369995"
	list1 = temp.split(".")	
	e_string = list1[0] + '.' + list1[1][:n]
	return e_string

def giaithua(n):
	if n == 0 or n == 1 : 
		tich = 1
	else:
		tich = 1
		for i in range(1,n+1):
			tich = tich * i
	return tich
def cale3(n):
	#e = e = Sum_{k >= 0} 1/k! = lim_{x -> 0} (1+x)^(1/x).

	e = 0
	for i in range (2000):
		e +=  1/(giaithua(i))
	
	e= str(e)
	list1 = e.split(".")	
	e_string = list1[0] + '.' + list1[1][:n]
	return e_string

def main():
	#nho chuyen doi n sang so nguyen, loi hoai
	n = int(sys.argv[1])
	
	#print tim pi cach 1
	print ("e from math module")
	e = cale(n)
	print (e)
	
	#print e theo cach 2
	print ("e value from string")
	e2 = cale2(n)
	print (e2)
	
	#print tim e cach 3
	print ("Tinh bang cong thuc 3")
	e3 = cale3(n)
	print(e3)

if __name__ == '__main__':
	main()