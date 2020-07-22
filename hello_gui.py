#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#https://github.com/michaelliao/learn-python3/blob/master/samples/gui/hello_gui.py
from tkinter import *
import tkinter.messagebox as messagebox
import datetime, os
import subprocess
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #tao ra mot cai input text ben trong widget, de nhap input tu user
        self.nameInput = Entry(self)
        self.nameInput.pack()

        #tao them 1 cai button ben trong widget
        self.alertButton = Button(self, text='Call Hello FUNC', command=self.hello)
        self.alertButton.pack()

        #tao them 1 cai button thu2 ben trong widget
        self.alertButton2 = Button(self, text='show current day time', command=self.show_current_daytime)
        self.alertButton2.pack()
        #add button to show calendar
        #tao them 1 cai button thu2 ben trong widget
        self.alertButton3 = Button(self, text='show calendar', command=self.show_calendar)
        self.alertButton3.pack()
    def hello(self):
        #'world is default input' if have no input from user
        name = self.nameInput.get() or 'world'
        #title of message box is "TITLE of Message BOX"
        messagebox.showinfo('TITLE of Message BOX', 'Nice to meet, %s' % name)
    def show_current_daytime(self):
        current_dt_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #title of message box is "Current daytime"
        messagebox.showinfo('Current daytime', current_dt_str)
    def show_calendar(self):
        #lenh nay chi in ket qua ra terminal thoi
        #current_cal = os.system('cal')
        (status ,output ) = subprocess.getstatusoutput('cal')
        #title of message box is "Current daytime"
        messagebox.showinfo('Calendar of this month', output)


# 主消息循环, Vòng lặp tin nhắn chính:
app = Application()

# 设置窗口标题, Đặt tiêu đề cửa sổ:
app.master.title('Hello World GUI')

app.mainloop()
