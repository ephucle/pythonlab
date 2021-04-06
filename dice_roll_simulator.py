#!/usr/bin/env python3
#https://levelup.gitconnected.com/21-python-mini-projects-with-codes-c4126e4131e4
#Dice Roll Simulator

import random
#randint(a, b) method of random.Random instance
#    Return random integer in range [a, b], including both end points.
while int(input("1 to Roll, 0 to Exit, \n >>> ")):
	n1 =  random.randint(0,6)
	print(n1)


