import re
# Using readlines()
file1 = open('mytext.txt', 'r')
lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in lines:
    count += 1
    line = line.strip()
    #print("Line{}: {}".format(count, line))
    #xx = "guru99,education is fun"
    r1 = re.search(r"faj\w+",line, re.IGNORECASE)
    if r1:
        print(line," | ",r1.group())

    r2 = re.search(r"sp\w+",line, re.IGNORECASE)
    if r2:
        print(line," | ",r2.group())