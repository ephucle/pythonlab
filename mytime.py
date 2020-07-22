#http://greenteapress.com/thinkpython/html/thinkpython017.html
class Time(object):
	"""Represents the time of day.
	attributes: hour, minute, second
	"""
	def __init__(self, hour =9 , minute = 59, second=30):
		self.hour = hour
		self.minute = minute
		self.second = second
	def print_time(self):
		print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}" )
	def __str__(self):
		return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
	def __add__(self, other):
		h = self.hour + other.hour
		m = self.minute + other.minute
		s = self.second + other.second
		if s > 60:
			s -= 60
			m +=1
		if m > 60:
			m -= 60
			h += 1
		return Time(h,m,s)

def is_after(t1, t2):
	if (t1.hour *60 + t1.minute)*60 + t1.second <= (t2.hour *60 + t2.minute)*60 + t2.second: return True
	else: return False

t1= Time(10,30,58)
t2= Time(11,30,59)
#t1.print_time()
#t2.print_time()
print (str(t1), str(t2), is_after(t1, t2))

print (str(Time(10,8,9)), str(Time(9,9,9)) ,  is_after(Time(10,8,9), Time(9,9,9)))

t1= Time(10,30,30)
t2= Time(11,10,30)
print (f"t1 = {str(t1)}, t2 = {str(t2)}, t1+t2 = {str(t1+t2)}")

t1= Time(10,30,40)
t2= Time(11,10,30)
print (f"t1 = {str(t1)}, t2 = {str(t2)}, t1+t2 = {str(t1+t2)}")

t1= Time(10,30,10)
t2= Time(11,40,20)
print (f"t1 = {str(t1)}, t2 = {str(t2)}, t1+t2 = {str(t1+t2)}")

t1= Time(10,30,10)
t2= Time(12,40,20)
print (f"t1 = {str(t1)}, t2 = {str(t2)}, t1+t2 = {str(t1+t2)}")
