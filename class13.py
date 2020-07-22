#!/usr/bin/python3

#https://www.tutorialspoint.com/python3/python_classes_objects.htm
#Class Inheritance

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method



#>>> class Parent:        # define parent class
#...     parentAttr = 100
#...     def __init__(self):
#...             print ("Calling parent constructor")
#...     def parentMethod(self):
#...             print ('Calling parent method')
#...     def setAttr(self, attr):
#...             Parent.parentAttr = attr
#...     def getAttr(self):
#...             print ("Parent attribute :", Parent.parentAttr)
#...
##>>>
#>>>
#>>> Parent.
#Parent.getAttr(       Parent.mro(           Parent.parentAttr     Parent.parentMethod(  Parent.setAttr(
#>>> Parent.__
#Parent.__abstractmethods__  Parent.__dictoffset__       Parent.__gt__(              Parent.__module__           Parent.__reduce_ex__(       Parent.__text_signature__
#Parent.__base__(            Parent.__dir__(             Parent.__hash__(            Parent.__mro__              Parent.__repr__(            Parent.__weakref__
#Parent.__bases__            Parent.__doc__              Parent.__init__(            Parent.__name__             Parent.__setattr__(         Parent.__weakrefoffset__
#Parent.__basicsize__        Parent.__eq__(              Parent.__init_subclass__(   Parent.__ne__(              Parent.__sizeof__(
#Parent.__call__(            Parent.__flags__            Parent.__instancecheck__(   Parent.__new__(             Parent.__str__(
#Parent.__class__(           Parent.__format__(          Parent.__itemsize__         Parent.__prepare__(         Parent.__subclasscheck__(
#Parent.__delattr__(         Parent.__ge__(              Parent.__le__(              Parent.__qualname__         Parent.__subclasses__(
#Parent.__dict__             Parent.__getattribute__(    Parent.__lt__(              Parent.__reduce__(          Parent.__subclasshook__(
#>>> Parent.__dict__
#mappingproxy({'__module__': '__main__', 'parentAttr': 100, '__init__': <function Parent.__init__ at 0x7f8970e84d90>, 'parentMethod': <function Parent.parentMethod at 0x7f8970e84e18>, 'setAttr': <function Parent.setAttr at 0x7f8970e84ea0>, 'getAttr': <function Parent.getAttr at 0x7f8970e84f28>, '__dict__': <attribute '__dict__' of 'Parent' objects>, '__weakref__': <attribute '__weakref__' of 'Parent' objects>, '__doc__': None})
#>>> class Child(Parent): # define child class
#...     def __init__(self):
#...             print ("Calling child constructor")
#...     def childMethod(self):
#...             print ('Calling child method')
#...
#>>> c = Child()
#Calling child constructor
#>>> p = Parent()
#Calling parent constructor
#>>> c.childMethod()
#Calling child method
#>>> p.
#p.getAttr(       p.parentAttr     p.parentMethod(  p.setAttr(
#>>> p.parentMethod()
#Calling parent method
#>>> c.
#c.childMethod(   c.getAttr(       c.parentAttr     c.parentMethod(  c.setAttr(
#>>> c.parentMethod()
#Calling parent method
#>>> c.setAttr(200)
#>>> c.getAttr()
#Parent attribute : 200
#>>> c.setAttr(500)
#>>> c.getAttr()
#Parent attribute : 500
#>>>