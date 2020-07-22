#!/usr/bin/python3
#https://www.tutorialspoint.com/python3/python_classes_objects.htm


class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )


#>>> import class12
#>>> em1 = Employee('hoang', 1200)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'Employee' is not defined

#>>> em1 = class12.Employee('hoang', 1200)
#>>> em1.
#em1.displayCount(     em1.displayEmployee(  em1.empCount          em1.name              em1.salary
#>>> em1.displayCount()
#Total Employee 1
#>>> em1.displayEmployee()
#Name :  hoang , Salary:  1200
#>>> em2 = class12.Employee('someone', 2000)
#>>> em2.
#em2.displayCount(     em2.displayEmployee(  em2.empCount          em2.name              em2.salary
#>>> em2.display()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'Employee' object has no attribute 'display'
#>>> em2.display
#em2.displayCount(     em2.displayEmployee(

#>>> em2.displayCount()
#Total Employee 2
#>>> em2.displayEmployee()
#Name :  someone , Salary:  2000
