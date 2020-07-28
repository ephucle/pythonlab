#from __future__ import print_function
#from swampy.Gui import *
from swampy.Gui import Gui

from PIL import Image,ImageTk

#help(ImageTk)

import sys, os
from tkinter import PhotoImage






#>>> import swampy.Gui as Gui
#>>> dir(Gui)
#['ALL', 'BBox', 'BOTTOM', 'Callable', 'CanvasTransform', 'E', 'END', 'Gui', 'GuiCanvas', 'Item', 'LEFT', 'N', 'Point', 'RIGHT', 'RotateTransform', 'S', 'ScaleTransform', 'SwirlTransform', 'TOP', 'Transform', 'W', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'flatten', 'get_options', 'gui_example', 'main', 'math', 'override', 'pair', 'pairiter', 'pop_options', 'remove_options', 'split_options', 'sys', 'tk_example', 'tkinter', 'underride', 'widget_demo']

#>>> import tkinter as tk
#>>> dir(tk)
#['ACTIVE', 'ALL', 'ANCHOR', 'ARC', 'BASELINE', 'BEVEL', 'BOTH', 'BOTTOM', 'BROWSE', 'BUTT', 'BaseWidget', 'BitmapImage', 'BooleanVar', 'Button', 'CASCADE', 'CENTER', 'CHAR', 'CHECKBUTTON', 'CHORD', 'COMMAND', 'CURRENT', 'CallWrapper', 'Canvas', 'Checkbutton', 'DISABLED', 'DOTBOX', 'DoubleVar', 'E', 'END', 'EW', 'EXCEPTION', 'EXTENDED', 'Entry', 'Event', 'EventType', 'FALSE', 'FIRST', 'FLAT', 'Frame', 'GROOVE', 'Grid', 'HIDDEN', 'HORIZONTAL', 'INSERT', 'INSIDE', 'Image', 'IntVar', 'LAST', 'LEFT', 'Label', 'LabelFrame', 'Listbox', 'MITER', 'MOVETO', 'MULTIPLE', 'Menu', 'Menubutton', 'Message', 'Misc', 'N', 'NE', 'NO', 'NONE', 'NORMAL', 'NS', 'NSEW', 'NUMERIC', 'NW', 'NoDefaultRoot', 'OFF', 'ON', 'OUTSIDE', 'OptionMenu', 'PAGES', 'PIESLICE', 'PROJECTING', 'Pack', 'PanedWindow', ------'PhotoImage' ----, 'Place', 'RADIOBUTTON', 'RAISED', 'READABLE', 'RIDGE', 'RIGHT', 'ROUND', 'Radiobutton', 'S', 'SCROLL', 'SE', 'SEL', 'SEL_FIRST', 'SEL_LAST', 'SEPARATOR', 'SINGLE', 'SOLID', 'SUNKEN', 'SW', 'Scale', 'Scrollbar', 'Spinbox', 'StringVar', 'TOP', 'TRUE', 'Tcl', 'TclError', 'TclVersion', 'Text', 'Tk', 'TkVersion', 'Toplevel', 'UNDERLINE', 'UNITS', 'VERTICAL', 'Variable', 'W', 'WORD', 'WRITABLE', 'Widget', 'Wm', 'X', 'XView', 'Y', 'YES', 'YView', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_cnfmerge', '_default_root', '_exit', '_flatten', '_join', '_magic_re', '_setit', '_space_re', '_splitdict', '_stringify', '_support_default_root', '_test', '_tkerror', '_tkinter', '_varnum', 'constants', 'enum', 'getboolean', 'getdouble', 'getint', 'image_names', 'image_types', 'mainloop', 're', 'sys', 'wantobjects']

#tk.PhotoImage
#class PhotoImage(Image)
# |  Widget which can display images in PGM, PPM, GIF, PNG format.
#PhotoImage reads a file and returns a PhotoImage object that Tkinter can display.

root = "./"
img_file_paths = []
for path, subdirs, files in os.walk(root):
		for name in files:
			file_path = os.path.join(path,name)
			#neu open duoc file bang image, thi file do chinh la image, neu ko dc thi bo qua
			try:
				with Image.open(file_path) as im:
					img_file_paths.append(file_path)
					print(file_path, im.format, "%dx%d" % im.size, im.mode)
			except IOError:
				pass
print(img_file_paths)
#sys.exit()

g = Gui()
canvas = g.ca(width=200,height=200)
first_image = img_file_paths.pop()
print(first_image)
#photo = PhotoImage(file='python.gif')
#photo = PhotoImage(file=first_image)
#canvas.image([0,0], image=photo)


first_image_path = img_file_paths.pop()
image = Image.open(first_image_path)
photo2 = ImageTk.PhotoImage(image)  #convert to ImageTk
#canvas.image([0,0], image=photo2)
g.la(image=photo2)

def show_next_image(event):
	global img_file_paths
	next_photo_path = img_file_paths.pop()
	print(next_photo_path)
	
	image = Image.open(next_photo_path)
	photo2 = ImageTk.PhotoImage(image)  #convert to ImageTk
	#update image in canvas
	g.la.config(image = photo2)
	

#https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
#<Button-1> A mouse button is pressed over the widget. Button 1 is the leftmost button, button 2 is the middle button (where available), and button 3 the rightmost button. 

canvas.bind("<Button-1>", show_next_image)

#image = Image.open('python_mini.gif')
#photo2 = ImageTk.PhotoImage(image)
#g.la(image=photo2)

g.mainloop()

#Starting with this example, write a program that takes the name of a directory and loops through all the files, displaying any files that PIL recognizes as images. You can use a try statement to catch the files PIL doesn’t recognize.
#When the user clicks on the image, the program should display the next one.