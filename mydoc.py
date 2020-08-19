#!/usr/bin/env python3
import sys
import importlib

target_module_name = sys.argv[1]

print("target_module_name", target_module_name, type(target_module_name))

module = importlib.import_module(target_module_name)
print(module)  #<module 'collections' from '/usr/lib/python3.6/collections/__init__.py'>
module_items = dir(module)

print("attribule and method inside module", module_items)

print("Test callable for each attribute_name:")
function_list = []
attribute_list = []
for attribute_name in module_items:
	#https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
	method_to_call = getattr(module, attribute_name)
	print(attribute_name, callable(method_to_call))
	if callable(method_to_call):
		function_list.append(attribute_name)
		print("--------Help of function", attribute_name, "as below:---------")
		print(method_to_call.__doc__)
	else :
		attribute_list.append(attribute_name)


print("list of function of ", target_module_name, "is:")
print("\n".join(function_list))

print("list of attributes of ", target_module_name, "is:")
print("\n".join(attribute_list))


