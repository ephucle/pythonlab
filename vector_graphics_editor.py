#!/usr/bin/env python3

from tkinter import *
from PIL import Image

canvas_width = 500
canvas_height = 150


def paint( event ):
	python_green = "#476042"
	x1, y1 = ( event.x - 1 ), ( event.y - 1 )
	x2, y2 = ( event.x + 1 ), ( event.y + 1 )
	#w.create_oval( x1, y1, x2, y2, fill = python_green)
	w.create_line(x1, y1, x2, y2, fill=python_green, width=3)

#>>> w.create_
#w.create_arc(        w.create_image(      w.create_oval(       w.create_rectangle(  w.create_window(
#w.create_bitmap(     w.create_line(       w.create_polygon(    w.create_text(

#w.create_oval(*args, **kw) method of tkinter.Canvas instance
#    Create oval with coordinates x1,y1,x2,y2.

master = Tk()
master.title( "Painting using Ovals" )
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack(side = BOTTOM)
def clear_canvas():
	print("clear canvas")
	w.delete("all")

def save_to_ps():
	print("save to ps")
	#https://www.kite.com/python/docs/Tkinter.Canvas.postscript
	ps = w.postscript(file = "ps_output_file" , colormode='color')


button = Button( master, text ="clear",  command=clear_canvas)
button.pack(side = BOTTOM)

button2 = Button( master, text ="save",  command=save_to_ps)
button2.pack(side = BOTTOM)

#postscript(**options) [#]
#Generates a Postscript rendering of the canvas contents. Images and embedded widgets are not included.

#postscript(cnf={}, **kw) method of tkinter.Canvas instance
#    Print the contents of the canvas to a postscript
#    file. Valid options: colormap, colormode, file, fontmap,
#    height, pageanchor, pageheight, pagewidth, pagex, pagey,
#    rotate, width, x, y.


mainloop()