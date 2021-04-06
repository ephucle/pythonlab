def printtype(var):
	print(type(var))
	
#s = 'abc'
#print("s:", s)
#it = iter(s)
#print(type(it))
#
#print(next(it))
#
#print(next(it))
#
#print(next(it))
#print(next(it))


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
printtype(iter(rev))
for char in rev:
	print(char)