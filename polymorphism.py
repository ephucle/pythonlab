#17.9  Polymorphism
#Functions that can work with several types are called polymorphic. 
#http://greenteapress.com/thinkpython/html/thinkpython018.html
#from Time1 import *
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c]+1
    return d

t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']

histogram(t)

print(t, histogram(t))

print("test test test hello world", histogram("test test test hello world"))

#def int_to_time(seconds):
#    """Makes a new Time object.
#
#    seconds: int seconds since midnight.
#    """
#    time = Time()
#    minutes, time.second = divmod(seconds, 60)
#    time.hour, time.minute = divmod(minutes, 60)
#    return time
# inside class Time:
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    def int_to_time(self, seconds):
        """
        Makes a new Time object.seconds: int seconds since midnight.
        """
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time
    def time_to_int(self):
        """Computes the number of seconds since midnight.time: Time object.
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return self.int_to_time(seconds)
    def increment(self, seconds):
        seconds += self.time_to_int()
        return self.int_to_time(seconds)


t1 = Time(7, 43)
t2 = Time(7, 41)
t3 = Time(5, 0)
print(f"t1 = {t1}, t2 = {t2}, t3 = {t3}")
print(f"t1.__add__(t2) = {t1.__add__(t2)}")
print(f"t1 + t2 = {t1+t2}")
print(f"t1 + t2 + t3 = {t1+t2+t3}")

#print(total)