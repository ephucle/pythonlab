#!/usr/bin/env python3
#2. Guess the Number

#The Goal: Similar to the first project, this project also uses the random module in Python. The program will first randomly generate a number unknown to the user. The user needs to guess what that number is. (In other words, the user needs to be able to input information.) If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear. You’ll need functions to check if the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.
#
#The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice. 

import sys
import random
import os


def getinput():
	try :
		n = int(input("Guess the number between [0,100]: "))
	except:
		print ("n must be an integer number")
	#print (type(n))
	return n


def main():
	#clear screen
	os.system('clear')
	target = random.randint(0,100)
	#print (target)
	n = getinput()

	
	while n != target:
		if n > target :
			print("So big..")
		if n < target :
			print("So small..")
		n = getinput()
	print('*'*20)
	print (n, "is the correct number")
	print('*'*20)
		
	
if __name__ == '__main__':
	main()