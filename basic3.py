#https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import datetime
now = datetime.now()

#dinh dang can in 2014-07-05 14:34:14
d2 = now.strftime("%Y-%m-%d %H:%M:%S")
print("now: ", d2)