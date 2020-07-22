from tkinter import *
#https://likegeeks.com/python-gui-examples-tkinter-tutorial/



window = Tk()

window.title("New Crash app")

#lbl = Label(window, text="Hello")
lbl = Label(window, text="Hello", font=("Arial Bold", 20))

lbl.grid(column=0, row=0)
window.geometry('350x200')

def clicked():
	#lbl.configure(text="Button was clicked !!")
	res = "Welcome to " + txt.get()
	lbl.configure(text= res)
#text box
txt = Entry(window,width=10)
txt.grid(column=1, row=0)

#Adding a button widget
btn = Button(window, text="Click Me", bg="orange", fg="red", command=clicked)
btn.grid(column=2, row=0)




window.mainloop()


