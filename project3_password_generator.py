#!/usr/bin/env python3
import string, random
upper = string.ascii_uppercase
lower =  string.ascii_lowercase
digits = string.digits
special_char = string.punctuation

all_chars = list(upper + lower+digits+special_char)
print("before shuffle: ", all_chars)
random.shuffle(all_chars)
print("after shuffle:", all_chars)

password = ""
pass_len = int(input("Password len: "))
for i in range(pass_len):
	password += random.choice(all_chars)

print("Password: ", password)
