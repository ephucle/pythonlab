import sys
numbers = sys.argv[1:]

n1= int(numbers[0])
n2= int(numbers[1])


def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

print ('LCM of', n1, n2, 'is: ', lcm(n1,n2))