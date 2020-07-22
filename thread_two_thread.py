#!/usr/bin/env python3
#https://www.tutorialspoint.com/python/python_multithreading.htm

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, count, delay):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.count = count
      self.delay = delay
   def run(self):
      print ("Starting " + self.name)
      #print time count lan, moi lan cach nhau delay giay
      print_time(self.name, self.count, self.delay)
      print ("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads

#try to use name variable
thread1 = myThread(threadID=1, name="Thread-1", count= 5, delay=2)
thread2 = myThread(threadID=2, name="Thread-2", count= 5, delay=4)
# Start new Threads
#then start a new thread by invoking the start(), which in turn calls run() method.
thread1.start()
thread2.start()

print ("Exiting Main Thread")