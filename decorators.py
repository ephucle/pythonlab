def decorator(func):
	def wraper(*args,**kwargs):
		print ("some action happen before")
		func(*args,**kwargs)
		print ("some action happen after")
	return wraper


def do_twice(func):
	def wraper(*args,**kwargs):
		func(*args,**kwargs)
		func(*args,**kwargs)
	return wraper

@decorator
def say_hi(name):
	print("Hi ! " + name)

say_hi('world')

@do_twice
def say_bye(name):
	print("bye " + name)

say_bye('some one')

#ephucle@VN-00000267:/mnt/c/cygwin/home/ephucle/tool_script/python$ python3 decorators.py
#some action happen before
#Hi ! world
#some action happen after
#bye some one
#bye some one