import tkinter as tk
from tkinter import ttk

mainWindow = tk.Tk()

def update_progress_bar():
    x = barVar.get()
    if x < 100:
        barVar.set(x+10)
        mainWindow.after(500, update_progress_bar)
    else:
        print("Complete")


barVar = tk.DoubleVar()
barVar.set(0)
bar = ttk.Progressbar(mainWindow, length=200, style='black.Horizontal.TProgressbar', variable=barVar, mode='determinate')


bar.grid(row=1, column=0)
button= tk.Button(mainWindow, text='Click', command=update_progress_bar)
button.grid(row=0, column=0)

mainWindow.mainloop()