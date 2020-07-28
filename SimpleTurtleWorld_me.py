from swampy.TurtleWorld import TurtleWorld, Turtle

class SimpleTurtleWorld(TurtleWorld):
	"""This class is identical to TurtleWorld, but the code that
	lays out the GUI is simplified for explanatory purposes."""

	def setup(self):
		self.row()
		self.canvas = self.ca(width=400, height=400, bg='white')
		#self.col()
		#The first widget in the column is a grid Frame, which contains four buttons arranged two-by-two:
		self.gr(cols=2)
		self.bu(text='Print canvas', command=self.canvas.dump)
		self.bu(text='Quit', command=self.quit)
		self.bu(text='Make Turtle', command=self.make_turtle)
		self.bu(text='Clear', command=self.clear)
		self.endgr()
		self.row([0,1], pady=30)
		self.bu(text='Run file', command=self.run_file)
		self.en_file = self.en(text='snowflake.py', width=5)
		self.endrow()
world = SimpleTurtleWorld()
world.setup()