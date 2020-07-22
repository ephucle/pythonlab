#!/usr/bin/env python3
#1. Dice Rolling Simulator
#
#The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice. 

import sys
import random


def getinput():
	try :
		min = int(input("input min: "))
		max = int(input("input max: "))
	except:
		print ("min /max phai la so nguyen lon hon 0")
	
	#print min, max
	if min >= max:
		print ("min must be lower then max, ==>input again")
		sys.exit()
	return (min,max)


def main():
	(min, max ) = getinput()

	checker = ''
	i = 1
	while checker != 'n':
		print (i, "Tha xuc xac:", random.randint(min,max))
		checker = str(input("===> continue [y/n]: "))
		i += 1
	
if __name__ == '__main__':
	main()