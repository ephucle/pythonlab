import re
sum = 0

pattern = 'back'
if re.match(pattern, 'backup.txt'):  #ok 1
	sum += 1
if re.match(pattern, 'text.back'):   #nok
	sum += 2
if re.search(pattern, 'backup.txt'): #ok 4
	sum += 4
if re.search(pattern, 'text.back'): # ok 8
	sum += 8
if re.search(pattern, 'text.back.back'): # ok 16, chi tinh 1 lan
	sum += 16

print(sum) #1 4 8 16 = 13 16 = 29