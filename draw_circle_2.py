from swampy.Gui import *
g = Gui()
g.title('Button demo gui')

#tao ra 1 canvas

canvas = g.ca(width=250, height=250)
canvas.config(bg='white')
entry = g.en(text='yellow')


def draw_circle_in_canvas():
	''' When the user presses the second button, it should read a color name from the Entry and use it to change the fill color of the circle. '''
	item = canvas.circle([0,0], 100)
	#get color from entry
	fill_color = entry.get()
	item.config(fill=fill_color, outline='red', width=15)

button = g.bu(text='First button', command=draw_circle_in_canvas)
g.mainloop()