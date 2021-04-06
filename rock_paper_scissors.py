#!/usr/bin/env python3
#Rock, Paper & Scissors
import random

user_point = 0
computer_point = 0
round = 0
while True:
	round +=1
	try:
		user_input = int(input("Please select: 0_bao, 1_bua, 2_keo \n >>>"))
	except:
		print("input only 0,1,2")
	if user_input in [0,1,2]:
		mapping = {0:"bao", 1:"bua", 2:"keo" }
		user_input_text = mapping[user_input]
		print("Your choice:",user_input_text)
	else:
		#The continue statement in Python returns the control to the beginning of the while loop.
		print("input only 0,1,2")
		continue
	
	
	baobuakeo_list = ["bao", "bua", "keo"]
	# random item from list
	
	computer_choice = random.choice(baobuakeo_list)
	print("Computer choice:", computer_choice)
	
	
	def check_rule(player_input, computer_input):
		
		if player_input == "bao":
			if computer_input == "bua": return 1
			if computer_input == "keo": return 0
		if player_input == "bua":
			if computer_input == "keo": return 1
			if computer_input == "bao": return 0
		if player_input == "keo":
			if computer_input == "bao": return 1
			if computer_input == "bua": return 0
		if player_input==computer_input:
			return 0.5
	
	
	result = check_rule(user_input_text, computer_choice)
	result_map = {1:"YOU WIN", 0:"YOU LOOSE", 0.5:"DRAW"}
	print("COMPARE: ",result_map[result])
	##point calcu##
	if result == 0.5:
		user_point += 0.5
		computer_point += 0.5
	if result == 1:
		user_point += 1
		computer_point += 0
	if result == 0:
		user_point += 0
		computer_point += 1
	print("Points Summary:")
	print("round",round," | user:", user_point, "computer", computer_point)
	print("****************")