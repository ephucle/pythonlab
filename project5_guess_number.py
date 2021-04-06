#!/usr/bin/env python3
import random
hiden_number = random.randint(1,10)

times = 0

while times < 3:
	i = int(input("guess the number: "))
	times +=1
	if i == hiden_number:
		print("Hurra, YOU WIN !!!")
		break
	elif i > hiden_number:
		print("Too large")
	else:
		print("Two low")
else:
	print("YOU LOOSE !!!, 03 times reach")