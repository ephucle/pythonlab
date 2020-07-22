#!/usr/bin/env python3

def trace(f):
    def g(x):
        print(f"1. start to call function {f.__name__} with value = {x}")
        value = f(x)
        print(f'2. return of f({x}) is {repr(value)}')
        return value
    return g

@trace
def fact(n):
	if n == 1:
		return 1
	else:
		return n*(fact(n-1))



print(fact(4))

