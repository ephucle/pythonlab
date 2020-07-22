class Reverse_iter:
	def __init__(self, listn):
		self.listn = listn 
	def __iter__(self):
		self
	
	def __next__(self):
		
		if len(self.listn) > 0:
			#get last item
			last_item = self.listn[-1]
			#remove last items
			temp = self.listn
			del temp[-1]
			self.listn = temp
			return last_item
		else:
			raise StopIteration()
	
	def __str__(self):
		return str(self.listn)
	__repl__ = __str__
		