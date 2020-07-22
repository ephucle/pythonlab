import string
import random

passlen = int(input("len of pass:"))
numofchar = int(input("num of letter:"))
numofnumber = int(input("num of number:"))

password = ""
for i in range(numofchar):
	password+=random.choice(string.ascii_lowercase+string.ascii_uppercase)

#print (password)
	
for i in range(numofnumber):
	password+=random.choice(random.choice(string.digits))

#print (password)

for i in range(passlen- numofnumber-numofchar):
	password+=random.choice(random.choice("!#$%&\()*;<=>?@[]^_{|}~"))

print ("random password:")
print (password)

password = ''.join(random.sample(password,len(password)))
print(password)