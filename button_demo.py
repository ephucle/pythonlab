from swampy.Gui import *
g = Gui()
g.title('Button demo gui')
def make_button():
	botton2 = g.bu(text='Second button is created', command=make_label)
def make_label():
	g.la(text='Nice job !')
button = g.bu(text='First button', command=make_button)
g.mainloop()