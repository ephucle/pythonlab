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
def map_new(func, iterables):
	mapping = [func(i) for i in iterables]
	return mapping
	



y = map_new(lambda x:x*2,[1,2,3])
print(y)

f = lambda x:x*3
x2 =['a','b','c']
z = map_new(f, x2)
print(z)
