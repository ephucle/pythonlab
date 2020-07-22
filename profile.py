#!/usr/bin/env python3
import time
def profile(f):
	def g(x):
		print(f"Start call func {f.__name__} with input {x}")
		start_time = time.time()
		#call f(x)
		value = f(x)
		end_time = time.time()
		elapsed_time = end_time - start_time
		print(f'time taken of {f.__name__}({x}): {elapsed_time} sec')
		return value
	return g

@profile
def fact(n):
	if n == 1:
		return 1
	else:
		return n*(fact(n-1))

print(fact(10))