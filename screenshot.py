import time
import pyautogui
import datetime
import tkinter as tk

def screenshot():
	#sleep 5 second
	#print("start wait 5 second")
	#time.sleep(5)

	timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
	filename = "screenshot_" + timestamp + ".png"
	#print("start screen shoot")
	img = pyautogui.screenshot(filename)
	img.show()

#chup man hinh
#screenshot()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button_shoot = tk.Button(frame,text = "Screenshoot",command=screenshot)
button_shoot.pack()

button_quit = tk.Button(frame,text = "Quit", command=quit)
button_quit.pack()

root.mainloop()
