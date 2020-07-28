from swampy.Gui import *
g = Gui()
g.title('Button demo gui')

#tao ra 1 canvas

canvas = g.ca(width=250, height=250)
canvas.config(bg='white')

def draw_circle_in_canvas():
	#cai tien ve hong tam
	item = canvas.circle([0,0], 100, fill='red')
	item.config(fill='yellow', outline='red', width=15)
	item1 = canvas.circle([0,0], 70, fill='red')
	item1.config(fill='yellow', outline='red', width=15)
	item2 = canvas.circle([0,0], 40, fill='red')
	item2.config(fill='yellow', outline='red', width=15)
	item3 = canvas.circle([0,0], 10, fill='red')
	item3.config(fill='yellow', outline='red', width=15)
	
button = g.bu(text='First button', command=draw_circle_in_canvas)

g.mainloop()