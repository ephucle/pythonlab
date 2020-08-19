#!/usr/bin/env python3.8
from tkinter import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pickle


master = Tk()
master.title( "Basic Web Brower using tkinter" )

#width  = master.winfo_screenwidth()
#height = master.winfo_screenheight()

width  = 800
height = 600
master.geometry(f'{width}x{height}')

text = Text(master, width=200)
text.pack()

pages_set ={"https://vnexpress.net/", "https://tuoitre.vn/"}
with open("page_list.db", "wb") as file:
	pickle.dump(pages_set,file)



#this support select color of background
var_of_option = StringVar(master)
var_of_option.set("white") # initial value
option = OptionMenu(master, var_of_option, "white", "yellow", "green", "cyan")
option.pack()

#to input url address
entry = Entry(master, width=200)
entry.insert(END, 'https://vnexpress.net/')
entry.pack(side = TOP)

def do_web_browser():
	url = entry.get()
	print("Do web browser...")
	print("url path:",url)
	response  = urlopen(url)
	html_doc = response.read()
	soup = BeautifulSoup(html_doc, 'html.parser')
	#delete and insert data into text
	text.delete('1.0', END)
	text.insert('1.0', soup)
	
button = Button(master, text = "Download", command = do_web_browser)
button.pack(side = BOTTOM)

def change_text_bg_color():
	print ("value selected is", var_of_option.get())
	#update background color
	text['bg'] = var_of_option.get()
	#The colors 'white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', and 'magenta' will always be available. Other names may work, depending on your local installation.

button2 = Button(master, text = "Change bg color", command = change_text_bg_color)
button2.pack(side = BOTTOM)

master.mainloop()