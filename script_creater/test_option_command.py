#https://stackoverflow.com/questions/35974203/optionmenu-command-function-requires-argument
from tkinter import *

def update():
    x = optionvar.get()
    x = str(x)
    mylabel.config(text=x)

root = Tk()

l = []
for n in range(10):
    l.append(n)

t = tuple(l)

optionvar = IntVar()

optionvar.set('hello stackoverflow')

#mymenu  = OptionMenu(root, optionvar, *t, command=update)
mymenu = OptionMenu(root, optionvar, *t, command=lambda _: update())


mylabel = Label(root)

mymenu.pack()
mylabel.pack()

root.mainloop()