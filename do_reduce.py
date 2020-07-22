#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#https://raw.githubusercontent.com/michaelliao/learn-python3/master/samples/functional/do_reduce.py

from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))


#Help on built-in function reduce in module _functools:
#
#reduce(...)
#    reduce(function, sequence[, initial]) -> value
#
#    Apply a function of two arguments cumulatively to the items of a sequence,
#    from left to right, so as to reduce the sequence to a single value.
#    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
#    of the sequence in the calculation, and serves as a default when the
#    sequence is empty.
#(END)

#class map(object)
# |  map(func, *iterables) --> map object
# |
# |  Make an iterator that computes the function using arguments from
# |  each of the iterables.  Stops when the shortest iterable is exhausted.
# |
# |  Methods defined here:
# |
# |  __getattribute__(self, name, /)
# |      Return getattr(self, name).
# |
# |  __iter__(self, /)
# |      Implement iter(self).
# |
# |  __new__(*args, **kwargs) from builtins.type
# |      Create and return a new object.  See help(type) for accurate signature.
# |
# |  __next__(self, /)
# |      Implement next(self).
# |
# |  __reduce__(...)
# |      Return state information for pickling.
#(END)