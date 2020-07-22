#!/usr/bin/env python3
def my_enumerate(list_var):
	count = 0
	for item in list_var:
		yield(count, item)
		count += 1
