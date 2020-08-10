#!/usr/bin/env python
import tkinter as tk
from decode_esi_multidcgm import *
def run():
	print("print something")
	

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

nodename = tk.Entry(root)
nodename.grid(row=0, column=1)

button = tk.Button(frame,text = "Decrypt",command=run)
button.pack()

button_quit = tk.Button(frame,text = "Quit", command=quit)
button_quit.pack()

root.mainloop()