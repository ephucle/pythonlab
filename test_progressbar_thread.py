import tkinter as tk
from tkinter import ttk
import _thread
import time

def Gui():
   global root, mpb

   root = tk.Tk()

   button1 = tk.Button(root, text='Exit', command=root.destroy)
   button1.pack()

   mpb = ttk.Progressbar(root, mode="determinate")
   mpb.pack()

   mpb["maximum"] = 3000
   mpb["value"] = 1000

   root.mainloop()


def main():
    global root, mpb

    time.sleep(1)

    while True:
        mpb["value"] += 100
        #root.update_idletasks() # works without it

        #Do some other tasks.
        time.sleep(0.2)


if __name__ == '__main__':
    _thread.start_new_thread(Gui, ())
    _thread.start_new_thread(main, ())