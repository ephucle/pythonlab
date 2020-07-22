import string
import random

def gen():
	s1= string.ascii_uppercase
	s2 =string.ascii_lowercase
	s3= string.digits
	s4= string.punctuation
	s = []
	s.extend(s1)
	s.extend(s2)
	s.extend(s3)
	s.extend(s4)
	# xao tron list
	random.shuffle(s)
	
	password = "".join(s)
	pass_length = int(input("pass_length:"))
	password = password[0:pass_length]
	print('Your password is:')
	print(password)

gen()

