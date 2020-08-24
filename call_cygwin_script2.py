#!/usr/bin/python
from subprocess import Popen, PIPE

cygwin = Popen(['bash'],stdin=PIPE,stdout=PIPE)
#result=cygwin.communicate(input=b"uname -a")
#print (result)

#result=cygwin.communicate(input=b"ls -ltr")
result=cygwin.communicate(input=b"which moshell")
print (result)