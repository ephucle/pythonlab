# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk

class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
	def add_button(self):
		self.Button(text="test button")
		#<create the rest of your GUI here>

if __name__ == "__main__":
	root = tk.Tk()
	#MainApplication(root).pack(side="top", fill="both", expand=True)
	app = MainApplication(root)
	app.add_button()
	root.mainloop()