#!/usr/bin/env python3
#./mydoc.py 'sys'

#Problem 12: Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module

import sys,inspect
from importlib import __import__

#The dir function to get all entries of a module
#The inspect.isfunction function can be used to test if given object is a function
#x.__doc__ gives the docstring for x.
#The __import__ function can be used to import a module by name


module_name = sys.argv[1]
print(module_name)

all_items = dir(module_name)
for i, item in enumerate(all_items):
	print(i, item)
	print(f"{i}, try to import")
	try:
		x = __import__( item )
		print("import successful")
		print (type(x))
		print(callable(print))
	except:
		print(f"{i}, import item: {item} failure")

#check function
#callable(print)

#__import__(name, globals=None, locals=None, fromlist=(), level=0)
#    Import a module.
#
#    The 'globals' argument is used to infer where the import is occurring from
#    to handle relative imports. The 'locals' argument is ignored. The
#    'fromlist' argument specifies what should exist as attributes on the module
#    being imported (e.g. ``from module import <fromlist>``).  The 'level'
#    argument represents the package location to import from in a relative
#    import (e.g. ``from ..pkg import mod`` would have a 'level' of 2).
#(END)