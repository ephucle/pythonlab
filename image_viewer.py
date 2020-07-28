from swampy.Gui import Gui
import collections
from PIL import Image,ImageTk

import sys, os
from tkinter import PhotoImage

#>>> import swampy.Gui as Gui
#>>> dir(Gui)
#['ALL', 'BBox', 'BOTTOM', 'Callable', 'CanvasTransform', 'E', 'END', 'Gui', 'GuiCanvas', 'Item', 'LEFT', 'N', 'Point', 'RIGHT', 'RotateTransform', 'S', 'ScaleTransform', 'SwirlTransform', 'TOP', 'Transform', 'W', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'flatten', 'get_options', 'gui_example', 'main', 'math', 'override', 'pair', 'pairiter', 'pop_options', 'remove_options', 'split_options', 'sys', 'tk_example', 'tkinter', 'underride', 'widget_demo']


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

g = Gui()
canvas = g.ca(width=200,height=200)
image_path = './python_mini.GIF'
label1 = g.la(text = image_path)

#show image to canvas
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)  #convert to ImageTk
myimg = canvas.image([0,0], image=photo)

#click event
def callback(event):
	print ("clicked at", event.x, event.y)
	global img_file_paths
	
	#rotate list of image
	d = collections.deque(img_file_paths)
	d.rotate(1)
	img_file_paths= list(d)
	next_image_path = img_file_paths[-1]
	
	label1['text'] = next_image_path
	#update new image
	image2 = Image.open(next_image_path)
	global photo2   #very importance
	photo2 = ImageTk.PhotoImage(image2)
	canvas.itemconfigure(myimg, image=photo2) #myimg is origin image in canvas

canvas.bind("<Button-1>", callback)  #<Button-1>: is mouse left button

g.mainloop()

#Starting with this example, write a program that takes the name of a directory and loops through all the files, displaying any files that PIL recognizes as images. You can use a try statement to catch the files PIL doesn’t recognize.
#When the user clicks on the image, the program should display the next one.