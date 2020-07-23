#Exercise 6  
#Download the code from this chapter (http://thinkpython.com/code/Time2.py). Change the attributes of Time to be a single integer representing seconds since midnight. Then modify the methods (and the function int_to_time) to work with the new implementation. You should not have to modify the test code in main. When you are done, the output should be the same as before. Solution: http://thinkpython.com/code/Time2_soln.py

class Time:
    def __init__(self, seconds=0):
        '''
        second: second from midnigh
        '''
        minutes, self.second = divmod(seconds, 60)
        self.hour, self.minute = divmod(minutes, 60)
        
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


t1 = Time(100)
t2 = Time(200)
t3 = Time(300)
print(f"t1 = {t1}, t2 = {t2}, t3 = {t3}")
print(f"t1.__add__(t2) = {t1.__add__(t2)}")
print(f"t1 + t2 = {t1+t2}")
print(f"t1 + t2 + t3 = {t1+t2+t3}")

#print(total)