#!/usr/bin/env python3
#https://www.tutorialspoint.com/python/python_multithreading.htm

import threading
import time
import datetime
#exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, count, delay):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.count = count
      self.delay = delay
   def run(self):
      print ("Starting " + self.name)
      #add this for easy troubleshooting
      print ("Thread", self.threadID, "parameter:", "count=" + str(self.count), "delay=" + str(self.delay))
      #print time count lan, moi lan cach nhau delay giay
      print_time(self.name, self.count, self.delay)
      print ("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      #if exitFlag:
      #   threadName.exit()
      time.sleep(delay)
      now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      #print ("%s: %s" % (threadName, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
      print ("%s: %s" % (threadName, now))
      counter -= 1

# Create new threads

#try to use name variable
thread1 = myThread(threadID=1, name="Thread-1", count= 5, delay=2)
thread2 = myThread(threadID=2, name="Thread-2", count= 5, delay=4)
thread3 = myThread(threadID=3, name="Thread-3", count= 3, delay=6)
# Start new Threads
#then start a new thread by invoking the start(), which in turn calls run() method.
thread1.start()
thread2.start()
thread3.start()

print ("Exiting Main Thread")